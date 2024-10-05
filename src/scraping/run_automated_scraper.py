import subprocess
import time

# teams = ["bears", "bengals", "bills", "broncos", "browns", "buccaneers", "cardinals", "chargers", "chiefs",
#          "colts", "commanders", "cowboys", "dolphins", "eagles", "falcons", "fortyniners", "giants", 
#          "jaguars", "jets", "lions", "packers", "panthers", "patriots", "raiders", "rams", "ravens",
#          "saints", "seahawks", "steelers", "texans", "titans", "vikings"]

# teams = ["angels", "astros", "athletics", "bluejays", "braves", "brewers", "cardinals", "cubs", "diamondbacks", "dodgers", "giants", 
#          "guardians", "mariners", "marlins", "mets", "nationals", "orioles", "padres", "phillies", "pirates", "rangers", "rays",
#          "reds", "redsox", "rockies", "royals", "tigers", "twins", "whitesox", "yankees"]
teams = ["marlins", "mets", "nationals", "orioles", "padres", "phillies", "pirates", "rangers", "rays",
         "reds", "redsox", "rockies", "royals", "tigers", "twins", "whitesox", "yankees"]
league = "mlb"

print(len(teams))
total_games_per_team = 3400
chunk_size = 200

for team in teams:
    print(f"Starting scrape for team: {team}")
    for start_index in range(0, total_games_per_team, chunk_size):
        print(f"  Scraping {team} games from index {start_index} to {start_index + chunk_size - 1}")
        subprocess.run(["python3", "src/scraping/automated_scraper.py", team, league, str(start_index)])
        time.sleep(30)