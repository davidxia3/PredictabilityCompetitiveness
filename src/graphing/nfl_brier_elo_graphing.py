import pandas as pd
import matplotlib.pyplot as plt

results_df = pd.read_csv("results/nfl_by_model.csv")

results_df = results_df.sort_values(by="season")

plt.figure(figsize=(10, 6))

plt.plot(results_df["season"], results_df["moneyline_brier_score"], label="Betting Market", marker='o', color='green',linewidth=3,markersize=10)
plt.plot(results_df["season"], results_df["baseline_brier_score"], label="Historical Home Win Probability Model", marker='o', color='red',linewidth=3,markersize=10)
plt.plot(results_df["season"], results_df["elo_brier_score"], label="Elo Model", marker='o', color='blue',linewidth=3,markersize=10)
plt.plot(results_df["season"], [0.25]*len(results_df["season"]), label="Coinflip Model", marker='o',color='purple',linewidth=3,markersize=10)

plt.xticks(ticks=range(len(results_df["season"])), labels=results_df["season"], rotation=45)
plt.ylim(0.15,0.26)
plt.xlabel("Season",fontsize=20)
plt.ylabel("Score",fontsize=20)
plt.title("Brier Scores of Different Models by Season",fontsize=25)
plt.legend(fontsize=15)
plt.grid(True)
plt.tick_params(axis='both', which='major', labelsize=15)

plt.tight_layout()

plt.savefig("figures/brier_score_by_model.png", dpi=300, bbox_inches='tight')