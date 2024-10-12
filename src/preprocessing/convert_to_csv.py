import pandas as pd


# define league and file and retrieve file
leagues = ["nfl", "mlb", "nhl", "nba"]
files = ["games", "market"]

for league in leagues:
    for file in files:

        df = pd.read_json(f'data/{league}/_combined/combined_{file}.json')


        # convert to csv
        df.to_csv(f'data/{league}/_combined/combined_{file}.csv', index=False)