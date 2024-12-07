import pandas as pd
import matplotlib.pyplot as plt

file_paths = ["results/mlb_seasonal.csv", "results/nba_seasonal.csv", "results/nhl_seasonal.csv", "results/nfl_seasonal.csv"]
leagues = ['MLB', 'NBA', 'NHL', 'NFL']
colors = ['blue', 'green', 'red', 'purple']

plt.figure(figsize=(10, 6))

all_years = set()

for i, file_path in enumerate(file_paths):
    df = pd.read_csv(file_path)
    
    df['year'] = df['season'].str.extract(r'_(\d{4})').astype(int)
    
    df = df[(df['year'] >= 2009) & (df['year'] <= 2023)]
    
    all_years.update(df['year'])
    
    plt.plot(df['year'], df['brier_score'], color=colors[i], label=leagues[i], marker = 'o')

all_years = sorted(all_years)
plt.xticks(ticks=all_years, labels=[str(year) for year in all_years], rotation=45)

plt.ylim(0.15, 0.26)

plt.xlabel("Season")
plt.ylabel("Brier Score")
plt.title("Seasonal Brier Scores by League (2009–2023)")
plt.legend()
plt.grid(True)

plt.savefig('figures/league_seasonal.png')

