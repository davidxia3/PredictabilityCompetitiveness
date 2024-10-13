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

chrome_options = Options()
chrome_options.add_argument("--headless=new")

service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

def list_subfolders(folder_path):
    subfolders = [name for name in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, name))]
    return subfolders

league = "nba"
teams = list_subfolders(f'data/{league}/')
print(teams)

seasons = list(range(2009, 2025))

game_to_id_map = {}

def get_id(s):
    pattern = r'\b\d{9}\b'
    
    match = re.search(pattern, s)
    
    if match:
        return match.group(0)
    else:
        return "000000000"


for i in range(len(teams)):
    team = teams[i]
    file = files[i]

    for season in seasons:

        for j in range(1,4):

            base_url = f'https://www.espn.com/{league}/team/schedule/_/name/{team}/season/{season}/seasontype/{j}'

            driver.get(base_url)

            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "Table__TBODY"))
            )
            table = driver.find_element(By.CLASS_NAME, "Table__TBODY")

            rows = table.find_elements(By.TAG_NAME, "tr")

            game_type = rows[0].text.lower()

            for row in rows:
                time.sleep(0.5)
                if len(row.find_elements(By.TAG_NAME, "td")) < 3:
                    continue
                if row.find_elements(By.TAG_NAME, "td")[0].text == "DATE":
                    continue
                score = row.find_elements(By.TAG_NAME, "td")[2]
                link = score.find_element(By.TAG_NAME, "a").get_attribute("href")
                
                

                id = get_id(link)


            

