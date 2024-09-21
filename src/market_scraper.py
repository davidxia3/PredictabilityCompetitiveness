from selenium import webdriver  
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import json
import time
import os
import gc

options = Options()
options.add_argument("--headless=new")

driver = webdriver.Chrome(options=options) 
base_url = "https://www.oddsportal.com/basketball/"

month_abbreviation_to_month = {
    "Jan": "january", "Feb": "february", "Mar": "march", "Apr": "april",
    "May": "may", "Jun": "june", "Jul": "july", "Aug": "august",
    "Sep": "september", "Oct": "october", "Nov": "november", "Dec": "december"
}

team = "mavericks"
x = 0

with open(f'data/nba/{team}/games.json', 'r') as file:
    games = json.load(file)

total_data = []
i = 0
fails = 0

while i < min(len(games), x+ 900):
    if i < x:
        i += 1
        continue

    print(i)

    game = games[i]
    game_url = game["game_url"]
    team_1 = game["team_1"]
    team_2 = game["team_2"]

    try:
        driver.get(base_url + game_url) 
        time.sleep(1)

        wrapper = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/main/div[3]/div[2]/div[2]/div[1]/div/div[2]")

        avg_moneyline_1 = None
        avg_moneyline_2 = None
        high_moneyline_1 = None
        high_moneyline_2 = None

        try:
            avg_moneyline_1 = int(driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/main/div[3]/div[2]/div[2]/div[1]/div/div[2]/div[1]/div[2]").text)
        except:
            pass

        try:
            avg_moneyline_2 = int(driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/main/div[3]/div[2]/div[2]/div[1]/div/div[2]/div[1]/div[3]").text)
        except:
            pass

        try:
            high_moneyline_1 = int(driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/main/div[3]/div[2]/div[2]/div[1]/div/div[2]/div[2]/div[2]").text)
        except:
            pass

        try:
            high_moneyline_2 = int(driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/main/div[3]/div[2]/div[2]/div[1]/div/div[2]/div[2]/div[3]").text)
        except:
            pass

        date = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/main/div[3]/div[2]/div[1]/div[3]/div[1]/p[2]").text.split(" ")

        day = date[0]
        month_abbreviation = date[1]
        month = month_abbreviation_to_month.get(month_abbreviation, month_abbreviation)
        year = date[2][:-1]

        game_data = {
            "id": (day + "_" + month + "_" + year + "_" + team_1.replace(" ", "_") + "_" + team_2.replace(" ", "_")).lower(),
            "date": f"{day} {month} {year}",
            "team_1": game["team_1"].lower(),
            "team_2": game["team_2"].lower(),
            "score_1": game["score_1"],
            "score_2": game["score_2"],
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
        fails += 1
        if fails >= 3:
            print(f"Failed after 3 attempts at index {i}")
            fails = 0
            i += 1 
        else:
            print(f"Retrying for index {i}, attempt {fails}")
            time.sleep(2)
            continue 

    gc.collect()

if os.path.getsize(f"data/nba/{team}/market.json") == 0:
    existing = [] 
else:
    with open(f"data/nba/{team}/market.json", "r") as market:
        existing = json.load(market)

with open(f"data/nba/{team}/market.json", "w") as outfile:
    json.dump(existing + total_data, outfile, indent=4)

driver.quit()
