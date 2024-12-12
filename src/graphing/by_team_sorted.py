import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

team_colors = {
    "ARI": "#97233F", "ATL": "#A71930", "BAL": "#241773", "BUF": "#00338D",
    "CAR": "#0085CA", "CHI": "#C83803", "CIN": "#FB4F14", "CLE": "#311D00",
    "DAL": "#003594", "DEN": "#FB4F14", "DET": "#0076B6", "GB": "#203731",
    "HOU": "#03202F", "IND": "#002C5F", "JAX": "#006778", "KC": "#E31837",
    "LV": "#A5ACAF", "LAC": "#0080C6", "LAR": "#003594", "MIA": "#008E97",
    "MIN": "#4F2683", "NE": "#002244", "NO": "#D3BC8D", "NYG": "#0B2265",
    "NYJ": "#125740", "PHI": "#004C54", "PIT": "#FFB612", "SF": "#AA0000",
    "SEA": "#002244", "TB": "#D50A0A", "TEN": "#0C2340", "WSH": "#5A1414"
}

league = "nfl"
file = f'results/{league}_by_team.csv'
df = pd.read_csv(file)
df = df.sort_values(by="brier_score", ascending=True)

num_rows, num_cols = df.shape
x_labels = df.iloc[:, 0]  
x = np.arange(num_rows)
bar_width = 0.5

fig, ax = plt.subplots(figsize=(12, 6))
bars = ax.bar(
    x, 
    df.iloc[:, 1], 
    width=bar_width, 
    color=[team_colors[team] for team in x_labels], 
    edgecolor="black" 
)

ax.set_xticks(x)
ax.set_xticklabels(x_labels, rotation=270, ha='right', fontsize=15)
ax.set_xlabel("Teams", fontsize=20)
ax.set_ylabel("Brier Score", fontsize=20)
plt.tick_params(axis='y', which='major', labelsize=15)

plt.ylim(0.15, 0.26)
plt.tight_layout()

plt.savefig(f'figures/{league}_brier_by_team_sorted.png', dpi=300, bbox_inches='tight')
