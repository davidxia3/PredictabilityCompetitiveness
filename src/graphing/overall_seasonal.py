import pandas as pd
import matplotlib.pyplot as plt

file_paths = ["results/mlb_seasonal.csv", "results/nba_seasonal.csv", "results/nhl_seasonal.csv", "results/nfl_seasonal.csv"]
leagues = ['MLB', 'NBA', 'NHL', 'NFL']
colors = ['blue', 'green', 'red', 'purple']

plt.figure(figsize=(10, 6))

for i, file_path in enumerate(file_paths):
    df = pd.read_csv(file_path)
    
    df['year'] = df['season'].str.extract(r'_(\d{4})').astype(int)
    
    plt.plot(df['year'], df['brier_score'], color=colors[i], label=leagues[i])

plt.xlabel("Year")
plt.ylabel("Brier Score")
plt.title("Seasonal Brier Scores by League")
plt.legend()
plt.grid(True)

plt.savefig('figures/league_seasonal.png')

