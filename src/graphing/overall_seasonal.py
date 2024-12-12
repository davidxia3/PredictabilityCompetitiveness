import pandas as pd
import matplotlib.pyplot as plt

file_paths = ["results/mlb_seasonal.csv", "results/nhl_seasonal.csv", "results/nfl_seasonal.csv", "results/nba_seasonal.csv"]
leagues = ['MLB', 'NHL', 'NFL', 'NBA']
colors = ['blue', 'orange', 'red', 'purple']

plt.figure(figsize=(10, 6))

all_years = set()

for i, file_path in enumerate(file_paths):
    df = pd.read_csv(file_path)
    
    df['year'] = df['season'].str.extract(r'_(\d{4})').astype(int)
    
    df = df[(df['year'] >= 2009) & (df['year'] <= 2021)]
    
    all_years.update(df['year'])
    
    plt.plot(df['year'], df['brier_score'], color=colors[i], label=leagues[i], marker = 'o', linewidth=3,markersize=10)

all_years = sorted(all_years)
plt.xticks(ticks=all_years, labels=[str(year) for year in all_years], rotation=45)

plt.ylim(0.15, 0.26)

plt.xlabel("Season",fontsize=20)
plt.ylabel("Brier Score",fontsize=20)
plt.legend(fontsize=15)
plt.grid(True)
plt.tick_params(axis='both', which='major', labelsize=15)

plt.tight_layout()

plt.savefig('figures/league_seasonal.png', dpi=300, bbox_inches='tight')

