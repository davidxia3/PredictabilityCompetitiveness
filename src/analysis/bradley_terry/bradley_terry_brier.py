import pandas as pd

leagues = ['nfl', 'nhl', 'mlb', 'nba']
brier_scores_list = []

for league in leagues:
    df = pd.read_csv(f'results/bradley_terry/{league}_bradley_terry_predictions.csv')

    df.loc[df['FTHG'] > df['FTAG'], 'result'] = 1
    df.loc[df['FTHG'] < df['FTAG'], 'result'] = 0 

    brier_score1 = ((df['bradley_terry_prediction'] - df['result']) ** 2).mean()

    brier_scores_list.append(pd.DataFrame({
        'Prediction_Method': [
            f'{league}_bradley_terry'
        ],
        'Brier_Score': [brier_score1]
    }))

brier_scores_df = pd.concat(brier_scores_list, ignore_index=True)
brier_scores_df.to_csv('results/bradley_terry/bradley_terry_brier_scores.csv', index=False)
