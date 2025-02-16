import pandas as pd


leagues = ['nfl', 'nhl', 'mlb', 'nba']
for league in leagues:
    df = pd.read_csv(f'processed_data/{league}_ratingslib_predictions.csv')

    df.loc[df['FTHG'] > df['FTAG'], 'result'] = 1
    df.loc[df['FTHG'] < df['FTAG'], 'result'] = 0 

    brier_score1 = ((df['elopoint_prediction'] - df['result']) ** 2).mean()

    brier_score2 = ((df['elowin_prediction'] - df['result']) ** 2).mean()

    brier_score3 = ((df['keener_prediction'] - df['result']) ** 2).mean()

    brier_score4 = ((df['massey_prediction'] - df['result']) ** 2).mean()

    brier_score5 = ((df['od_prediction'] - df['result']) ** 2).mean()


    brier_scores_df = pd.DataFrame({
        'Prediction_Method': ['elo_point', 'elo_win', 'keener', 'massey', 'od'],
        'Brier_Score': [brier_score1, brier_score2, brier_score3, brier_score4, brier_score5]
    })

    brier_scores_df.to_csv(f'results/ratings/{league}_brier_score.csv', index=False)

