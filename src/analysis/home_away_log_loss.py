import pandas as pd
from sklearn.metrics import log_loss

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

    log_losses = {
        scenario: log_loss(scenario_df['result'], scenario_df['avg_prob_1'])
        for scenario, scenario_df in scenarios.items()
    }

    l.append(league)
    predictions.append(1)
    scores.append(log_losses['prediction_1'])

    l.append(league)
    predictions.append(0)
    scores.append(log_losses['prediction_0'])

result_df = pd.DataFrame({'league': l, 'prediction': predictions, 'log_loss': scores})

result_df.to_csv(f'results/home_away_log_loss.csv', index=False)
