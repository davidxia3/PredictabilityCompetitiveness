import pandas as pd
from sklearn.metrics import log_loss

leagues = ['nfl', 'nhl', 'mlb', 'nba']
log_loss_scores_list = []

for league in leagues:
    file_path = f'results/bradley_terry/{league}_bradley_terry_predictions.csv'
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

    def compute_log_loss(df_subset, period):
        df_clean = df_subset[['bradley_terry_prediction', 'result']].dropna()

        if len(df_clean) == 0:
            return [{'Prediction_Method': f'{league}_{period}_bradley_terry', 'Log_Loss': None}]

        return [{
            'Prediction_Method': f'{league}_{period}_bradley_terry',
            'Log_Loss': log_loss(df_clean['result'], df_clean['bradley_terry_prediction'])
        }]

    log_loss_scores_list.extend(compute_log_loss(df_full, "full"))
    log_loss_scores_list.extend(compute_log_loss(df_half, "half"))

log_loss_scores_df = pd.DataFrame(log_loss_scores_list)
log_loss_scores_df.to_csv('results/bradley_terry/bradley_terry_half_full_log_loss.csv', index=False)
