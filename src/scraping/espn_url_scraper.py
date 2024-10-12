import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
chrome_options.add_argument("--headless=new")
service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

google_url = "https://www.google.com/"
league = "nfl"

def valid(value):
    return value.isdigit() and len(value) == 9



with open(f'data/master/{league}_market.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)

    with open(f'data/master/{league}_market_with_espn_id.csv', mode='w', newline='') as new_file:
        fieldnames = csv_reader.fieldnames + ['espn_id']
        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames)

        csv_writer.writeheader()

        for row in csv_reader:
            google_search = row["team_1"] + " " + row["team_2"] + " " + row["date"] + " espn"
            retries = 3
            espn_id = ""

            for attempt in range(retries):
                try:
                    driver.get(google_url)

                    search_box = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.NAME, "q"))
                    )
                    search_box.send_keys(google_search)
                    search_box.submit()

                    time.sleep(1)
                    
                    first_result = driver.find_elements(By.CLASS_NAME, "yuRUbf")[0]
                    first_link = first_result.find_elements(By.TAG_NAME, "a")[0]
                    espn_id = first_link.get_attribute('href').split("gameId")[1][1:10]
                    if not valid(espn_id):
                        print("not valid " + google_search)
                    # espn_id = first_link.get_attribute("href").split("gameId/")[1].split("/")[0]
                    break 

                except Exception as e:
                    print(f"Attempt {attempt+1} failed for {google_search}")
                    print(e)
                    time.sleep(1) 

            if not espn_id:
                print(f"No ESPN ID found for {google_search} after {retries} attempts")

            row['espn_id'] = espn_id if espn_id else None
            csv_writer.writerow(row)

            time.sleep(1)

driver.quit()
