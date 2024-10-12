# Predictability and Competitiveness of Major American Sports Leagues
### David Xia

## In this project, we look into the betting market predictability of the four major American sports leagues (MLB, NFL, NBA, NHL)

## Scraping

### game_scraper.py
Archived historical data was scraped from [OddsPortal.com's Historical Sports Betting Odds webpage](https://www.oddsportal.com/results/#football). Historical data is displayed as a list of games, ranging from the current season back to the 2008-2009 seasons. The game_scraper.py script scrapes these initial games and their corresponding game_url. game_url is a unique url for each game and is only available from scraping. Games and their respective game_url are stored in each team's respective games.json file. Here is a breakdown of each field in all the games.json files. Each field is well-defined for every game.
- "date" : the date and month the game is played
- "team_1" : home team, (if neutral game, then one of the teams)
- "score_1" : team_1 score
- "score_2" : team_2 score
- "team_2" : away team, (if netural game, then the other team)
- "game_url" : unique game url


### automated_scraper.py and run_automated_scraper.py
The automated_scraper uses the game_url of each game to access the individual webpage of each game to scrape betting data. The four key betting lines that are scraped for each game are the average_moneyline_1, average_money_line_2, high_moneyline_1, high_moneyline_2. The average moneylines is the average of all the different bookmaker's lines. The high moneyline is the most positive moneyline of any bookmaker. Furthermore, some additional metadata was also scraped. Here is the breakdown of each field in all the market.json files. Each team is well-defined for every game. For each team, there were approximately 10 games that had missing betting market data. These games were skipped and not added to the market.json files.
- "date" : date, month, and year the game is played
- "team_1" : home team, (if neutral game, then one of the teams)
- "team_2" : away team, (if neutral game, then other team)
- "score_1" : team_1 score
- "score_2" : taem_2 score
- "result" : 1 if team_1 won, 0 if team_2 won (there are no ties)
- "tournament" : unique string representing the season or tournament (e.g. NFL_2021-2022, NBA_Las_Vegas_Summer_League)
- "game_url" : unique game url
- "avg_moneyline_1" : average moneyline of team_1
- "avg_moneyline_2" : average moenyline of team_2
- "high_moneyline_1" : high moneyline of team_1
- "high_moneyline_2" : high moneyline of team_2




## Preprocessing

### team_combiner.py
This script combines every team's games.json and market.json files into the combined_games.json and combined_market.json files.

### convert_to_csv.py
This script converts the combined_market.json files into csv files and places it into the data/master/ subfolder.

### ml_probabilities.py
This script rearranges the columns as well as computes the moneyline probabilities. The moneyline probability of a team is given by the absolute value of the moneyline divided by the sum of the absolute values of both moneylines.
- "avg_prob_1" : abs(avg_moneyline_1) / (abs(avg_moneyline_1) + abs(avg_moneyline_2))
- "avg_prob_2" : abs(avg_moneyline_2) / (abs(avg_moneyline_1) + abs(avg_moneyline_2))
- "avg_prob_1" : abs(high_moneyline_1) / (abs(high_moneyline_1) + abs(high_moneyline_2))
- "avg_prob_2" : abs(high_moneyline_2) / (abs(high_moneyline_1) + abs(high_moneyline_2))

