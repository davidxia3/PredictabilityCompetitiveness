import os
import time
import sys
import pandas as pd
import csv
import gc
from selenium import webdriver  
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)

month_abbreviation_to_month = {
    "jan": "01", "feb": "02", "mar": "03", "apr": "04",
    "may": "05", "jun": "06", "jul": "07", "aug": "08",
    "sep": "09", "oct": "10", "nov": "11", "dec": "12"
}

# input arguments from run_automated_scraper.py
team = sys.argv[1] if len(sys.argv) > 1 else ""  
league = sys.argv[2] if len(sys.argv) > 2 else ""   
start_index = int(sys.argv[3]) if len(sys.argv) > 3 else 0

sport = ""

data_path = f'data/{league}/{team}/games.csv'
if not os.path.exists(data_path):
    print("not found")
    sys.exit(1)

games = pd.read_csv(data_path)

total_data = []
i = start_index
fails = 0
end_index = min(len(games), start_index + 200) 

base_url = f'https://www.oddsportal.com/{sport}/'

# scraping each individual game
while i < end_index:
    print("scraping " + team + " " + str(i))

    game = games.iloc[i] 
    game_url = game["game_url"]

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
        month_abbreviation = date[1].lower()
        month = month_abbreviation_to_month.get(month_abbreviation)
        year = date[2][:-1]

        # creating dictionary for the game and adding it to the list
        game_data = {
            "date": f"{day}-{month}-{year}",
            "team_1": game["team_1"],
            "team_2": game["team_2"],
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

market_file = f"data/{league}/{team}/market.csv"
fieldnames = [
    "date", "team_1", "team_2", "score_1", "score_2", 
    "result", "tournament", "game_url", 
    "avg_moneyline_1", "avg_moneyline_2", 
    "high_moneyline_1", "high_moneyline_2"
]

# Open the market.csv file in append mode
with open(market_file, mode="a", newline="", encoding="utf-8") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    
    # Check if the file is empty to write the header
    if csv_file.tell() == 0:  # Only write header if the file is empty
        writer.writeheader()
        
    for game_data in total_data:
        writer.writerow(game_data)

driver.quit()
