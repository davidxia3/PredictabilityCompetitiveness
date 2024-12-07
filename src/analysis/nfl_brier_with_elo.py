import pandas as pd
import numpy as np

df = pd.read_csv("processed_data/nfl_espn_combined_with_elo.csv")

df = df.dropna(subset=["result", "tournament", "avg_prob_1", "elo_prob_1"])

df["result"] = df["result"].astype(int)
df["avg_prob_1"] = df["avg_prob_1"].astype(float)
df["elo_prob_1"] = df["elo_prob_1"].astype(float)

baseline_prob = df["result"].mean()

results = []

grouped = df.groupby("tournament")
for season, group in grouped:
    avg_brier_score = np.mean((group["avg_prob_1"] - group["result"]) ** 2)
    
    elo_brier_score = np.mean((group["elo_prob_1"] - group["result"]) ** 2)

    baseline_brier_score = np.mean((baseline_prob - group["result"]) ** 2)
    
    results.append({
        "season": season,
        "moneyline_brier_score": avg_brier_score,
        "baseline_brier_score": baseline_brier_score,
        "elo_brier_score": elo_brier_score,
    })

results_df = pd.DataFrame(results)

results_df.to_csv("results/nfl_by_model.csv", index=False)


