# Processed Data Documentation

## Contains final, clean, and processed version of data used for analysis

### processed_data/mlb_espn_combined.csv   ,   processed_data/nba_espn_combined.csv   ,   processed_data/nhl_espn_combined.csv
- Final version of combined OddsPortal market data, now combined with ESPN ids
- Fields
    - date : "dd-mm-yyyy" of the game
    - team_1 : home team (if applicable)
    - team_2 : away_team (if applicable)
    - score_1 : team_1 score
    - score_2 : team_2 score
    - result : 1 if team_1 won and 0 if team_1 lost
    - tournament : the league/tournament/competition (e.g NBA_2009/2009, NHL_2016/2017) 
    - game_url : individual OddsPortal url for that specific game
    - avg_moneyline_1 : average moneyline across all bookmakers for team_1
    - avg_moneyline_2 : average moneyline across all bookmakers for team_2
    - avg_prob_1 : the predicted probability that team_1 wins, derived from moneylines
    - game_url : OddsPortal url of specific game
    - espn_id : unique game id that ESPN uses for game's webpage
    - game_type : type of game (e.g postseason, regular_season)

### processed_data/nfl_espn_combined_with_elo.csv
- Final version of combined OddsPortal market data for NFL games with both ESPN ids and elo based probabilities
- NFL was the only league that had FiveThirtyEight elo scores, but last available data was for 2020-2021 season
- Fields
    - date : "dd-mm-yyyy" of the game
    - team_1 : home team (if applicable)
    - team_2 : away_team (if applicable)
    - score_1 : team_1 score
    - score_2 : team_2 score
    - result : 1 if team_1 won and 0 if team_1 lost
    - tournament : the league/tournament/competition (e.g NBA_2009/2009, NHL_2016/2017) 
    - game_url : individual OddsPortal url for that specific game
    - avg_moneyline_1 : average moneyline across all bookmakers for team_1
    - avg_moneyline_2 : average moneyline across all bookmakers for team_2
    - avg_prob_1 : the predicted probability that team_1 wins, derived from moneylines
    - game_url : OddsPortal url of specific game
    - espn_id : unique game id that ESPN uses for game's webpage
    - game_type : type of game (e.g postseason, regular_season)
    - elo_prob_1 : the predicted probability that team_1 wins, derived from elo scores; None if elo didn't exist for the game