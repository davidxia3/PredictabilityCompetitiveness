import pandas as pd
import matplotlib.pyplot as plt

results_df = pd.read_csv("results/moneyline/modelwise/nfl_modelwise.csv")
results_df = results_df.sort_values(by="season")

all_years = [str(year) for year in range(2009,2022)]

plt.figure(figsize=(10, 6))

plt.plot(results_df["season"], results_df["moneyline_brier_score"], label="Betting Market", marker='o', color='green', linewidth=3, markersize=10)
plt.plot(results_df["season"], results_df["elo_brier_score"], label="Elo Model", marker='o', color='magenta', linewidth=3, markersize=10)
plt.plot(results_df["season"], results_df["baseline_brier_score"], label="Home Bias Coinflip Model", marker='o', color='cyan', linewidth=3, markersize=10)
plt.plot(results_df["season"], [0.25] * len(results_df["season"]), label="Coinflip Model", marker='o', color='black', linewidth=3, markersize=10)

all_years = sorted(all_years)
plt.xticks(ticks=range(len(all_years)), labels=all_years, rotation=0)
plt.ylim(0.15, 0.26)
plt.xlabel("Season", fontsize=20)
plt.ylabel("Brier Score", fontsize=20)
plt.text(-1.7, 0.245, "Less Accurate", fontsize=12, ha='center', va='center', rotation=90)
plt.text(-1.7, 0.165, "More Accurate", fontsize=12, ha='center', va='center', rotation=90)
plt.legend(fontsize=15)
plt.grid(True)
plt.tick_params(axis='both', which='major', labelsize=15)

plt.tight_layout()
plt.savefig("figures/nfl_brier_modelwise.png", dpi=300, bbox_inches='tight')
plt.close()
