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

#нахождение кол-ва карточек
def getCount(driver_):  # 6
    print("6")
    print("ждём загрузки кол-ва товаров")
    WebDriverWait(driver_, 50).until(EC.presence_of_element_located((By.XPATH, "//*[@class='goods-count']/span[1]")))
    print("кол-во товаров загружено")
    while driver_.find_element(By.XPATH, "//*[@class='goods-count']/span[1]").text=="":
        continue
    cards_count_element = driver_.find_element(By.XPATH, "//*[@class='goods-count']/span[1]")
    print("кол-во товаров получено")
    cards_count = cards_count_element.text.replace(" ","")
    return int(cards_count)

# получение интового массива с ценами
def getPrices(driver):  # 10
    print("#10")
    print("ждём, пока цены загрузятся")
    WebDriverWait(driver, 50).until(
        EC.presence_of_element_located((By.XPATH, "//*[@class='lower-price']")))
    priceslist = driver.find_elements(By.XPATH, "//*[@class='lower-price']")
    print("нашли цены")
    prices = []
    print("#11")
    print("начинается обработка массива цен")
    for price in priceslist:  # 11
        prices.append(int(price.text.replace(" ", "").replace("₽", "")))
    return prices

# получение интового массива с выручкой
def getEarnings(driver):  # 12
    print("#12")
    print("ждём закгрузки блока маяка")
    time.sleep(6)
    element = driver.find_element((By.TAG_NAME,"body"))
    element.screenshot("screenshot_full.png")
    WebDriverWait(driver, 50).until(
        EC.presence_of_element_located((By.XPATH, "//*[@class='mayak-details mayak-details--in-card']/div[1]")))
    print("ждём загрузки значений в маяк")
    while driver.find_elements(By.XPATH, "//*[@class='mayak-details mayak-details--in-card']/div[1]")[0]=="":
        continue
    print("находим эти цены")
    earnings = driver.find_elements(By.XPATH, "//*[@class='mayak-details mayak-details--in-card']/div[1]")
    earnings_arr = []
    for earning in earnings:  # 13
        print(earning.text)
        print("#13")
        # if earning.text.replace("\u202f", "").split(" ")[1] == "-" or earning.text.replace("\u202f", "").split(" ")[1] == "0" :  # 7
        #     print("#7")
        #     earnings_arr.append(0)
        # else:
        #     earnings_arr.append(int(earning.text.replace("\u202f", "").split(" ")[1]))
        earn = earning.text.replace(" ","").replace("р.","")
        print(earn.find(" "))
        earnings_arr.append(earn)
    return earnings_arr

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
extension_path = "C:\my programs\e5.0.4_0.crx"  # поменять расположение расширения
chrome_options.add_extension(extension_path)
chrome_options.headless = True # фоновый режим браузера
# установка расширения

# создание браузера
driver = webdriver.Chrome(options=chrome_options)
#запуск парсера
login(driver)#здесь всё работает отлично
input = "фонарик"
search(driver,input)#поиск нужного товара
cards_count = getCount(driver)#nахождение кол-ва карточек
prices_arr = getPrices(driver)#нахождение массива цен
#print(getEarnings(driver))
