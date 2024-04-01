import time

from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class AuthLocators:
    LOGIN = (By.CSS_SELECTOR, "input[name='login']")
    PASSWORD = (By.NAME, "passwd")
    BTN_SUBMIT = (By.CSS_SELECTOR, ".passport-Button")


class AuthPage(BasePage):
    def __init__(self, driver, url):
        super().__init__(driver, url)
        # self.AuthLocators = None

    def enter_login(self, login):
        search_field = self.element_is_present(AuthLocators.LOGIN)
        search_field.click()
        search_field.send_keys(login)
        return search_field

    def enter_password(self, password):
        search_field = self.element_is_present(AuthLocators.PASSWORD)
        search_field.click()
        search_field.send_keys(password)
        return search_field

    def click_submit(self):
        return self.element_is_present(AuthLocators.BTN_SUBMIT).click()

