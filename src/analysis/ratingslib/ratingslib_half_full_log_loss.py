import pandas as pd
from sklearn.metrics import log_loss

leagues = ['nfl', 'nhl', 'mlb', 'nba']
log_loss_scores_list = []

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

    def compute_log_loss_scores(df_subset, period):
        methods = ['elopoint', 'elowin', 'keener', 'massey', 'od']
        results = []

        for method in methods:
            col_name = f'{method}_prediction'
            df_clean = df_subset[[col_name, 'result']].dropna()

            if len(df_clean) == 0:
                score = None
            else:
                score = log_loss(df_clean['result'], df_clean[col_name])

            results.append({
                'Prediction_Method': f'{league}_{period}_{method}',
                'Log_Loss': score
            })

        return results

    log_loss_scores_list.extend(compute_log_loss_scores(df_full, "full"))
    log_loss_scores_list.extend(compute_log_loss_scores(df_half, "half"))

log_loss_scores_df = pd.DataFrame(log_loss_scores_list)
log_loss_scores_df.to_csv('results/ratingslib/ratingslib_half_full_log_loss.csv', index=False)
