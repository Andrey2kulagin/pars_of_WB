# всякие импорты
import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import statistics

# вход в маяк, открытие вб
def login(driver):  # 4
    print("#4")
    driver.get(url="https://app.mayak.bz/users/sign_in?utm_source=plugin")
    print("Открыто окно входа в маяк")
    driver.switch_to.window(driver.window_handles[0])
    print("ждём загрузки страницы входа в маяк")
    WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, "//*[@id='email']")))
    setMail = driver.find_element(By.XPATH, "//*[@id='email']")
    setPasw = driver.find_element(By.XPATH, "//*[@id='user_password']")
    setMail.send_keys("elnar3primo@yandex.ru")
    print("веден логин")
    setPasw.send_keys("pars123")
    print("введен пароль")
    setPasw.send_keys(Keys.ENTER)
    print("нажат энтер")
    driver.get(
        url="https://www.wildberries.ru/catalog/0/search.aspx?sort=popular&search=")
    WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, "//*[@id = 'searchInput']")))
    print("вб открыт и загружен")

# ввод инпута в поисковую строку
def search(driver, input):  # 5
    print("#5")
    inputLine = driver.find_element(By.XPATH, "//*[@id = 'searchInput']")
    print("Поисковая строка найдена")
    inputLine.clear()
    print("Поисковая строка очищена")
    inputLine.send_keys(input)
    print("Инпут введён в поисковую строку")
    inputLine.send_keys(Keys.ENTER)
    print("нажат энтер")


#Главная часть!!
# настройки опшион
chrome_options = Options()
# неробот
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option("useAutomationExtension", False)
# здесь настройки опшион для реплита, здесь может быть не нужно
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument("--window-size=1920,1080")
#chrome_options.headless = True # фоновый режим браузера
# установка расширения
extension_path = "C:\my programs\e5.0.4_0.crx"  # поменять расположение расширения
chrome_options.add_extension(extension_path)
# создание браузера
driver = webdriver.Chrome(options=chrome_options)
#запуск парсера
login(driver)#здесь всё работает отлично
#теперь надо научиться вводить запросы в поисковую строку
input = "фонарик"
search(driver,input)#всё хорошо