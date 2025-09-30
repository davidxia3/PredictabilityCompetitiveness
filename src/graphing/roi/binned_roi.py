import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

leagues = ["mlb", "nfl", "nba", "nhl"]
methods = ["bradley_terry", "moneyline"]

for league in leagues:
    for method in methods:

        df = pd.read_csv(f"results/{method}_roi/{league}_binned_roi.csv")
        df = df.replace(-2.0, np.nan)

        plt.figure(figsize=(9,5))
        plt.plot(df["bin"], df["favorite_roi"], marker="o", label="Favorite ROI")
        plt.plot(df["bin"], df["underdog_roi"], marker="o", label="Underdog ROI")



        for i, n in enumerate(df["n"]):
            if not np.isnan(df["favorite_roi"][i]):
                plt.text(df["bin"][i], df["favorite_roi"][i]+0.005, f"n={n}", ha="center", fontsize=8)

        plt.axhline(0, color="black", linewidth=0.8, linestyle="--")
        plt.xlabel("Probability Bin")
        plt.ylabel("ROI")
        plt.title(f"Favorite vs Underdog ROI by Probability Bin ({method})")
        plt.legend()
        plt.savefig(f"figures/{method}_roi/{league}_binned_roi.png")

