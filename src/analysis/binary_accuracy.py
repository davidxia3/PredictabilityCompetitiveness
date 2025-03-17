import pandas as pd

accuracies = []
files = [
    "processed_data/combined/mlb_espn_combined.csv",
    "processed_data/combined/nba_espn_combined.csv",
    "processed_data/combined/nhl_espn_combined.csv",
    "processed_data/combined/nfl_espn_combined_with_elo.csv"
]

for file in files:
    df = pd.read_csv(file)
    df['predicted'] = (df['avg_prob_1'] >= 0.5).astype(int)
    accuracy = (df['predicted'] == df['result']).mean()
    accuracies.append(accuracy)

df = pd.read_csv("processed_data/nfl_espn_combined_with_elo.csv")
df['predicted'] = (df['elo_prob_1'] >= 0.5).astype(int)
accuracy = (df['predicted'] == df['result']).mean()
accuracies.append(accuracy)

labels = ["MLB_ML", "NBA_ML", "NHL_ML", "NFL_ML", "NFL_ELO"]

output_df = pd.DataFrame({'label': labels, 'accuracy': accuracies})
output_df.to_csv("results/binary_accuracy.csv", index=False)

