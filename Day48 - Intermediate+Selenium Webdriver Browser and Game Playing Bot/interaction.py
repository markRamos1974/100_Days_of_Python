from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
URL = "https://en.wikipedia.org/wiki/Main_Page"
driver = webdriver.Chrome(chrome_options)
driver.get(URL)

number_of_articles = driver.find_element(By.CSS_SELECTOR, value="#articlecount > a").text
print(number_of_articles)

driver.quit()
