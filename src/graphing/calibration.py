import pandas as pd
import matplotlib.pyplot as plt
from sklearn.calibration import calibration_curve


leagues = ["nfl", "nba", "mlb", "nhl"]


for league in leagues:
    file_path = f'processed_data/combined/{league}_espn_combined.csv'
    if league == "nfl":
        file_path = 'processed_data/combined/nfl_espn_combined_with_elo.csv'

        df = pd.read_csv(file_path)

        df = df[df[['avg_prob_1', 'elo_prob_1']].notnull().all(axis=1)]

        c1 = df["avg_prob_1"]
        c2 = df["elo_prob_1"]
        actual_results = df["result"]

        prob_true1, prob_pred1 = calibration_curve(actual_results, c1, n_bins=10, strategy='uniform')
        prob_true2, prob_pred2 = calibration_curve(actual_results, c2, n_bins=10, strategy='uniform')

        plt.figure(figsize=(10, 6))

        plt.plot(prob_pred1, prob_true1, marker='o', label='Betting Market Model', color='green',linewidth=3, markersize=10)
        plt.plot(prob_pred2, prob_true2, marker='o', label='Elo Model', color='magenta',linewidth=3, markersize=10)
        plt.plot([0, 1], [0, 1], linestyle='--', color='gray', label='Perfect Calibration',linewidth=3, markersize=10)

        plt.xlim(0, 1)
        plt.ylim(0, 1)
        plt.xlabel('Predicted Win Probability', fontsize=20)
        plt.ylabel('Actual Win Frequency', fontsize=20)
        plt.legend(fontsize=15)
        plt.grid(True, linestyle='--', alpha=0.6)
        plt.tick_params(axis='both', which='major', labelsize=15)

        plt.tight_layout()
        plt.savefig("figures/nfl_calibration_plot.png", dpi=300, bbox_inches='tight')
        plt.close()

    else:
        df = pd.read_csv(file_path)

        df = df[df[['avg_prob_1']].notnull().all(axis=1)]

        c1 = df["avg_prob_1"]
        actual_results = df["result"]

        prob_true1, prob_pred1 = calibration_curve(actual_results, c1, n_bins=10, strategy='uniform')

        plt.figure(figsize=(10, 6))

        plt.plot(prob_pred1, prob_true1, marker='o', label='Betting Market Model', color='green',linewidth=3, markersize=10)
        plt.plot([0, 1], [0, 1], linestyle='--', color='gray', label='Perfect Calibration',linewidth=3, markersize=10)

        plt.xlim(0, 1)
        plt.ylim(0, 1)
        plt.xlabel('Predicted Win Probability', fontsize=20)
        plt.ylabel('Actual Win Frequency', fontsize=20)
        plt.legend(fontsize=15)
        plt.grid(True, linestyle='--', alpha=0.6)
        plt.tick_params(axis='both', which='major', labelsize=15)

        plt.tight_layout()
        plt.savefig(f'figures/calibration/{league}_calibration.png', dpi=300, bbox_inches='tight')
        plt.close()
        
