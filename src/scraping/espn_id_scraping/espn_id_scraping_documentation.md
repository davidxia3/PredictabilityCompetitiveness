# Scraping Documentation

## Contains all scripts to scrape ESPN game IDs

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