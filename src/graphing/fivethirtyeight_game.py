import pandas as pd
import matplotlib.pyplot as plt

file = "results/fivethirtyeight_results.csv"
df = pd.read_csv(file)

labels = df['season']
percentiles = df['percentiles']
placements = df['placements']

fig, ax = plt.subplots(figsize=(10, 6))

bars = ax.bar(labels, placements, color='skyblue')

for i, bar in enumerate(bars):
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), f'{percentiles[i]}%', 
            ha='center', va='bottom', fontsize=10, color='black')

ax.set_xlabel('Season')
ax.set_ylabel('Placements')
ax.set_title('Moneyline Performance in FiveThirtyEight NFL Forecasting Game')

plt.xticks(rotation=45, ha='right')

plt.tight_layout()
plt.savefig('figures/fivethirtyeight_game.png')
