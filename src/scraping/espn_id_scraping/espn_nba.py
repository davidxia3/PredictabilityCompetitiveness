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

teams = list_subfolders('data/nba')

seasons = list(range(2009, 2025))

# function to extract the string of 9 digits from the url
def get_id(s):
    pattern = r'\b\d{9}\b'
    
    match = re.search(pattern, s)
    
    if match:
        return match.group(0)
    else:
        return "000000000"


# iterates through each team and saves a json dictionary for that team
for team in teams:

    game_to_id_map = {}

    # scraping the team's ESPN webpage
    for season in seasons:

        base_url = f'https://www.espn.com/nba/team/schedule/_/name/{team}/season/{season}'

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
            base_url = f'https://www.espn.com/nba/team/schedule/_/name/{team}/season/{season}/seasontype/{j}'

            driver.get(base_url)

            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "Table__TBODY"))
            )
            table = driver.find_element(By.CLASS_NAME, "Table__TBODY")
            
            rows = table.find_elements(By.TAG_NAME, "tr")

            print(len(rows))
            for row in rows:
                # for each game, extract the espn_id and the game_type
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

                date = day + "-" + month + "-" + str(year)

                game_id = date
                
                game_to_id_map[game_id] = (id, game_types[j])


    with open(f'raw_data/espn_mapping/nba/{team}.json', 'w') as json_file:
        json.dump(game_to_id_map, json_file, indent=4)

            

