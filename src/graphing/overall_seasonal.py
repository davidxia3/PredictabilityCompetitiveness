import pandas as pd
import matplotlib.pyplot as plt

file_paths = ["results/mlb_seasonal.csv", "results/nba_seasonal.csv", "results/nhl_seasonal.csv", "results/nfl_seasonal.csv"]
leagues = ['MLB', 'NBA', 'NHL', 'NFL']
colors = ['blue', 'green', 'red', 'purple']

data = {}

for i, file_path in enumerate(file_paths):
    df = pd.read_csv(file_path)
    data[leagues[i]] = df["brier_score"]

plt.figure(figsize=(10, 6))
for i, (label, brier_scores) in enumerate(data.items()):
    plt.plot(brier_scores, color=colors[i], label=label)

plt.xlabel("Seasons")
plt.ylabel("Brier Score")
plt.title("Seasonal Brier Scores by League")
plt.legend()
plt.grid(True)
plt.savefig('figures/league_seasonal.png')
