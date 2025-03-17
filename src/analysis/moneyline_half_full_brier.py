import numpy as np
import pandas as pd

leagues = ["nhl", "mlb", "nfl", "nba"]
output_file = "results/moneyline/half_full_brier.csv"

results = []

for league in leagues:
    file = f'processed_data/combined/{league}_espn_combined.csv'
    if league == "nfl":
        file = 'processed_data/combined/nfl_espn_combined_with_elo.csv'

    df = pd.read_csv(file)
    df["date"] = pd.to_datetime(df["date"])

    brier_score_overall = np.mean((df["avg_prob_1"] - df["result"])**2)
    results.append([f"{league}_full_ml", brier_score_overall])

    season_game_counts = df.groupby("tournament").size()
    df = df.sort_values(by=["tournament", "date"])

    df["games_before"] = df.groupby("tournament")["date"].rank(method="first") - 1

    df_late_season = df[df.apply(lambda row: row["games_before"] > season_game_counts[row["tournament"]] / 2, axis=1)]
    brier_score_late = np.mean((df_late_season["avg_prob_1"] - df_late_season["result"])**2)
    results.append([f"{league}_half_ml", brier_score_late])

df_results = pd.DataFrame(results, columns=["Prediction_Method", "Brier_Score"])
df_results.to_csv(output_file, index=False)

