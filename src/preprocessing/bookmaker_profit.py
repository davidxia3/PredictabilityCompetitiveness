import pandas as pd
import math


leagues = ["nfl", "nhl", "mlb", "nba"]

for league in leagues:
    file_path = f"processed_data/combined/{league}_espn_combined.csv"
    if league == "nfl":
        file_path = f"processed_data/combined/{league}_espn_combined_with_elo.csv"

    df = pd.read_csv(file_path)

    for idx, row in df.iterrows():
        team_1_prob = row["avg_prob_1"]
        
        ml1 = row["avg_moneyline_1"]
        ml2 = row["avg_moneyline_2"]

        if team_1_prob >= 0.5:
            # team 1 is favorite
            df.loc[idx, "raw_prob_1"] = abs(ml1) / (abs(ml1) + 100)
            df.loc[idx, "raw_prob_2"] = 100 / (abs(ml2) + 100)
        else:
            # team 2 is favorite
            df.loc[idx, "raw_prob_1"] = 100 / (abs(ml1) + 100)
            df.loc[idx, "raw_prob_2"] = abs(ml2) / (abs(ml2) + 100)

    df['raw_prob_1'] = df['raw_prob_1'].apply(lambda x: math.trunc(x * 10000) / 10000)
    df['raw_prob_2'] = df['raw_prob_2'].apply(lambda x: math.trunc(x * 10000) / 10000)
    df['bookmaker_profit'] = df['raw_prob_1'] + df['raw_prob_2'] - 1

    df['bookmaker_profit'] = df['bookmaker_profit'].apply(lambda x: f"{x:.4f}")

    df.to_csv(file_path, index=False)