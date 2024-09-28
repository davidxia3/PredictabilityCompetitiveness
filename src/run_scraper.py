# run_scrape.py

import subprocess
import time

# List of teams to scrape
teams = ["phillies", "pirates", "rangers", "rays", "reds", "redsox", "rockies", "royals", "tigers", "twins", "whitesox", "yankees"]  # Add all team names here
league = "mlb"


#redsox 200
# Define the total number of games to scrape per team and the chunk size
total_games_per_team = 3200
chunk_size = 200

# Iterate over each team and run the scraper in chunks
for team in teams:
    print(f"Starting scrape for team: {team}")
    for start_index in range(0, total_games_per_team, chunk_size):
        print(f"  Scraping {team} games from index {start_index} to {start_index + chunk_size - 1}")
        subprocess.run(["python3", "src/scrape.py", team, league, str(start_index)])
        time.sleep(30)
