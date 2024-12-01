import os
import time
import sys
import pandas as pd
import csv
import gc
from selenium import webdriver  
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

# Selenium browser setup
options = Options()
options.add_argument("--headless")
driver = webdriver.Firefox(options=options)

# Month abbreviation mapping
month_abbreviation_to_month = {
    "jan": "01", "feb": "02", "mar": "03", "apr": "04",
    "may": "05", "jun": "06", "jul": "07", "aug": "08",
    "sep": "09", "oct": "10", "nov": "11", "dec": "12"
}

# Input arguments from `run_automated_scraper.py`
team = sys.argv[1] if len(sys.argv) > 1 else ""  
league = sys.argv[2] if len(sys.argv) > 2 else ""   
start_index = int(sys.argv[3]) if len(sys.argv) > 3 else 0

sport = "hockey"
data_path = f'raw_data/{league}/{team}/games.csv'

if not os.path.exists(data_path):
    print("not found")
    sys.exit(1)

games = pd.read_csv(data_path)

# Initialize variables
total_data = []
i = start_index
fails = 0
end_index = min(len(games), start_index + 200) 

# Failed games CSV
fail_file = 'failures.csv'
if os.path.exists(fail_file):
    failed_games = pd.read_csv(fail_file)
else:
    failed_games = pd.DataFrame(columns=["team", "index", "game_url"])

base_url = f'https://www.oddsportal.com/{sport}/'

# Scraping each individual game
while i < end_index:
    print(f"Scraping {team} {i}")
    game = games.iloc[i]
    game_url = game["game_url"] + "#home-away;1"

    try:
        # Retrieve game webpage
        driver.get(base_url + game_url) 
        time.sleep(2)

        # Scrape moneyline data
        avg_moneyline_1 = int(driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/main/div[3]/div[2]/div[2]/div/div/div[2]/div[1]/div[2]/div/p").text)
        avg_moneyline_2 = int(driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/main/div[3]/div[2]/div[2]/div/div/div[2]/div[1]/div[3]/div/p").text)

        tournament = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/main/div[3]/div[1]/div/ul[2]").find_elements(By.TAG_NAME, "a")[-1].text

        # Convert date
        date = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/main/div[3]/div[2]/div[1]/div[2]/div[1]/p[2]").text.split(" ")
        day = date[0]
        month_abbreviation = date[1].lower()
        month = month_abbreviation_to_month.get(month_abbreviation)
        year = date[2][:-1]

        # Create dictionary for the game and append to the list
        game_data = {
            "date": f"{day}-{month}-{year}",
            "team_1": game["team_1"],
            "team_2": game["team_2"],
            "score_1": game["score_1"],
            "score_2": game["score_2"],
            "result": 1 if int(game["score_1"]) > int(game["score_2"]) else 0,
            "tournament": tournament.replace(" ", "_"),
            "game_url": game_url,
            "avg_moneyline_1": avg_moneyline_1,
            "avg_moneyline_2": avg_moneyline_2,
        }
        total_data.append(game_data)

        date = "null"
        avg_moneyline_1 = "null"
        avg_moneyline_2 = "null"

        # reset failure counter
        fails = 0
        i += 1

    except Exception as e:
        print(f"Error at index {i}: {e}")
        

        # retry logic
        fails += 1
        if fails >= 3:
            print(f"Failed {i}. Skipping.")
            fails = 0
            i += 1

            failed_games = pd.concat([
            failed_games,
            pd.DataFrame({
                "team": [team],
                "index": [i],
                "game_url": [game_url],
            })
        ], ignore_index=True)
        else:
            print(f"Retrying {i}, attempt {fails}")
            time.sleep(2)
            continue

    gc.collect()

# Save results to CSV
market_file = f"raw_data/{league}/{team}/market.csv"
fieldnames = [
    "date", "team_1", "team_2", "score_1", "score_2", 
    "result", "tournament", "game_url", 
    "avg_moneyline_1", "avg_moneyline_2"
]

with open(market_file, mode="a", newline="", encoding="utf-8") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    if csv_file.tell() == 0:
        writer.writeheader()
    for game_data in total_data:
        writer.writerow(game_data)

# Save failures to CSV
failed_games.to_csv(fail_file, index=False)

driver.quit()
