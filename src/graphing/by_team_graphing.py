import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

league = "mlb"
file = f'results/{league}_by_team.csv'

df = pd.read_csv(file)

num_rows, num_cols = df.shape
x_labels = df.iloc[:, 0] 
x = np.arange(num_rows)
bar_width = 0.2 

# graph 1 (just brier score)
fig, ax = plt.subplots(figsize=(8, 4))
ax.bar(x, df.iloc[:, 1], width=bar_width, label=df.columns[1])
ax.set_xticks(x)
ax.set_xticklabels(x_labels, rotation=45, ha='right')
ax.set_xlabel("Teams")
ax.set_ylabel("Brier Score")
ax.set_title(f"Brier Score by Team")
plt.tight_layout()
plt.savefig(f'figures/by_team/{league}_by_team_bs.png')
plt.close(fig)

# graph 2 (just log loss)
fig, ax = plt.subplots(figsize=(8, 4))
ax.bar(x, df.iloc[:, 2], width=bar_width, label=df.columns[2])
ax.set_xticks(x)
ax.set_xticklabels(x_labels, rotation=45, ha='right')
ax.set_xlabel("Teams")
ax.set_ylabel("Log Loss")
ax.set_title(f"Log Loss by Team")
plt.tight_layout()
plt.savefig(f'figures/by_team/{league}_by_team_log.png')
plt.close(fig)

# graph 3 (3 bss)
columns = df.columns[-3:]
offsets = np.arange(len(columns)) * bar_width

fig, ax = plt.subplots(figsize=(12, 6))
for i, col in enumerate(columns):
    ax.bar(x + offsets[i] - bar_width * (len(columns) - 1) / 2,
           df[col],
           width=bar_width,
           label=col)
ax.set_xticks(x)
ax.set_xticklabels(x_labels, rotation=45, ha='right')
ax.set_xlabel("Teams")
ax.set_ylabel("Brier Skill Scores")
ax.set_title("Brier Skill Scores by Team")
ax.legend(title="Columns")
plt.tight_layout()
plt.savefig(f'figures/by_team/{league}_by_team_bss.png')
plt.close(fig)
