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



# параметры для нахождения кол-ва через xhr
def getParam(str):  # 1
    print("#1")
    link = "https://wbxsearch.wildberries.ru/exactmatch/v2/common?query=" + str
    if requests.get(link).status_code == 200:  # 2
        print("#2")
        if requests.get(link).status_code != "":  # 3
            print("#3")
            params = requests.get(link).json()
            param = []
            param.append(params["shardKey"])
            param.append(params["query"])
            return param
        else:
            return ""
    else:
        return ""


# ввод инпута в поисковую строку
def search(driver, input):  # 5
    print("#5")
    WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, "//*[@id = 'searchInput']")))
    inputLine = driver.find_element(By.XPATH, "//*[@id = 'searchInput']")
    inputLine.clear()
    inputLine.send_keys(input)
    inputLine.send_keys(Keys.ENTER)


# вход в маяк и еще здесь будет подтверждение возраста
def login(driver):  # 4
    print("#4")
    driver.get(url="https://app.mayak.bz/users/sign_in?utm_source=plugin")
    driver.switch_to.window(driver.window_handles[0])

    WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, "//*[@id='email']")))
    setMail = driver.find_element(By.XPATH, "//*[@id='email']")
    setPasw = driver.find_element(By.XPATH, "//*[@id='user_password']")
    setMail.send_keys("elnar3primo@yandex.ru")
    print("веден логин")
    setPasw.send_keys("pars123")
    print("введен пароль")
    setPasw.send_keys(Keys.ENTER)
    driver.get(
        url="https://www.wildberries.ru/catalog/0/search.aspx?sort=popular&search=лдлвыдлывдлывлдыдл")


# получение кол-ва через hxr
def getCount(str):  # 6
    print("#6")
    if getParam(str) != "":  # 8
        print("#8")
        link = "https://wbxcatalog-ru.wildberries.ru/" + getParam(str)[
            0] + "/filters?filters=xsubject;fkind;fcolor;fbrand&spp=0&regions=83,75,64,4,38,30,33,70,71,22,31,66,69,48,40,82,1,80,68&stores=117673,122258,122259,125238,125239,125240,6159,507,3158,117501,120602,6158,124731,121709,120762,159402,2737,130744,117986,1733,686,132043&pricemarginCoeff=1.0&reg=0&appType=1&offlineBonus=0&onlineBonus=0&emp=0&locale=ru&lang=ru&curr=rub&couponsGeo=12,3,18,15,21&dest=-1029256,-102269,-2263058,-380707&" + \
               getParam(str)[1]
        if requests.get(link).status_code == 200:  # 9
            print("#9")
            return int(requests.get(link).json()["data"]["total"])
        else:
            return 0
    else:
        return 0


# получение интового массива с ценами
def getPrices(driver, input):  # 10
    print("#10")
    WebDriverWait(driver, 50).until(
        EC.presence_of_element_located((By.XPATH, "//*[@class='lower-price']")))

    priceslist = driver.find_elements(By.XPATH, "//*[@class='lower-price']")
    prices = []
    for price in priceslist:  # 11
        print("#11")
        print(price.text)
        if price.text=="":
            break
        if price.text.find(" ") != -1:
            prices.append(int(price.text.replace(" ", "").replace("₽", "")))
        else:
            prices.append(int(price.text.replace("₽", "")))

    return prices


# получение интового массива с выручкой
def getEarnings(driver):  # 12
    print("#12")
    earnings = driver.find_elements(By.XPATH, "//*[@class='mayak-details mayak-details--in-card']/div[1]")
    print(earnings)
    a = []
    for earning in earnings:  # 13
        print(earning.text)
        print("#13")
        if earning.text.replace("\u202f", "").split(" ")[1] == "-" or earning.text.replace("\u202f", "").split(" ")[1] == "0" :  # 7
            print("#7")
            a.append(0)
        else:
            a.append(int(earning.text.replace("\u202f", "").split(" ")[1]))
    return a


# вычисление кэфов
def k1(earning):  # 14
    print("#14")
    return sum(earning)


def k2(earning):  # 15
    print("#15")
    return statistics.median(earning)


def k3(earning):  # 16
    print("#16")
    if len(earning) >= 40:  # 17
        print("#17")
        sum1 = sum(earning[0:20])
    else:  # 18
        print("#18")
        sum1 = sum(earning[0:len(earning) // 2])
    return sum1


def k4(earning):  # 19
    print("#19")
    if len(earning) >= 40:  # 20
        print("#20")
        sum1 = sum(earning[20:])
    else:  # 21
        print("#21")
        sum1 = sum(earning[len(earning) // 2 + 1:])
    return sum1


def k5(earning):  # 22
    print("#22")
    if len(earning) >= 40:  # 23
        print("#23")
        med = statistics.median(earning[0:20])
    else:  # 24
        print("#24")
        med = statistics.median(earning[0:len(earning) // 2])
    return med


def k6(earning):  # 25
    print("#25")
    if len(earning) >= 40:  # 26
        print("#26")
        med = statistics.median(earning[20:])
    else:  # 27
        print("#27")
        med = statistics.median(earning[len(earning) // 2 + 1:])
    return med


def k7(prices):  # 28
    print("#28")
    return min(prices)


def k8(prices):  # 29
    print("#29")
    return max(prices)


def k9(prices):  # 30
    print("#30")
    return statistics.median(prices)


# настройки опшион
chrome_options = Options()
# неробот
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option("useAutomationExtension", False)
# здесь настройки опшион для реплита, здесь может быть не нужно
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.headless = True # фоновый режим браузера
# установка расширения
extension_path = "C:\my programs\e5.0.4_0.crx"  # поменять расположение расширения
chrome_options.add_extension(extension_path)
driver = webdriver.Chrome(options=chrome_options)
login(driver)
fin = open("m_input.txt", "r", encoding="utf-8")

for input in fin:  # 31
    data = open("data.txt", "a", encoding="utf-8")
    fout = open("output.txt", "a", encoding="utf-8")
    print("#31")
    print("---------------_____----------________----------___________------_______----" + "\n" + "\n")
    print("начало работы с ", input)
    search(driver, input)
    cardsCount = getCount(input)
    prices = getPrices(driver, input)
    earning = getEarnings(driver)
    print(cardsCount)
    print(prices)
    print(earning)
    # ki1 = k1(earning)
    # ki2 = k2(earning)
    # ki3 = k3(earning)
    # ki4 = k4(earning)
    # ki5 = k5(earning)
    # ki6 = k6(earning)
    # ki7 = k7(prices)
    # ki8 = k8(prices)
    # ki9 = k9(prices)
    # data.write(input[0:input.find("  ")] + " earnings = " + str(earning))
    # data.close()
    # outStr = input[0:input.find("  ")] + "," + str(cardsCount) + "," + str(ki1) + "," + str(ki2) + "," + str(
    #     ki3) + "," + str(ki4) + "," + str(ki5) + "," + str(ki6) + "," + str(ki7) + "," + str(ki8) + "," + str(ki9)
    # fout.write(outStr + "\n")
    # fout.close()
    print("---------------_____----------________----------___________------_______----" + "\n" + "\n")
    print("конец работы с ", input)
