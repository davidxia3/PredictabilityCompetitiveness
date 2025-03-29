import pandas as pd


leagues = ['nfl', 'nba', 'mlb', 'nhl']

for league in leagues:
    suffix = ""
    if league == "nfl":
        suffix = '_with_elo'
    ml_df = pd.read_csv(f'processed_data/combined/{league}_espn_combined{suffix}.csv')
    bt_df = pd.read_csv(f'results/bradley_terry/{league}_bradley_terry_predictions.csv')
    rl_df = pd.read_csv(f'results/ratingslib/{league}_ratingslib_predictions.csv')

    ml_df = ml_df.sort_values(by=["tournament", "date"])
    ml_filtered_df = pd.DataFrame()

    for season, season_df in ml_df.groupby("tournament"):
        num_games_in_season = len(season_df)
        cutoff = num_games_in_season // 2
        filtered_season_df = season_df.iloc[cutoff:]
        ml_filtered_df = pd.concat([ml_filtered_df, filtered_season_df])

    ml_filtered_df.to_csv(f'processed_data/combined/{league}_half_espn_combined{suffix}.csv', index=False)

    bt_df = bt_df.sort_values(by=["Season", "Date"])
    bt_filtered_df = pd.DataFrame()

    for season, season_df in bt_df.groupby("Season"):
        num_games_in_season = len(season_df)
        cutoff = num_games_in_season // 2
        filtered_season_df = season_df.iloc[cutoff:]
        bt_filtered_df = pd.concat([bt_filtered_df, filtered_season_df])

    bt_filtered_df.to_csv(f'results/bradley_terry/{league}_half_bradley_terry_predictions.csv', index=False)

    rl_df = rl_df.sort_values(by=["Season", "Date"])
    rl_filtered_df = pd.DataFrame()

    for season, season_df in rl_df.groupby("Season"):
        num_games_in_season = len(season_df)
        cutoff = num_games_in_season // 2
        filtered_season_df = season_df.iloc[cutoff:]
        rl_filtered_df = pd.concat([rl_filtered_df, filtered_season_df])

    rl_filtered_df.to_csv(f'results/ratingslib/{league}_half_ratingslib_predictions.csv', index=False)

