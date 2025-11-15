import pandas as pd
import matplotlib.pyplot as plt


leagues = ["nfl", "nba", "nhl", "mlb"]

for league in leagues:
    file_path = f"processed_data/combined/{league}_espn_combined.csv"
    if league == "nfl":
        file_path = f"processed_data/combined/{league}_espn_combined_with_elo.csv"

    df = pd.read_csv(file_path)

    col = "bookmaker_profit"

    plt.hist(df[col].values, bins=50)
    plt.xlabel("Bookmaker Profit")
    plt.ylabel("Frequency")
    plt.title(f"{league.upper()} Bookmaker Profit")
    plt.savefig(f"figures/bookmaker_profit/{league}_bookmaker_profit.png")

    plt.close()

    print(f"--{league}--")
    print(f"mean: {df[col].mean()}")
    print(f"std: {df[col].std()}")
    print(f"median: {df[col].median()}")
    print("-----\n")
