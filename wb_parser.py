from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import statistics


class Parser_wb():

    def set_option(self):
        chrome_options = Options()
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option("useAutomationExtension", False)
        # здесь настройки опшион для реплита, здесь может быть не нужно
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.headless = True  # фоновый режим браузера
        return chrome_options

    # установка расширения

    def __init__(self, input):
        print("init")
        self.input = input
        self.driver = webdriver.Chrome(options=self.set_option())
        print("init2")

    # вход в маяк, открытие вб

    def login(self):  # 4
        driver = self.driver
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

    def search(self):  # 5
        print("#5")
        inputLine = self.driver.find_element(By.XPATH, "//*[@id = 'searchInput']")
        print("Поисковая строка найдена")
        inputLine.clear()
        time.sleep(2)
        print("Поисковая строка очищена")
        inputLine.send_keys(self.input)
        print("Инпут введён в поисковую строку")
        inputLine.send_keys(Keys.ENTER)
        print("нажат энтер")

    #нахождение кол-ва карточек
    def getCount(self):  # 6
        print("6")
        print("ждём загрузки кол-ва товаров")
        WebDriverWait(self.driver, 50).until(EC.presence_of_element_located((By.XPATH, "//*[@class='goods-count']/span[1]")))
        print("кол-во товаров загружено")
        while self.driver.find_element(By.XPATH, "//*[@class='goods-count']/span[1]").text=="":
            continue
        cards_count_element = self.driver.find_element(By.XPATH, "//*[@class='goods-count']/span[1]")
        print("кол-во товаров получено")
        cards_count = cards_count_element.text.replace(" ","")
        return int(cards_count)
        # получение интового массива с ценами

    def getPrices(self):  # 10
        print("#10")
        print("ждём, пока цены загрузятся")
        WebDriverWait(self.driver, 50).until(
            EC.presence_of_element_located((By.XPATH, "//*[@class='lower-price']")))
        priceslist = self.driver.find_elements(By.XPATH, "//*[@class='lower-price']")
        print("нашли цены")
        prices = []
        print("#11")
        print("начинается обработка массива цен")
        for price in priceslist:  # 11
            prices.append(int(price.text.replace(" ", "").replace("₽", "")))
        return prices
    def getEarnings(self,driver):  # 12
        print("Получем выручку, юхуууу")
        # значение выручки получаеtся из расширения для браузера, в фоновом режиме расширение не работает, поэтому блок выручки пока надо отключить
        # а фоновый режим необходим, т.к. в обычном режиме мой ноут не тянет даже простую работу, не говорю уже о многопоточности
    def main(self):
        self.login()
        self.search()
        goods_count = self.getCount()
        prices_arr = self.getPrices()
        min_price = min(prices_arr)
        max_price = max(prices_arr)
        median_price = statistics.median(prices_arr)
        return_str = f"{goods_count},{min_price},{median_price},{max_price}"
        return return_str

a = Parser_wb("чайник")
print(a.main())
