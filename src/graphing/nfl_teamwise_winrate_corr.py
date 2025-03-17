import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import pearsonr

winrates_df = pd.read_csv("results/nfl_teamwise_winrate.csv")
brier_scores_df = pd.read_csv("results/moneyline/teamwise/nfl_teamwise.csv")

merged_df = pd.merge(winrates_df, brier_scores_df, on='team')

x = abs(merged_df['win_rate'] - 0.5)
y = merged_df['brier_score']

slope, intercept = np.polyfit(x, y, 1)
regression_line = slope * x + intercept

correlation, p_value = pearsonr(x, y)

plt.figure(figsize=(8, 6))
plt.scatter(x, y, color='blue', alpha=0.7, label="Teams")
plt.plot(x, regression_line, color='red', linewidth=2, label=f"Regression Line\ny = {slope:.2f}x + {intercept:.2f}")

plt.text(0.02, 0.22, f"Correlation: {correlation:.2f}\nP-value: {p_value:.2e}", fontsize=12, color="black")

plt.xlabel('Absolute Win Rate Difference (|win_rate - 0.5|)', fontsize=14)
plt.ylabel('Brier Score', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(fontsize=12)
plt.tight_layout()

plt.savefig("figures/nfl_brier_winrate_corr.png", dpi=300, bbox_inches='tight')
