import subprocess
import time


# defining teams and league
teams = ["bears"]
league = "nfl"
print(len(teams))
total_games_per_team = 400
chunk_size = 200


# looping through teams chunk by chunk and running automated_scraper.py
for team in teams:
    print(f"Starting scrape for team: {team}")
    for start_index in range(0, total_games_per_team, chunk_size):
        print(f"  Scraping {team} games from index {start_index} to {start_index + chunk_size - 1}")
        subprocess.run(["python3", "src/scraping/automated_scraper.py", team, league, str(start_index)])
        time.sleep(30)