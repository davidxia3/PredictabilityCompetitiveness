import pandas as pd
from sklearn.metrics import log_loss

# calculates log loss for the entirety of league by season
league = "nba"
df = pd.read_csv(f'processed_data/{league}_espn_combined.csv')

season_groups = df.groupby('tournament')

seasons = []
log_losses = []

for season, group in season_groups:
    loss = log_loss(group['result'], group['avg_prob_1'])
    seasons.append(season)
    log_losses.append(loss)

df = pd.DataFrame({'season': seasons, 'log_loss': log_losses})

df.to_csv(f'results/seasonal_log_loss/{league}_seasonal_log_loss.csv', index=False)
