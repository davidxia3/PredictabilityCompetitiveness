import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df1 = pd.read_csv('results/combined_half_full_brier.csv')
df2 = pd.read_csv('results/combined_half_full_log_loss.csv')

merged = pd.merge(df1, df2, on='Prediction_Method')

data1 = merged['Brier_Score'] / merged['Brier_Score'].max()
data2 = merged['Log_Loss'] / merged['Log_Loss'].max()
labels = merged['Prediction_Method']

x = np.arange(len(labels))
width = 0.35

fig, ax = plt.subplots(figsize=(10, 6))
bars1 = ax.bar(x - width/2, data1, width, label='Brier Score (scaled)')
bars2 = ax.bar(x + width/2, data2, width, label='Log Loss (scaled)')

ax.set_xlabel('Prediction Method')
ax.set_ylabel('Normalized Loss (max=1)')
ax.set_title('Normalized Brier Score vs Log Loss')
ax.set_xticks(x)
ax.set_xticklabels(labels, rotation=45, ha='right')
ax.legend()

plt.tight_layout()
plt.savefig("figures/brier_vs_log_loss.png")
