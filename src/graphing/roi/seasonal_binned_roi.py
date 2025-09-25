import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

leagues = ["nfl", "nhl", "mlb", "nba"]

for league in leagues:

    df = pd.read_csv(f"results/roi/{league}_seasonal_binned_roi.csv")

    df = df.replace(-2.0, np.nan)

    plt.figure(figsize=(9,6))

    for season, group in df.groupby("season"):
        plt.plot(group["bin"], group["favorite_roi"], marker="o", label=f"{season} Favorite")
        plt.plot(group["bin"], group["underdog_roi"], marker="x", label=f"{season} Underdog")

    plt.axhline(0, color="black", linestyle="--", linewidth=0.8)
    plt.xlabel("Probability Bin")
    plt.ylabel("ROI")
    plt.title("Favorite vs Underdog ROI by Bin and Season")
    plt.legend()
    plt.savefig(f"figures/roi/{league}_seasonal_binned_roi.png")