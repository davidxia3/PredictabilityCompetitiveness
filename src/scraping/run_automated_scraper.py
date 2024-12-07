import subprocess
import time


# defining teams and league
teams = ['CGY', 'CHI', 'COL', 'DAL', 'DET', 'EDM', 'FLA', 'LA',
         'MIN', 'MTL', 'NJ', 'NSH', 'NYI', 'NYR', 'OTT', 'PHI', 'SEA', 'SJ', 'STL', 'TB',
         'TOR', 'VAN', 'VGK', 'WPG', 'WSH']
league = "nhl"
print(len(teams))
total_games_per_team = 2000
chunk_size = 200


# looping through teams chunk by chunk and running automated_scraper.py
for team in teams:
    print(f'Starting scrape for team: {team}')
    for start_index in range(0, total_games_per_team, chunk_size):
        print(f'Scraping {team} games from index {start_index} to {start_index + chunk_size - 1}')
        subprocess.run(["python3", "src/scraping/firefox_automated_scraper.py", team, league, str(start_index)])
        time.sleep(30)