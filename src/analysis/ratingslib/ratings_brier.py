import pandas as pd

leagues = ['nfl', 'nhl', 'mlb', 'nba']
brier_scores_list = []

for league in leagues:
    files = ['half_', '']
    for file in files:
        df = pd.read_csv(f'results/ratings/{league}_{file}ratingslib_predictions.csv')

        df.loc[df['FTHG'] > df['FTAG'], 'result'] = 1
        df.loc[df['FTHG'] < df['FTAG'], 'result'] = 0 

        brier_score1 = ((df['elopoint_prediction'] - df['result']) ** 2).mean()
        brier_score2 = ((df['elowin_prediction'] - df['result']) ** 2).mean()
        brier_score3 = ((df['keener_prediction'] - df['result']) ** 2).mean()
        brier_score4 = ((df['massey_prediction'] - df['result']) ** 2).mean()
        brier_score5 = ((df['od_prediction'] - df['result']) ** 2).mean()

        brier_scores_list.append(pd.DataFrame({
            'Prediction_Method': [
                f'{league}_{file}elo_point', f'{league}_{file}elo_win', f'{league}_{file}keener', f'{league}_{file}massey', f'{league}_{file}od'
            ],
            'Brier_Score': [brier_score1, brier_score2, brier_score3, brier_score4, brier_score5]
        }))

brier_scores_df = pd.concat(brier_scores_list, ignore_index=True)
brier_scores_df.to_csv('results/ratings/ratingslib_brier_scores.csv', index=False)
