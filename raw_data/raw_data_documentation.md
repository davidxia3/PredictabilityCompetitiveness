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