import numpy as np
import pandas as pd
from sklearn.metrics import log_loss

output_file = "results/fivethirtyeight_elo/fivethirtyeight_elo_half_full_log_loss.csv"

results = []

file = 'processed_data/combined/nfl_espn_combined_with_elo.csv'

df = pd.read_csv(file)
df["date"] = pd.to_datetime(df["date"])

df = df[["elo_prob_1", "result", "tournament", "date"]].dropna()

try:
    log_loss_overall = log_loss(df["result"], df["elo_prob_1"])
except ValueError:
    log_loss_overall = None

results.append(["nfl_full_fivethirtyeight_elo", log_loss_overall])

season_game_counts = df.groupby("tournament").size()
df = df.sort_values(by=["tournament", "date"])
df["games_before"] = df.groupby("tournament")["date"].rank(method="first") - 1

df_late_season = df[df.apply(lambda row: row["games_before"] > season_game_counts[row["tournament"]] / 2, axis=1)]

try:
    log_loss_late = log_loss(df_late_season["result"], df_late_season["elo_prob_1"])
except ValueError:
    log_loss_late = None

results.append(["nfl_half_fivethirtyeight_elo", log_loss_late])

df_results = pd.DataFrame(results, columns=["Prediction_Method", "Log_Loss"])
df_results.to_csv(output_file, index=False)
