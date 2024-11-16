import pandas as pd
from sklearn.metrics import brier_score_loss


# calculates brier score for entirety of league by season
league = "nfl"
df = pd.read_csv(f'processed_data/{league}_espn_combined.csv')

season_groups = df.groupby('tournament')

seasons = []
brier_scores = []

for season, group in season_groups:
    brier = brier_score_loss(group['result'], group['avg_prob_1'])
    seasons.append(season)
    brier_scores.append(brier)


df = pd.DataFrame({'season': seasons, 'brier_score': brier_scores})

df.to_csv(f'results/seasonal_brier/{league}_seasonal_brier.csv', index=False)
