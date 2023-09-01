from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
URL = "https://www.python.org/"
driver = webdriver.Chrome(chrome_options)



driver.get(URL)
driver.fullscreen_window()
dates_tags = driver.find_elements(By.CSS_SELECTOR, ".event-widget > .shrubbery > .menu > li > time")
event_tags = driver.find_elements(By.CSS_SELECTOR, ".event-widget > .shrubbery > .menu > li > a")

event_details = {index:{"time": dates_tags[index].text, "name": event_tags[index].text} for index in range(len(dates_tags))}

print(event_details)


driver.quit()
