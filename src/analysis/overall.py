import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import brier_score_loss

files = [
    'processed_data/mlb_espn_combined.csv',
    'processed_data/nba_espn_combined.csv',
    'processed_data/nhl_espn_combined.csv',
    'processed_data/nfl_espn_combined_with_elo.csv'
]

leagues = ['MLB', 'NBA', 'NHL', 'NFL']

brier_scores = []

for file in files:
    df = pd.read_csv(file)
    
    true_labels = df['result']
    predictions = df['avg_prob_1']
    
    score = brier_score_loss(true_labels, predictions)
    
    brier_scores.append(score)

fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(range(len(files)), brier_scores, tick_label=leagues)

ax.set_xlabel("Leagues")
ax.set_ylabel("Brier Score")
ax.set_title("Brier Scores of Different Leagues")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

plt.savefig('figures/overall.png')
