import pandas as pd
import numpy as np

leagues = ["nfl", "nba", "nhl", "mlb"]

for league in leagues:
    if league == "NFL":
        df = pd.read_csv("processed_data/combined/nfl_espn_combined_with_elo.csv")

        df = df.dropna(subset=["result", "tournament", "avg_prob_1", "elo_prob_1"])

        df["elo_prob_1"] = df["elo_prob_1"].astype(float)

    else:
        df = pd.read_csv(f'processed_data/combined/{league}_espn_combined.csv')

        df = df.dropna(subset=["result", "tournament", "avg_prob_1"])

    df["result"] = df["result"].astype(int)
    df["avg_prob_1"] = df["avg_prob_1"].astype(float)

    baseline_prob = df["result"].mean()

    results = []

    grouped = df.groupby("tournament")
    for season, group in grouped:
        avg_brier_score = np.mean((group["avg_prob_1"] - group["result"]) ** 2)

        if league == "NFL":
            elo_brier_score = np.mean((group["elo_prob_1"] - group["result"]) ** 2)

        baseline_brier_score = np.mean((baseline_prob - group["result"]) ** 2)
        
        if league == "NFL":
            results.append({
                "season": season,
                "moneyline_brier_score": avg_brier_score,
                "baseline_brier_score": baseline_brier_score,
                "elo_brier_score": elo_brier_score,
            })
        else:
            results.append({
                "season": season,
                "moneyline_brier_score": avg_brier_score,
                "baseline_brier_score": baseline_brier_score
            })

    results_df = pd.DataFrame(results)

    results_df.to_csv(f'results/moneyline/modelwise/{league}_modelwise.csv', index=False)


