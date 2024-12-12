import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# List of league CSV file paths
leagues = [
    'processed_data/mlb_espn_combined.csv', 
    'processed_data/nba_espn_combined.csv', 
    'processed_data/nhl_espn_combined.csv', 
    'processed_data/nfl_espn_combined_with_elo.csv'
]

# To store the data for plotting
data = []
league_names = []

# Read each file and collect 'avg_prob_1' data
for league in leagues:
    print(league)
    df = pd.read_csv(league)
    league_names.append(league.split('/')[-1].split('_')[0].upper())
    data.append(df['avg_prob_1']) 
    
    mean = np.mean(df['avg_prob_1'])
    std = np.std(df['avg_prob_1'])
    print(f"League: {league}, Mean: {mean:.4f}, Std: {std:.4f}")


plt.hist(df['elo_prob_1'],bins=100)
plt.show()

# plt.figure(figsize=(10, 6))
# plt.boxplot(data, labels=league_names, patch_artist=True, boxprops=dict(facecolor="skyblue"))
# plt.title("Box-and-Whisker Plot of avg_prob_1 for Different Leagues")
# plt.xlabel("Leagues")
# plt.ylabel("avg_prob_1")
# plt.grid(axis='y', linestyle='--', alpha=0.7)
# plt.show()
