import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="session")
def driver():
    options = Options()
    options.page_load_strategy = 'none'
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
    # driver.add_cookie({
    #     "sessionid2": "3:1702454292.5.0.1702454292349:OgABAAAAAAAxAoGwuAYCKg:9.1.2:2|4092536074.-1.0.3:1702454292|1:10373586.481206.fakesign0000000000000000000",
    #     "Session_id": "3:1704877167.5.0.1697093154088:IgABAAAAAAAwZYGwuAYCKg:4e.1.2:3|1120000000558941.0.2002.3:1697093154|5:10221759.644196._pLE-l1t997E5DrURwMmIbKxuOc",
    #     "yandex_login": "evgenij-nakus",
    #     "yandexuid": "2815074451697034318"
    # })

    # print(driver.get_cookie("yandexuid"))
    driver.maximize_window()
    yield driver
    driver.quit()