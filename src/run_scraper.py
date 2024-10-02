import subprocess
import time

teams = ["devils", "ducks",
         "flames", "flyers", "goldenknights", "hurricanes", "islanders", "jets", "kings", "kraken", "lightning", "mapleleafs",
         "oilers", "panthers", "penguins", "predators","rangers", "redwings", "sabres", "senators", "sharks", "stars", "wild"]
league = "nhl"


total_games_per_team = 1800
chunk_size = 200

for team in teams:
    print(f"Starting scrape for team: {team}")
    for start_index in range(0, total_games_per_team, chunk_size):
        print(f"  Scraping {team} games from index {start_index} to {start_index + chunk_size - 1}")
        subprocess.run(["python3", "src/scrape.py", team, league, str(start_index)])
        time.sleep(30)
