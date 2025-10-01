import pandas as pd
import matplotlib.pyplot as plt

methods = ["bradley_terry", "moneyline"]

for method in methods:
    df = pd.read_csv(f"results/{method}_roi/total_roi.csv")

    ax = df.plot(x="league", y=["favorite_roi", "underdog_roi"], kind="bar", figsize=(8,5))
    plt.axhline(0, color="black", linewidth=0.8, linestyle="--")
    plt.ylabel("ROI")
    plt.title(f"Favorite vs Underdog ROI by League ({method})")
    plt.xticks(rotation=0)
    plt.savefig(f"figures/{method}_roi/total_roi.png")