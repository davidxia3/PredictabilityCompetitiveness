# Scraping Documentation

## Contains all scripts to scrape data from webpages

### src/scraping/game_scraper.py
- Scrapes game data from the OddsPortal.com archived results webpage
- Scrapes by team, and saves each individual team's games to raw_data/{league}/{team}/games.csv
- Includes team_1, team_2, score_1, score_2, game_url
    - team_1 : home team (if applicable)
    - team_2 : away team (if applicable)
    - score_1 : team_1 score
    - score_2 : team_2 score
    - game_url : individual OddsPortal url for that specific game

### src/scraping/automated_scraper.py
- Opens each team's game csv at raw_data/{league}/{team}/games.csv
- Loops through each game and opens the game's webpage and scrapes the average and high moneylines for each team
- Saves the file with additional information at raw_data/{league}/{team}/market.csv
- Includes date, team_1, team_2, score_1, score_2, result, tournament, game_url, avg_moneyline_1, avg_moneyline_2, high_moneyline_1, high_moneyline_2
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
- There were a handful of games with no available betting data (~10 per team); these games weren't included in the saved file

### src/scraping/run_automated_scraper.py
- runs the automated_scraper.py file chunk by chunk to reduce memory allocation

### src/scraping/espn_id_scraping/
- Contains four scripts, one for each league, to scrape ESPN ids for each game
- The ESPN id is a string of 9 digits that defines the url for the ESPN webpage of that game
- Each script is slightly different because of each league's inherent differences (e.g start and end dates, 2020 season)
- All scripts loads each team's ESPN webpage and scrapes their schedule going back to the earliest season that is included in OddsPortal (2003-2004 for NHL, 2006 for MLB, 2008-2009 for NFL, 2008-2009 for NBA)
    - Seattle Kraken (NHL) only started in the 2021-2022 NHL season
    - Vegas Golden Knights (NHL) only started in the 2017-2018 NHL season
    - Arizona Coyotes moved and rebranded as the Utah Hockey Club, starting for the NHL 2023-2024 season
        - The last seasons that are included in this project are (NHL 2022-2023, NFL 2023-2024, NBA 2023-2024, MLB 2023)
        - For this project, we can pretend the Arizona Coyotes never rebranded, but ESPN no longer lists an individual webpage for the team
        - The team's past games can only be found through looking at other teams' schedules
        - This actually does not pose any issues, because each Arizona Coyotes game is also another NHL team's games, so can still be found in another team's webpage
- It creates a mapping for each team between the date of the game and the id of the game as well as the type of game (e.g postseason, regular_season)
- It saves the mapping to raw_data/espn_mapping/{league}/{team}.json