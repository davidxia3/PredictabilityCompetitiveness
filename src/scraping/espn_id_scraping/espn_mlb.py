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

teams = list_subfolders('data/mlb')

seasons = list(range(2006, 2024))


def get_id(s):
    pattern = r'\b\d{9}\b'
    
    match = re.search(pattern, s)
    
    if match:
        return match.group(0)
    else:
        return "000000000"


for team in teams:

    game_to_id_map = {}

    for season in seasons:

        base_url = f'https://www.espn.com/mlb/team/schedule/_/name/{team}/season/{season}'

        driver.get(base_url)

        WebDriverWait(driver, 9).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div/div/main/div[2]/div/div[5]/div/div/section/div/section/div[2]/div[2]/select[1]"))
        )


        game_types = {}
        dropdown = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/main/div[2]/div/div[5]/div/div/section/div/section/div[2]/div[2]/select[1]")
        options = dropdown.find_elements(By.TAG_NAME, "option")
        for option in options:
            value = option.get_attribute("value")
            if len(value) == 2:
                game_types[option.text.lower().replace(" ", "_")] = value[:1]
            else:
                game_types[option.text.lower().replace(" ", "_")] = value[:1] + "/half/" + value[2:]

        for game_type in game_types:
            print(team)
            print(season)
            print(game_type)
            base_url = f'https://www.espn.com/mlb/team/schedule/_/name/{team}/season/{season}/seasontype/{game_types[game_type]}'

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
                    print(f'{team} {season} {game_type}')
                    continue
                

                id = get_id(link)

                d = row_data[0].text.split(" ")
                m = d[1].lower()
                month = month_abbreviation_to_month[m]
                day = d[2]
                if len(day) == 1:
                    day = "0" + day
                year = season

                date = day + "-" + month + "-" + str(year)

                game_id = date


                
                game_to_id_map[game_id] = (id, game_type)



    with open(f'raw_data/espn_mapping/mlb/{team}.json', 'w') as json_file:
        json.dump(game_to_id_map, json_file, indent=4)

            