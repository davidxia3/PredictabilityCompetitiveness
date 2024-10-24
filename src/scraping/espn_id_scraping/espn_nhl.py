import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from webdriver_manager.chrome import ChromeDriverManager
import re
import os
import json

chrome_options = Options()
chrome_options.add_argument("--headless=new")

service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)



def list_subfolders(folder_path):
    teams = [name for name in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, name))]
    return teams


month_abbreviation_to_month = {
    "jan": "01", "feb": "02", "mar": "03", "apr": "04",
    "may": "05", "jun": "06", "jul": "07", "aug": "08",
    "sep": "09", "oct": "10", "nov": "11", "dec": "12"
}

teams = list_subfolders('data/nhl')

seasons = years = [year for year in range(2022, 2025) if year != 2005]


def get_id(s):
    pattern = r'\b\d{9}\b'
    
    match = re.search(pattern, s)
    
    if match:
        return match.group(0)
    else:
        return "000000000"


error_list = []

print(len(teams))
for team in teams:

    game_to_id_map = {}

    for season in seasons:

        base_url = f'https://www.espn.com/nhl/team/schedule/_/name/{team}/season/{season}'

        driver.get(base_url)

        WebDriverWait(driver, 9).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div/div/main/div[2]/div/div[5]/div/div/section/div/section/div[2]/div[2]/select[1]"))
        )


        game_types = {}
        dropdown = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/main/div[2]/div/div[5]/div/div/section/div/section/div[2]/div[2]/select[1]")
        options = dropdown.find_elements(By.TAG_NAME, "option")
        for option in options:
            game_types[option.get_attribute("value")[:1]] = option.text.lower().replace(" ","_")

        for j in game_types:
            print(team)
            print(season)
            print(j)
            base_url = f'https://www.espn.com/nhl/team/schedule/_/name/{team}/season/{season}/seasontype/{j}'

            driver.get(base_url)

            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "Table__TBODY"))
            )
            table = driver.find_element(By.CLASS_NAME, "Table__TBODY")
            
            rows = table.find_elements(By.TAG_NAME, "tr")

            print(len(rows))
            for row in rows:
                try:
                    time.sleep(0.5)
                    row_data = row.find_elements(By.TAG_NAME, "td")
                    if len(row_data) < 3:
                        continue
                    if row_data[0].text == "DATE":
                        continue
                    score = row_data[2]
                    link = score.find_element(By.TAG_NAME, "a").get_attribute("href")
                except:
                    print(f'{team} {season} {j}')
                    error_list.append(f'{team} {season} {j}')
                    continue
                

                id = get_id(link)

                d = row_data[0].text.split(" ")
                m = d[1].lower()
                month = month_abbreviation_to_month[m]
                day = d[2]
                if len(day) == 1:
                    day = "0" + day
                year = season
                if (game_types[j] != "postseason") and (month in ["08", "09", "10", "11", "12"]):
                    year = season - 1

                if j == "3":
                    year = season

                date = day + "-" + month + "-" + str(year)

                game_id = date


                
                game_to_id_map[game_id] = (id, game_types[j])



    with open(f'data/espn_mapping/nhl/{team}.json', 'w') as json_file:
        json.dump(game_to_id_map, json_file, indent=4)

            

print(error_list)

# notes
# - the arizona coyotes moved and rebranded in 2024-2025 to the utah hockey club. the 2024-2025 season is not considered for analysis, so there is no Utah hockey club in any of the data
# - however, espn no longer has its own individual webpage for the arizona coyotes, meaning it no longer has an easily scrapible schedule
# - luckily, each arizona coyote game is also a game for another team. the espn_processing file first tries to access the file for the coyotes, but because there is none, it will automatically use the second team's file
# - In most seasons, regular season ends in April and postseason begins in April
# - In 2020, when the pandemic hit in March, the remaining regular season games were cancelled and the postseason was delayed until August
# - Oddsportal lists 11 regular season games that all happened at the end of July (28-30), but espn does not, these games are left with null espn game ids
# - NJ TB 10-01-2010 (listed as January 10th on Oddsportal, but listed as January 8th on espn; manually added the espn game id and kept oddsportal date)