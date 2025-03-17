import pandas as pd

leagues = ['nfl', 'nhl', 'mlb', 'nba']
brier_scores_list = []

for league in leagues:
    file_path = f'results/ratingslib/{league}_ratingslib_predictions.csv'
    df = pd.read_csv(file_path)

    df.loc[df['FTHG'] > df['FTAG'], 'result'] = 1
    df.loc[df['FTHG'] < df['FTAG'], 'result'] = 0 

    df["Date"] = pd.to_datetime(df["Date"])

    season_game_counts = df.groupby("Season").size()


    df_half = []
    df_full = []

    for idx, row in df.iterrows():
        season = row["Season"]
        current_date = row["Date"]

        games_before = sum((df["Season"] == season) & (df["Date"] < current_date))

        if games_before > season_game_counts[season] / 2:
            df_half.append(row)
        df_full.append(row)

    df_half = pd.DataFrame(df_half)
    df_full = pd.DataFrame(df_full)

    def compute_brier_scores(df_subset, period):
        return [
            {'Prediction_Method': f'{league}_{period}_elo_point', 'Brier_Score': ((df_subset['elopoint_prediction'] - df_subset['result']) ** 2).dropna().mean()},
            {'Prediction_Method': f'{league}_{period}_elo_win', 'Brier_Score': ((df_subset['elowin_prediction'] - df_subset['result']) ** 2).dropna().mean()},
            {'Prediction_Method': f'{league}_{period}_keener', 'Brier_Score': ((df_subset['keener_prediction'] - df_subset['result']) ** 2).dropna().mean()},
            {'Prediction_Method': f'{league}_{period}_massey', 'Brier_Score': ((df_subset['massey_prediction'] - df_subset['result']) ** 2).dropna().mean()},
            {'Prediction_Method': f'{league}_{period}_od', 'Brier_Score': ((df_subset['od_prediction'] - df_subset['result']) ** 2).dropna().mean()},
        ]

    brier_scores_list.extend(compute_brier_scores(df_full, "full"))
    brier_scores_list.extend(compute_brier_scores(df_half, "half"))

brier_scores_df = pd.DataFrame(brier_scores_list)
brier_scores_df.to_csv('results/ratingslib/ratingslib_half_full_brier.csv', index=False)

