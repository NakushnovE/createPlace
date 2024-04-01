from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def get_current_url(self):
        return self.driver.current_url

    def getCoockies(self):
        print(self.driver.get_cookie("yandexuid"))

    def setCoockies(self):
        # self.driver.add_cookie({"name": "sessionid2", "value": "3:1702454292.5.0.1702454292349:OgABAAAAAAAxAoGwuAYCKg:9.1.2:2|4092536074.-1.0.3:1702454292|1:10373586.481206.fakesign0000000000000000000"})
        # self.driver.add_cookie({"name": "yandex_login", "value": "evgenij-nakus"})
        # self.driver.add_cookie({"name": "Session_id", "value": "3:1704877167.5.0.1697093154088:IgABAAAAAAAwZYGwuAYCKg:4e.1.2:3|1120000000558941.0.2002.3:1697093154|5:10221759.644196._pLE-l1t997E5DrURwMmIbKxuOc"})
        # self.driver.add_cookie({"name": "yandexuid", "value": "2815074451697034318"})
        # self.driver.add_cookie({"name": "yandex_login", "value": "nphne-6ubr7gf7"})
        # self.driver.add_cookie({"name": "_yasc", "value": "YMZCrlk39i9BTZD4taEbjnd6JBk6RAWm9lU0pIwEN6iTpGOcyBfCL8g6vXCXvjXsJAfyMMua/0yRhHMU2MdzZKFF"})
        # self.driver.add_cookie({"name": "Cookie_check", "value": "1.11.CiAZugJ7tiJcnNOxX3TKIqlh5KaySupzmer_pep3g_ZEvQ.XwaOdqvjzbjWn66mIKTX8pLZw-unaJEV2WsohcGPueE"})
        # self.driver.add_cookie({"name": "sessar", "value": "CheckCookieCheckCookie"})
        self.driver.add_cookie({"name": "PHPSESSID", "value": "520stcf0q3r2lm7cncl3u37bq8"})

    def element_is_present(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

