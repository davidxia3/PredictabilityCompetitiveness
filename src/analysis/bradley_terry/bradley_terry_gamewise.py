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

    return n/d

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

leagues = ['nba', 'nhl', 'mlb']

for league in leagues:
    league_csv = pd.read_csv(f'processed_data/ratingslib_formatted/{league}_ratingslib_formatted.csv')

    league_csv['winner'] = league_csv.apply(get_winner, axis=1)
    league_csv['loser'] = league_csv.apply(get_loser, axis=1)
    
    league_csv['bradley_terry_prediction'] = np.nan

    ratings_csv = pd.read_csv(f'processed_data/ratingslib_formatted/{league}_ratingslib_formatted.csv')
    ratings_csv['winner'] = ratings_csv.apply(get_winner, axis=1)
    ratings_csv['loser'] = ratings_csv.apply(get_loser, axis=1)

    ratings_csv['home_rating'] = np.nan
    ratings_csv['away_rating'] = np.nan
     
    for index, row in league_csv.iterrows():
        if index % 100 == 0:
            print(str(index) +" " + league) 

        season_total = league_csv[
            (league_csv['Season'] == row['Season'])]
        past_games = league_csv[
            (league_csv['Season'] == row['Season']) & 
            (pd.to_datetime(league_csv['Date'], format="%d/%m/%Y") < pd.to_datetime(row['Date'], format="%d/%m/%Y"))
        ]


        teams = sorted(list(set(past_games.HomeTeam) | set(past_games.AwayTeam)))
        t2i = {t: i for i, t in enumerate(teams)}

        df = past_games\
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

        iterate_df = pd.DataFrame(mat, columns=teams, index=teams)

        p, estimates = iterate(iterate_df, n=20)


        home_team, away_team = row['HomeTeam'], row['AwayTeam']

        if home_team in p and away_team in p:
            league_csv.at[index, 'bradley_terry_prediction'] = p[home_team] / (p[home_team] + p[away_team])
            ratings_csv.at[index, 'home_rating'] = p[home_team]
            ratings_csv.at[index, 'away_rating'] = p[away_team]


    league_csv.drop(columns=['winner', 'loser'], inplace=True)

    ratings_csv.drop(columns=['winner', 'loser'], inplace=True)


    league_csv.to_csv(f'results/bradley_terry/{league}_bradley_terry_predictions.csv', index=False)
    ratings_csv.to_csv(f'results/bradley_terry/{league}_bradley_terry_ratings.csv', index=False)
