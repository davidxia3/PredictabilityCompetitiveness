# Processed Data Documentation

## Contains final, clean, and processed version of data used for analysis

### processed_data/combined/
- Final version of combined OddsPortal market data for NFL games with both ESPN ids (and elo based probabilities for NFL only)
- NFL was the only league that had FiveThirtyEight elo scores, but last available data was for 2020-2021 season
- Fields
    - date : "dd-mm-yyyy" formatted date of the game
    - team_1 : home team (if applicable)
    - team_2 : away team (if applicable)
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
    - elo_prob_1 (NFL ONLY): the predicted probability that team_1 wins, derived from elo scores; None if elo didn't exist for the game
- Also contains parallel version of each file with only second half of season games


### processed_data/ratingslib_formatted/
- Contains the four final version of match results in the four leagues
- Specifically formatted for compatiabilty with RatingsLib package
- Fields
    - Date : "dd/mm/yyyy" formatted date of the game
    - HomeTeam : home team (if applicable)
    - AwayTeam : away team (if applicable)
    - FTHG : HomeTeam score
    - FTAG : AwayTeam score
    - Season : season of game