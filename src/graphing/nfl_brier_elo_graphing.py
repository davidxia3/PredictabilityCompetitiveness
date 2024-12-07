import pandas as pd
import matplotlib.pyplot as plt

results_df = pd.read_csv("results/temp.csv")

results_df = results_df.sort_values(by="season")

plt.figure(figsize=(10, 6))

plt.plot(results_df["season"], results_df["moneyline_brier_score"], label="Betting Market", marker='o', color='blue')
plt.plot(results_df["season"], results_df["baseline_brier_score"], label="Historical Home Win Probability Model", marker='o', color='green')
plt.plot(results_df["season"], results_df["elo_brier_score"], label="Elo Model", marker='o', color='red')
plt.plot(results_df["season"], [0.25]*len(results_df["season"]), label="Coinflip Model", marker='o',color='purple')

plt.xticks(ticks=range(len(results_df["season"])), labels=results_df["season"], rotation=45)

plt.xlabel("Season")
plt.ylabel("Score")
plt.title("Brier Scores of Different Models by Season")
plt.legend()
plt.grid(True)

plt.savefig("figures/brier_score_by_model.png")