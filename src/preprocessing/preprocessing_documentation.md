# Preprocessing Documentation

## Contains all the scripts to process raw data into clean, processed data

### src/preprocessing/combined_preprocessing.py
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
- It then adds this additional information to the csv and saves it to processed_data/{league}_espn_combined.csv
- These are the files used for analysis