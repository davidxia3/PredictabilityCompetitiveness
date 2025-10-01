# Preprocessing Documentation

## Contains all the scripts to process raw data into clean, processed data

### src/preprocessing/combined_processing.py
- Combines each team's market csvs into a combined market csv at raw_data/combined/{league}_market.csv
- Filters out duplicate games and other miscellaneous games (e.g friendly games, ongoing season games)
- Computes the win probability derived from moneylines
- avg_prob_1 : the probability that team_1 wins according the average moneylines and is calculated as:
    - First, need normalized moneylines, M1* and M2*
        - The normalized value of the larger absolute value moneyline is calculated as M* = M/(M+100)
        - The normalized value of the smaller absolute value moneyline is calculated as M* = 100/(M+100)
    - The predicted probability of team 1 winning is M1*/(M1* + M2*)

### src/preprocessing/espn_processing.py
- Uses the combined market csv and the collection of json dictionaries in raw_data/espn_mapping/ to map each game with its corresponding ESPN id and game type
- It then adds this additional information to the csv and saves it to processed_data/{league}_espn_combined.cs
- These are the files used for analysis

### src/preprocessing/elo_combining.py
- Uses the raw_data/fivethirtyeight_mapping.json file to map games in raw_data/fivethirtyeight_nfl_elo.csv and games in nfl_espn_combined.csv
- This adds the elo data to all available games and saves it to the final version, processed_data/nfl_espn_combined_with_elo.csv

### src/preprocesing/elo_mapping.py
- Creates the JSON dictionary raw_data/fivethirtyeight_mapping.json file that contains keys that include information about the date of the game and the teams
- The values are the respective elo based probabilistic predictions for each game

### src/preprocessing/ratingslibformatter.py
- Converts output of combined processing to a format that is easier for the RatingsLib package to use

### src/preprocessing/second_half_season_filter.py
- Creates a filtered version of prediction csv files that contain only games from the second half of every season
