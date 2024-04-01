import time

from pages.auth_page import AuthPage


def test_auth(driver):
    auth_page = AuthPage(driver, "https://passport.yandex-team.ru/auth")
    auth_page.open()
    # time.sleep(3)
    auth_page.enter_login('')
    auth_page.enter_password("")
    auth_page.click_submit()
    time.sleep(4) #ждем загрузки страницы (оптимизиировать)

    assert auth_page.get_current_url() == "https://passport.yandex-team.ru/profile"




