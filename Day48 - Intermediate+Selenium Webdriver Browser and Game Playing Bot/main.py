from datetime import datetime, timedelta
from time import time, sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
URL = "http://orteil.dashnet.org/experiments/cookie/"
driver = webdriver.Chrome(chrome_options)
driver.get(URL)

cookie = driver.find_element(By.ID, value="cookie")



def get_price_list():

    price_list_tags = driver.find_elements(By.CSS_SELECTOR, value="#store > div > b")
    price_list = [int(float(f'{tag.text.split("-")[-1].replace(",", "")}.00000')) for tag in price_list_tags[0:-2]]
    return price_list




start_time = time()
counter = 0
while True:
    cookie.click()
    current_time = time()
    difference = current_time - start_time
    
   
    if difference >= 4:
        counter += 1
        price_list = get_price_list()
       
        
        previous_amount = None
     
        store_items = driver.find_elements(By.CSS_SELECTOR, "#store > div")

    
        game_currency_amount = str(driver.find_element(By.ID, value="money").text).replace(",", "").strip()
        game_currency_amount = int(game_currency_amount)

        for price in price_list:  
            
            if game_currency_amount < price and game_currency_amount >= 17:
            
                try:
                    item_to_click = price_list.index(previous_amount)
                    store_items[item_to_click].click()
                    itemBought = item_to_click
                except StaleElementReferenceException:
                    pass
                except ValueError:
                    item_to_click = 0
                    store_items[item_to_click].click()
                    itemBought = item_to_click
        
                
            else:
                previous_amount = price

        print(f"2 seconds elapsed: {counter} ----> Price List: {price_list} ----> Item bought index: {itemBought}")
        start_time = time()

   

 




