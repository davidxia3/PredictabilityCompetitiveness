import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.calibration import calibration_curve

league = 'nfl'

df = pd.read_csv(f'processed_data/{league}_espn_combined.csv')

predicted_probs = df['avg_prob_1']
true_results = df['result']

fraction_of_positives, mean_predicted_probabilities = calibration_curve(
    true_results, predicted_probs, n_bins=10, strategy='quantile'
)

plt.plot(mean_predicted_probabilities, fraction_of_positives, 's-', label="calibration curve")
plt.plot([0, 1], [0, 1], 'k--', label="perfect calibration")
plt.savefig(f'results/{league}_calibration.png')
