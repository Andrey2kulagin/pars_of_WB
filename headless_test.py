import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
chrome_options = Options()
#chrome_options.headless = True # фоновый режим браузера
driver = webdriver.Chrome(options=chrome_options)
driver.get(
        url="https://www.wildberries.ru/catalog/0/search.aspx?sort=popular&search=")

inputLine = driver.find_element(By.XPATH, "//*[@id = 'searchInput']")
time.sleep(15)
driver.get(url="https://mayak.bz/spasibo")
window = driver.window_handles
print(window)
print(inputLine)