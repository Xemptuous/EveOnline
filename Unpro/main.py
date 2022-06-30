import json
import os
import time
import logging
from colors import bcolors
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager


def main():
    print("Initializing driver...")
    start = time.time()
    os.environ['GH_TOKEN'] = 'INSERT_TOKEN_HERE'
    os.environ['WDM_LOG'] = 'false'
    moonBoard_url = "URL"

    logging.getLogger('WDM').setLevel(logging.NOTSET)

    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)

    try:
        driver.get(moonBoard_url)
        with open('/home/user/Python/Projects/Unpro/cookies.json') as cookiesFile:
            file = json.load(cookiesFile)
            driver.add_cookie(file[0])
            driver.add_cookie(file[1])
            cookiesFile.close()

        driver.get(moonBoard_url)

        time.sleep(2)

        tbody = driver.find_elements(By.XPATH, value="//tbody[@role='rowgroup']/tr")
        for i in range(1, len(tbody) + 1):
            dates = driver.find_elements(By.XPATH, value=f"//tbody[@role='rowgroup']/tr[{i}]/td[1]/h5")
            stations = driver.find_elements(By.XPATH, value=f"//tbody[@role='rowgroup']/tr[{i}]/td[2]/div/h5[1]")
            jackpot = driver.find_elements(By.XPATH, value=f"//tbody[@role='rowgroup']/tr[{i}]/td[3]/div")
            ores = driver.find_elements(By.XPATH, value=f"//tbody[@role='rowgroup']/tr[{i}]/td[4]/div/div")

            dates = [date.text for date in dates]
            stations = [station.text for station in stations]
            date = dates[0].split("\n")[1]
            station = stations[0]

            if jackpot:
                print(f"{bcolors.CYAN}{station} ({date})  JACKPOT{bcolors.ENDC}")
            else:
                print(f"{bcolors.BLUE}{station} ({date}){bcolors.ENDC}")
            print("")
            for j in range(1, len(ores) + 1):

                oreData = driver.find_elements(By.XPATH,
                                               value=f"//tbody[@role='rowgroup']/tr[{i}]/td[4]/div/div[{j}]/div/h5")
                remaining = driver.find_elements(By.XPATH,
                                                 value=f"//tbody[@role='rowgroup']/tr[{i}]/td[4]/div/div[{j}]/div/div")
                oreInfo = oreData[0].text.split("\n")
                oreName = oreInfo[0].split(" ")[0]
                oreType = oreInfo[1].split(" ")[0]
                mined = remaining[0].text.split(" ")[0]
                progress = float(mined[:-1])/4
                remain = 25 - round(progress)
                bar = "[" + "#"*round(progress) + "-"*remain + "]"

                if jackpot:
                    print(f"{bcolors.CYAN}{oreName:>20} | {oreType:<10} | {mined:<10} {bar:<10}{bcolors.ENDC}")
                    continue
                print(f"{bcolors.BLUE}{oreName:>20} | {oreType:<10} | {mined:<10} {bar:<10}{bcolors.ENDC}")
            print("")
            print("")
    except Exception as e:
        print(e)
    finally:
        end = time.time()
        time_elapsed = round((end - start), 2)
        print(f"Finished in {time_elapsed} seconds")
        driver.quit()


if __name__ == "__main__":
    main()
