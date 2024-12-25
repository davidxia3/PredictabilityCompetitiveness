import pandas as pd
import matplotlib.pyplot as plt

file_paths = ["results/mlb_seasonal.csv", "results/nhl_seasonal.csv", "results/nfl_seasonal.csv", "results/nba_seasonal.csv"]
leagues = ['MLB', 'NHL', 'NFL', 'NBA']
colors = ['blue', 'orange', 'red', 'purple']

plt.figure(figsize=(10, 6))

all_years = [str(year) for year in range(2009,2022)]
for i, file_path in enumerate(file_paths):
    df = pd.read_csv(file_path)
    df = df.sort_values(by="season")

    season_years = df["season"].str.split("_").str[1]
    
    df_filtered = df[season_years.isin(all_years)]

    plt.plot(season_years[season_years.isin(all_years)],
             df_filtered['brier_score'], color=colors[i], label=leagues[i], marker='o', linewidth=3, markersize=10)


all_years = sorted(all_years)
plt.xticks(ticks=range(len(all_years)), labels=all_years, rotation=0)

plt.ylim(0.15, 0.26)

plt.xlabel("Season",fontsize=20)
plt.ylabel("Brier Score",fontsize=20)
plt.legend(fontsize=15)
plt.text(-1.7, 0.245, "Less Accurate", fontsize=12, ha='center', va='center',rotation=90)
plt.text(-1.7, 0.165, "More Accurate", fontsize=12, ha='center', va='center', rotation=90)
plt.grid(True)
plt.tick_params(axis='both', which='major', labelsize=15)

plt.tight_layout()

plt.savefig('figures/league_seasonal.png', dpi=300, bbox_inches='tight')

