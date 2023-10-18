from selenium import webdriver
from selenium.webdriver.common.by import By
import time


timeout = 300 # 5*60s
start_time = time.time()
upgrade_start_time = time.time()

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://orteil.dashnet.org/experiments/cookie/")


def click_cookie():
    cookie = driver.find_element(By.ID, "cookie")
    cookie.click()

while time.time() <= start_time + timeout:
    click_cookie()



    time_for_upgrade = 5 

    if time.time() >= upgrade_start_time+time_for_upgrade:

        money = int(driver.find_element(By.ID, "money").text.replace(",",""))
        print(money)

        store = driver.find_element(By.ID, "store")

        cursor = store.find_element(By.ID, "buyCursor")
        grandma = store.find_element(By.ID, "buyGrandma")
        factory = store.find_element(By.ID, "buyFactory")
        mine = store.find_element(By.ID, "buyMine")
        shipment = store.find_element(By.ID, "buyShipment")
        alchemy = store.find_element(By.ID, "buyAlchemy lab")
        portal = store.find_element(By.ID, "buyPortal")
        timemachine = store.find_element(By.ID, "buyTime machine")

        upgrades = [cursor, grandma, factory, mine, shipment, alchemy, portal, timemachine]
        cost_upgrade = [
            int(
                upgrade.find_element(By.CSS_SELECTOR, "b")
                .text.split("-")[1]
                .strip()
                .replace(",", "")
            )
            for upgrade in upgrades
        ]
        print(cost_upgrade)

        upgrades.reverse()
        cost_upgrade.reverse()


        
        upgrade_start_time = time.time()
        # to pass the selenium.common.exceptions.StaleElementReferenceException
        try:
            for i in range(len(upgrades)):
                if cost_upgrade[i] <= money:
                    upgrades[i].click()
        except:
            pass

cookie_per_second = driver.find_element(By.ID, "cps")
print(cookie_per_second.text)

driver.quit()