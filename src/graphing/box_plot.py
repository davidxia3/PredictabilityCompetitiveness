import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


leagues = ['MLB', 'NHL', 'NFL', 'NBA']
csv_files = [
    "processed_data/mlb_espn_combined.csv",  
    "processed_data/nhl_espn_combined.csv", 
    "processed_data/nfl_espn_combined_with_elo.csv",
    "processed_data/nba_espn_combined.csv",
]
column_name = "avg_prob_1"
colors = ['blue', 'orange', 'red', 'purple']

dfs = [pd.read_csv(file) for file in csv_files]
data = [df[column_name].dropna() for df in dfs]

leagues_reversed = leagues[::-1]
data_reversed = data[::-1]
colors_reversed = colors[::-1]

plt.figure(figsize=(10, 6))
bp = plt.boxplot(data_reversed, patch_artist=True, labels=leagues_reversed, vert=False) 

for patch, color in zip(bp['boxes'], colors_reversed):
    patch.set_facecolor(color)
    patch.set_linewidth(3)

for element in ['whiskers', 'caps']:
    plt.setp(bp[element], linewidth=2)
plt.setp(bp['medians'], linewidth=2, color='black') 

plt.axvline(0.5, color='black', linestyle='--', linewidth=4)


plt.xlabel("Home Team Win Probability", fontsize=20)
plt.grid(True, linestyle="--", alpha=0.6)
xticks = np.arange(0, 1.1, 0.1)
plt.xticks(xticks, fontsize=15)
plt.yticks(fontsize=15)
plt.tight_layout()

plt.savefig("figures/prob_box_plot.png", dpi=300, bbox_inches='tight')
