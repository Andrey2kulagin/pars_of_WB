import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import statistics
# настройки опшион
chrome_options = Options()
# неробот
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option("useAutomationExtension", False)
# здесь настройки опшион для реплита, здесь может быть не нужно
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
#chrome_options.add_argument("--headless")
#chrome_options.headless = True # фоновый режим браузера
# установка расширения
extension_path = "C:\my programs\e5.0.4_0.crx"  # поменять расположение расширения
chrome_options.add_extension(extension_path)
driver = webdriver.Chrome(options=chrome_options)
#начало логина
# driver.close()
# driver.switch_to.window(driver.window_handles[0])
driver.get(url = "https://app.mayak.bz/users/sign_in?utm_source=plugin")
driver.switch_to.window(driver.window_handles[0])

WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, "//*[@id='email']")))
setMail = driver.find_element(By.XPATH, "//*[@id='email']")
setPasw = driver.find_element(By.XPATH, "//*[@id='user_password']")
setMail.send_keys("elnar3primo@yandex.ru")
print("веден логин")
setPasw.send_keys("pars123")
print("введен пароль")
loginBTN = driver.find_element(By.XPATH, "//*[@class='btn btn-lg btn-primary']")
loginBTN.click()