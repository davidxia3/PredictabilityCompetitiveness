import pandas as pd
import math


leagues = ["nfl", "nhl", "mlb", "nba"]

for league in leagues:
    file_path = f"processed_data/combined/{league}_espn_combined.csv"
    if league == "nfl":
        file_path = f"processed_data/combined/{league}_espn_combined_with_elo.csv"

    df = pd.read_csv(file_path)

    df['raw_prob_1'] = (abs(df['avg_moneyline_1']) / (abs(df['avg_moneyline_1']) + 100))
    df['raw_prob_2'] = (abs(df['avg_moneyline_2']) / (abs(df['avg_moneyline_2']) + 100))
    

    df['raw_prob_1'] = df['raw_prob_1'].apply(lambda x: math.trunc(x * 10000) / 10000)
    df['raw_prob_2'] = df['raw_prob_2'].apply(lambda x: math.trunc(x * 10000) / 10000)
    df['bookmaker_profit'] = df['raw_prob_1'] + df['raw_prob_2'] - 1

    df['bookmaker_profit'] = df['bookmaker_profit'].apply(lambda x: f"{x:.4f}")

    df.to_csv(file_path, index=False)