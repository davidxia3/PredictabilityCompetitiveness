from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import time
import re
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
chrome_options.add_argument("--headless=new")

service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

base_url = "https://www.oddsportal.com/search/results/"

# defining official team names for inputting into OddsPortal and corresponding file names
league = "mlb"
sport = "baseball"

teams = ["Texas Rangers"]
file_names = ["rangers"]

# looping through each team
for i in range(len(teams)):
    team = teams[i]
    file_name = file_names[i]
    total_data = []
    search_query = team.replace(" ", "+")

    team_url = base_url + search_query + f'/{sport}/'

    driver.get(team_url)


    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/main/div[3]/div[3]/div/div[1]/ul/li[2]/div/div"))
    )

    results = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/main/div[3]/div[3]/div/div[1]/ul/li[2]/div/div").text
    num_results = int(results.split("(")[1].split(")")[0])

    if num_results == 0:
        print("ERROR: 0 results: " + team)
        continue
    elif num_results < 100:
        team_url = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/main/div[3]/div[3]/div/div[2]/div[2]/a").get_attribute("href") + "/"
        driver.get(team_url)

    
    last_page = int(driver.find_elements(By.CLASS_NAME, "pagination-link")[-2].text)


    # looping through each team's pagination
    for page in range(1, last_page + 1):
        driver.get(team_url + "page/" + str(page) + "/")

        print(team + " " + str(page))

        time.sleep(1)

        games = driver.find_elements(By.CLASS_NAME, "eventRow")
        print(len(games))
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
                    game_data["team_1"] = lines[1]
                    game_data["score_1"] = int(lines[2])
                    game_data["score_2"] = int(lines[4])
                    game_data["team_2"] = lines[5]
                    
                    game_data["game_url"] = game.find_elements(By.TAG_NAME, "a")[-4].get_attribute("href").split("https://www.oddsportal.com/" + sport + "/")[1]
                    total_data.append(game_data)
                except:
                    pass

            else:
                print("no date: " + team)
                continue

    with open("data/" + league + "/" + file_name + "/games.json", "w") as outfile:
        json.dump(total_data, outfile, indent=4)

driver.quit()
