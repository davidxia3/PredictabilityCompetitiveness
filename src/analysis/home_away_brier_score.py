import pandas as pd

leagues = ["nfl", "mlb", "nba"]

l = []
predictions = []
scores = []

for league in leagues:
    df = pd.read_csv(f'processed_data/{league}_espn_combined.csv')

    df['pred'] = (df['avg_prob_1'] > 0.5).astype(int)

    scenarios = {
        'prediction_1': df[(df['pred'] == 1)],
        'prediction_0': df[(df['pred'] == 0)]
    }

    brier_scores = {
        scenario: ((scenario_df['avg_prob_1'] - scenario_df['result']) ** 2).mean()
        for scenario, scenario_df in scenarios.items()
    }

    l.append(league)
    predictions.append(1)
    scores.append(brier_scores['prediction_1'])

    l.append(league)
    predictions.append(0)
    scores.append(brier_scores['prediction_0'])

result_df = pd.DataFrame({'league': l, 'prediction': predictions, 'brier_score': scores})

result_df.to_csv(f'results/home_away_brier_score.csv', index=False)
