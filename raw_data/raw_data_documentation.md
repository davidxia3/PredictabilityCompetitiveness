# Raw Data Documentation

## Contains all the raw data and intermediate steps in producing the processed data

### raw_data/abbreviations.json
- A json map
- Keys are full names of all NFL, NHL, NBA, and MLB teams
- Values are 2-3 three letter abbreviation team codes for each team
- Abbreviated codes are unique in each league

### raw_data/teams.json
- Lists of NFL, NHL, NBA, and MLB teams for easy access

### raw_data/mlb/   ,   raw_data/nba/   ,   raw_data/nfl/   ,   raw_data/nhl/
- Contains the game and market data for each team in each league
- Data scraped from OddsPortal.com  

### raw_data/fivethirtyeight_mapping.json
- Dictionary that maps FiveThirtyEight NFL games with elo ratings to NFL games with moneyline ratings

### raw_data/five_thirty_eight_nfl_elo.csv
- Preexisting data, downloaded from FiveThirtyEight GitHub repository
- Fields
    - date : "dd-mm-yyyy" of the game
    - season : NFL season (e.g 2015 is 2015-2016)
    - neutral : 1 if neutral game, 0 if not
    - playoff : 1 if postseason, 0 if not
    - team1 : home team (if applicable)
    - team2 : away team (if applicable)
    - elo1 : team1 elo, going into the game
    - elo2 : team2 elo, going into the game
    - elo_prob1 : probability that team1 wins derived from elo1 and elo2 (elo_prob1 = elo1/(elo1 + elo2))
    - score1 : team1 score
    - score2 : team2 score
    - result1 : 1 if team 1 won, 0 if team 1 lost

### raw_data/nfl_espn_combined.csv
- Penultimate version of combined OddsPortal market data, now combined with ESPN ids
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