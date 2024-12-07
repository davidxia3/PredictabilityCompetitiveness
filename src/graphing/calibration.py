import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.calibration import calibration_curve

leagues = ["nhl", "nba", "nfl", "mlb"]
formats = ["quantile", "uniform"]

for league in leagues:
    for format in formats:

        file = f'processed_data/{league}_espn_combined.csv'
        if league == "nfl":
            file = f'processed_data/{league}_espn_combined_with_elo.csv'

        df = pd.read_csv(file)

        predicted_probs = df['avg_prob_1']
        true_results = df['result']

        fraction_of_positives, mean_predicted_probabilities = calibration_curve(
            true_results, predicted_probs, n_bins=10, strategy=format
        )

        plt.plot(mean_predicted_probabilities, fraction_of_positives, 's-', label="calibration curve")
        plt.plot([0, 1], [0, 1], 'k--', label="perfect calibration")
        plt.xlabel("Probabilistic Prediction")
        plt.ylabel("Observed Frequency")
        plt.title(f'{league.upper()} Calibration Curve ({format})')
        plt.savefig(f'figures/calibration/{league}_calibration_{format}.png')
        plt.clf()
