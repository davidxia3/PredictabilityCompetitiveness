import pandas as pd
import matplotlib.pyplot as plt

winrates_df = pd.read_csv("results/nfl_team_win_rates.csv")
brier_scores_df = pd.read_csv("results/nfl_by_team.csv")

merged_df = pd.merge(winrates_df, brier_scores_df, on='team')

plt.figure(figsize=(8, 6))
plt.scatter(merged_df['win_rate'], merged_df['brier_score'], color='blue', alpha=0.7)

plt.xlabel('Win Rate', fontsize=14)
plt.ylabel('Brier Score', fontsize=14)

plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig("figures/nfl_brier_vs_win_rate.png", dpi=300, bbox_inches='tight')
