import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("results/roi/total_roi.csv")

ax = df.plot(x="league", y=["favorite_roi", "underdog_roi"], kind="bar", figsize=(8,5))
plt.axhline(0, color="black", linewidth=0.8, linestyle="--")
plt.ylabel("ROI")
plt.title("Favorite vs Underdog ROI by League")
plt.xticks(rotation=0)
plt.savefig("figures/roi/total_roi.png")