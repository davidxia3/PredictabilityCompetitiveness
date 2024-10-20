import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import roc_auc_score

league = "nhl"
df = pd.read_csv(f'data/combined/{league}_market.csv')

season_groups = df.groupby('tournament')

seasons = []
auc_values = []

for season, group in season_groups:
    auc = roc_auc_score(group['result'], group['avg_prob_1'])
    seasons.append(season)
    auc_values.append(auc)

plt.figure(figsize=(10, 6))
plt.plot(seasons, auc_values, marker='o')
plt.xlabel('Season')
plt.ylabel('AUC')
plt.title(f'AUC by season ({league})')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.savefig(f'figures/seasonal_auc/{league}_seasonal_auc.png')
plt.show()
