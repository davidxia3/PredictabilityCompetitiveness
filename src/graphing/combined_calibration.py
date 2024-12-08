import pandas as pd
import matplotlib.pyplot as plt
from sklearn.calibration import calibration_curve

file_paths = [
    "processed_data/mlb_espn_combined.csv",
    "processed_data/nba_espn_combined.csv",
    "processed_data/nhl_espn_combined.csv",
    "processed_data/nfl_espn_combined_with_elo.csv"
]
leagues = ["MLB", "NBA", "NHL", "NFL"]

colors = ['red', 'green', 'blue', 'purple']

plt.figure(figsize=(10, 7))

for i, (file, league, color) in enumerate(zip(file_paths, leagues, colors), start=1):
    data = pd.read_csv(file)
    predicted_probs = data['avg_prob_1']
    actual_outcomes = data['result']
    
    prob_true, prob_pred = calibration_curve(actual_outcomes, predicted_probs, n_bins=10, strategy="quantile")
    
    plt.plot(
        prob_pred, prob_true,
        linestyle='-',
        marker='o',
        color=color,
        label=league,
        linewidth=3,
        markersize=12,
        alpha=0.8
    )

plt.plot([0, 1], [0, 1], 'k--', label='Perfectly calibrated', linewidth=1.5)

plt.title("Calibration Curves by League", fontsize=25)
plt.xlabel("Probabilistic Prediction", fontsize=20)
plt.ylabel("Observed Frequency", fontsize=20)
plt.legend(fontsize=20)
plt.grid(True, linestyle='--', alpha=0.6)
plt.tick_params(axis='both', which='major', labelsize=15)
plt.xlim(0.2,0.9)
plt.ylim(0.2,0.9)
plt.tight_layout()

plt.savefig("figures/calibration/combined_calibration.png", dpi=300, bbox_inches='tight')
