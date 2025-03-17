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

### src/scraping/firefox_automated_scraper.py
- Alternate option to automated_scraper.py that uses FireFox instead of Google Chrome. 

### src/scraping/run_automated_scraper.py
- Runs the automated_scraper.py file chunk by chunk to reduce memory allocation
