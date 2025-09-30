import pandas as pd

leagues = ["mlb", "nfl", "nba", "nhl"]


for league in leagues:
    df = pd.read_csv(f"results/bradley_terry/{league}_bradley_terry_predictions.csv")

    nan_cols = df.columns[df.isna().any()].tolist()
    print("Columns with NaNs:", nan_cols)
