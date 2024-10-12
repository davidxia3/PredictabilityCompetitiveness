from selenium import webdriver  
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import json
import time
import os
import gc
import sys

options = Options()
options.add_argument("--headless=new")

driver = webdriver.Chrome(options=options) 

month_abbreviation_to_month = {
    "Jan": "january", "Feb": "february", "Mar": "march", "Apr": "april",
    "May": "may", "Jun": "june", "Jul": "july", "Aug": "august",
    "Sep": "september", "Oct": "october", "Nov": "november", "Dec": "december"
}

# input arguments from run_automated_scraper.py
team = sys.argv[1] if len(sys.argv) > 1 else "bears"  
league = sys.argv[2] if len(sys.argv) > 2 else "nfl"   
start_index = int(sys.argv[3]) if len(sys.argv) > 3 else 0

# must scrape in chunks because of insufficient memory
chunk_size = 200
end_index = start_index + chunk_size


# define sport and base_url
sport = "american-football"
base_url = f'https://www.oddsportal.com/{sport}/'


# retrieve previously scraped chunks
data_path = f'data/{league}/{team}/games.json'
if not os.path.exists(data_path):
    print("not found")
    sys.exit(1)

with open(data_path, 'r') as file:
    games = json.load(file)


total_data = []
i = start_index
fails = 0

# scraping each individual game
while i < min(len(games), end_index):
    print("scraping " + team + " " + str(i))

    # 
    game = games[i]
    game_url = game["game_url"]
    team_1 = game["team_1"]
    team_2 = game["team_2"]

    try:
        # retrieve game webpage
        driver.get(base_url + game_url) 
        time.sleep(1)

        # scrape moneyline data
        avg_moneyline_1 = int(driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/main/div[3]/div[2]/div[2]/div[1]/div/div[2]/div[1]/div[2]").text)
        avg_moneyline_2 = int(driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/main/div[3]/div[2]/div[2]/div[1]/div/div[2]/div[1]/div[3]").text)
        high_moneyline_1 = int(driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/main/div[3]/div[2]/div[2]/div[1]/div/div[2]/div[2]/div[2]").text)
        high_moneyline_2 = int(driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/main/div[3]/div[2]/div[2]/div[1]/div/div[2]/div[2]/div[3]").text)

        tournament = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/main/div[3]/div[1]/div/ul[2]").find_elements(By.TAG_NAME, "a")[-1].text
        
        # converting date 
        date = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/main/div[3]/div[2]/div[1]/div[2]/div[1]/p[2]").text.split(" ")
        day = date[0]
        month_abbreviation = date[1]
        month = month_abbreviation_to_month.get(month_abbreviation, month_abbreviation)
        year = date[2][:-1]

        # creating dictionary for the game and adding it to the json list
        game_data = {
            "date": f"{day} {month} {year}",
            "team_1": game["team_1"].lower(),
            "team_2": game["team_2"].lower(),
            "score_1": game["score_1"],
            "score_2": game["score_2"],
            "result": 1 if int(game["score_1"]) > int(game["score_2"]) else 0,
            "tournament": tournament.replace(" ","_"),
            "game_url": game_url,
            "avg_moneyline_1": avg_moneyline_1,
            "avg_moneyline_2": avg_moneyline_2,
            "high_moneyline_1": high_moneyline_1,
            "high_moneyline_2": high_moneyline_2
        }

        total_data.append(game_data)
        driver.delete_all_cookies()

        
        fails = 0
        i += 1

    except Exception as e:
        # webpage sometimes fails to load, so given 3 tries to ensure that data truly is missing
        print(f"error at index {i}: {e}")
        print(game_url)
        fails += 1
        if fails >= 3:
            print(f"failed {i}. skipping")
            fails = 0
            i += 1
        else:
            print(f"retrying {i} attempt {fails}")
            time.sleep(2)
            continue 

    gc.collect()

market_file = f"data/{league}/{team}/market.json"
existing_data = []

if os.path.exists(market_file) and os.path.getsize(market_file) > 0:
    with open(market_file, "r") as market:
        existing_data = json.load(market)

with open(market_file, "w") as outfile:
    json.dump(existing_data + total_data, outfile, indent=4)

driver.quit()