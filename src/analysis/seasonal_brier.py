import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import brier_score_loss

league = "mlb"
df = pd.read_csv(f'data/combined/{league}_market.csv')

season_groups = df.groupby('tournament')

seasons = []
brier_scores = []

for season, group in season_groups:
    brier = brier_score_loss(group['result'], group['avg_prob_1'])
    seasons.append(season)
    brier_scores.append(brier)

plt.figure(figsize=(10, 6))
plt.plot(seasons, brier_scores, marker='o')
plt.xlabel('Season')
plt.ylabel('Brier Score')
plt.title(f'Brier by season ({league})')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.savefig(f'figures/seasonal_brier/{league}_seasonal_brier.png')
plt.show()
