import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# cite https://datascience.oneoffcoder.com/btl-model.html

def get_estimate(i, p, df):
    get_prob = lambda i, j: np.nan if i == j else p.iloc[i] + p.iloc[j]
    n = df.iloc[i].sum()

    d_n = df.iloc[i] + df.iloc[:, i]
    d_d = pd.Series([get_prob(i, j) for j in range(len(p))], index=p.index)
    d = (d_n / d_d).sum()

    return n / d

def estimate_p(p, df):
    return pd.Series([get_estimate(i, p, df) for i in range(df.shape[0])], index=p.index)


def iterate(df, p=None, n=20, sorted=True):
    if p is None:
        p = pd.Series([1 for _ in range(df.shape[0])], index=list(df.columns))

    estimates = [p]

    for _ in range(n):
        p = estimate_p(p, df)
        p = p / p.sum()
        estimates.append(p)

    p = p.sort_values(ascending=False) if sorted else p
    return p, pd.DataFrame(estimates)


def get_winner(r):
    if pd.isna(r.FTHG) or pd.isna(r.FTAG):
        return np.nan
    if r.FTHG > r.FTAG:
        return r.HomeTeam
    elif r.FTHG < r.FTAG:
        return r.AwayTeam
    else:
        return np.nan

def get_loser(r):
    if pd.isna(r.FTHG) or pd.isna(r.FTAG):
        return np.nan
    if r.FTHG > r.FTAG:
        return r.AwayTeam
    elif r.FTHG < r.FTAG:
        return r.HomeTeam
    else:
        return np.nan

leagues = ['nfl', 'nba', 'nhl', 'mlb']

for league in leagues:
    league_csv = pd.read_csv(f'processed_data/ratingslib_formatted/{league}_ratingslib_formatted.csv')

    league_csv['winner'] = league_csv.apply(get_winner, axis=1)
    league_csv['loser'] = league_csv.apply(get_loser, axis=1)

    seasons = league_csv['Season'].unique()

    season_results = []

    for season in seasons:
        season_data = league_csv[league_csv['Season'] == season]
        
        teams = sorted(list(set(season_data.HomeTeam) | set(season_data.AwayTeam)))
        t2i = {t: i for i, t in enumerate(teams)}

        df = season_data\
            .groupby(['winner', 'loser'])\
            .agg('count')\
            .drop(columns=['AwayTeam', 'FTHG', 'FTAG'])\
            .rename(columns={'HomeTeam': 'n'})\
            .reset_index()
        df['r'] = df['winner'].apply(lambda t: t2i[t])
        df['c'] = df['loser'].apply(lambda t: t2i[t])

        n_teams = len(teams)
        mat = np.zeros([n_teams, n_teams])

        for _, r in df.iterrows():
            mat[r.r, r.c] = r.n

        season_df = pd.DataFrame(mat, columns=teams, index=teams)

        p, estimates = iterate(season_df, n=100)

        season_results.append(pd.DataFrame({f'team_{season}': p.index, f'prediction_{season}': p.values}))

    final_df = pd.concat(season_results, axis=1)

    final_df.to_csv(f'results/bradley_terry/{league}_seasonal_bradley_terry.csv', index=False)
