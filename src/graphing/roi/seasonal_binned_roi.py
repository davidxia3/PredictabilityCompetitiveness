import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

leagues = ["nfl", "nhl", "mlb", "nba"]

for league in leagues:
    df = pd.read_csv(f"results/roi/{league}_seasonal_binned_roi.csv")

    df_clean = df[(df['favorite_roi'] > -2) & (df['underdog_roi'] > -2)]
    df_clean['season_year'] = df_clean['season'].str.extract(r'(\d+)').astype(int)

    min_year, max_year = df_clean['season_year'].min(), df_clean['season_year'].max()

    for b in sorted(df_clean['bin'].unique()):
        df_bin = df_clean[df_clean['bin'] == b]

        df_bin = df_bin[df_bin['n'] > 0]
        all_years_bin = sorted(df_bin['season_year'].unique())

        df_melted = df_bin.melt(
            id_vars=['season_year', 'n'],
            value_vars=['favorite_roi', 'underdog_roi'],
            var_name='bet_type',
            value_name='roi'
        )

        plt.figure(figsize=(8, 5))
        ax = sns.lineplot(
            data=df_melted,
            x='season_year',
            y='roi',
            hue='bet_type',
            marker='o'
        )

        for _, row in df_melted.iterrows():
            ax.text(
                row['season_year'],
                row['roi'],
                f"{int(row['n'])}",
                fontsize=8,
                ha='center',
                va='bottom'
            )

        plt.title(f'{league.upper()} ROI by Season (Bin {b})')
        plt.ylabel('ROI')
        plt.xlabel('Season')
        plt.axhline(0, color='black', linewidth=1)

        plt.xlim(min_year, max_year)
        plt.xticks(all_years_bin)

        plt.legend(title='Bet Type')
        plt.tight_layout()
        plt.savefig(f"figures/roi/{league}_bin{b}_seasonal_roi.png")
        plt.close()
