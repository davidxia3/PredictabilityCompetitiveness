from selenium import webdriver  
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import time
import re

options = Options()
options.headless = False

driver = webdriver.Chrome(options=options)


with open('teams.json', 'r') as file:
    data = json.load(file)

base_url = "https://www.oddsportal.com/search/results/"

teams = data["teams"]


#testing
teams = ["Los Angeles Lakers", "Atlanta Hawks"]


total_data = []


for team in teams:
    search_query = team.replace(" ","+")

    team_url = base_url + search_query + "/basketball/"

    driver.get(team_url)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/main/div[3]/div[3]/div/div[1]/ul/li[2]/div/div")))

    results = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/main/div[3]/div[3]/div/div[1]/ul/li[2]/div/div").text
    
    num_results = int(results.split("(")[1].split(")")[0])

    if num_results == 0:
        print("ERROR: 0 results: " + team)
        continue
    elif num_results < 100:
        team_url = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/main/div[3]/div[3]/div/div[2]/div[2]/a").get_attribute("href") + "/"
        driver.get(team_url)
    
    last_page = int(driver.find_elements(By.CLASS_NAME, "pagination-link")[-2].text)
    

    for page in range(1, last_page+1):
        driver.get(team_url + "page/" + str(page) + "/")

        print(team + " "  + str(page))

        time.sleep(1)

        games = driver.find_elements(By.CLASS_NAME, "eventRow")

        for game in games:
            game_data = {}
            pattern = r'\b.{2}/.{3}\b'
            match = re.search(pattern, game.text)
            if match:
                start_index = match.start()
                game_text = game.text[start_index:]
                lines = game_text.splitlines()

                try:
                    game_data["date"] = lines[0]
                    game_data["team1"] = lines[1]
                    game_data["score1"] = int(lines[2])
                    game_data["score2"] = int(lines[4])
                    game_data["team2"] = lines[5]
                    game_data["moneyline1"] = int(lines[-3])
                    game_data["moneyline2"] = int(lines[-2])
                    game_data["game_url"] = game.find_elements(By.TAG_NAME, "a")[-4].get_attribute("href").split("https://www.oddsportal.com/basketball/")[1]

                    total_data.append(game_data)
                except:
                    pass
        
            else:
                print("ERROR: no date: " + team)
                continue

with open("data.json","w") as outfile:
    json.dump(total_data, outfile, indent=4)