import pandas as pd
import matplotlib.pyplot as plt

file_path = "results/nfl_brier_log_auc.csv"
df = pd.read_csv(file_path)

df['year'] = df['season'].str.extract(r'NFL_(\d+)').astype(int)

x = df['year']
y1 = df['brier_score']
y2 = df['auc']

fig, ax1 = plt.subplots(figsize=(12, 6))

ax1.plot(x, y1, 'r-', label="Brier Score", marker='o', linewidth=3, markersize=10)
ax1.set_ylabel("Brier Score", color="red", size=20)
ax1.tick_params(axis='y', labelcolor="red", labelsize=15)
ax1.set_xlabel("Season", size=20)

ax1.set_xticks(x) 
ax1.tick_params(axis='x', labelsize=15,rotation=45)

ax2 = ax1.twinx()
ax2.plot(x, 1-y2, 'g-', label="AUC", marker='o', linewidth=3, markersize=10)
ax2.set_ylabel("AUC", color="green", size=20)
ax2.tick_params(axis='y', labelcolor="green", labelsize=15)

fig.legend(
    loc="upper left", bbox_to_anchor=(0.1, 0.9),
    labels=["Brier Score", "AUC"],
    fontsize=15
)

plt.text(2006.7, 0.32, "More Accurate", fontsize=12, ha='center', va='center',rotation=90,color="red")
plt.text(2006.7, 0.25, "Less Accurate", fontsize=12, ha='center', va='center', rotation=90,color="red")

plt.text(2026.1, 0.32, "More Accurate", fontsize=12, ha='center', va='center',rotation=90,color="green")
plt.text(2026.1, 0.25, "Less Accurate", fontsize=12, ha='center', va='center', rotation=90,color="green")

plt.tight_layout()
plt.savefig("figures/nfl_brier_auc.png", dpi=300, bbox_inches='tight')
