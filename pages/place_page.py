import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from tests import partner_data


class PlacePageLocator:
    PLACE_NAME = (By.CSS_SELECTOR, "#name")
    COUNTRY = (By.CSS_SELECTOR, "#country")
    OPTION_COUNTRY_IS_RUS = (By.CSS_SELECTOR, "option[value='35']")
    REGION = (By.CSS_SELECTOR, "#region")
    OPTION_REGION_IS_MOSCOW = (By.CSS_SELECTOR, "option[value='1']")
    BRAND = (By.XPATH, "//select[@id='brand']//following-sibling::span")

    ADDRESS = (By.XPATH, "//select[@id='address_input']//following-sibling::span")

    PHONE_NUMBER = (By.CSS_SELECTOR, "#phoneNumbers_0_phone_number")
    PHONE_NUMBER_TYPE = (By.CSS_SELECTOR, "#phoneNumbers_0_type")
    OPTION_PHONE_NUMBER_TYPE_IS_AUTO_CALL = (By.CSS_SELECTOR, "option[value='auto_call']")
    EMAIL = (By.CSS_SELECTOR, "#email")
    PLACE_GROUP = (By.XPATH, "//select[@id='placeGroup']//following-sibling::span")

    ORIGIN_ID = (By.CSS_SELECTOR, "#originId")
    RATING = (By.CSS_SELECTOR, "#rating")
    SALES = (By.CSS_SELECTOR, "#sales")

    CHECKBOX_SERVICE_EDA = (By.CSS_SELECTOR, "#placeServices_eda")



    BILLING_INFO = (By.CSS_SELECTOR, "a[href='#legal-info']")

    INN = (By.CSS_SELECTOR, "#billingCollection_0_inn")
    BUTTON_FIND_CLIENT = (By.XPATH, "//h4[text() = 'eats']//parent::div//a[@title = 'Найти и заполнить по ИНН']")

    COMMISSION = (By.CSS_SELECTOR, "a[data-toggle='dropdown']")
    MAIN_COMMISSION = (By.CSS_SELECTOR, "a[href='#commission']")
    PERCENT_COMMISSION = (By.CSS_SELECTOR, "#place_commission__percent_commission_line0")
    AVAILABLE_FROM = (By.CSS_SELECTOR, "#place_commission__available_from_line0")
    #выбрать дату
    TICKET = (By.CSS_SELECTOR, "#place_commission__ticket")

    BUTTON_SAVE_COMMISSION = (By.CSS_SELECTOR, "button[title='Создать новую комиссию']")
    BUTTON_WATCH_DRAFT = (By.XPATH, "//a[@title = 'Смотреть драфт']")

    BUTTON_ACCEPT_DRAFT = (By.XPATH, "//span[text() = 'Подтвердить']")

    DELIVERY_ZONE = (By.CSS_SELECTOR, "a[href^='/place-delivery-zones']")
    BUTTON_ADD_ZONE = (By.CSS_SELECTOR, ".btn-success")
    NAME_ZONE = (By.CSS_SELECTOR, "#place_delivery_zone_name")
    ZONE_CONDITION = (By.CSS_SELECTOR, "#select2-place_delivery_zone_deliveryCondition-container")
    SELECT_RESULT_ZONE_CONDITION = (By.XPATH, "//li[contains(text(), 'НД Москва: Доставка: 99р., 39р. Бесплатно от: 900р. [Д]')]")
    PLACE_FOR_COPY_ZONE = (By.XPATH, "//span[@id = 'select2-search-places-container']//parent::span")
    SELECT_RESULT_PLACE_FOR_COPY_ZONE = (By.XPATH, "//li[contains(text(), 'Сосисочная (тест интеграции)')]")
    BUTTON_COPT_ZONE = (By.XPATH, "//button[contains(text(), 'Копировать зону доставки')]")
    BUTTON_READY = (By.XPATH, "//ymaps[contains(text(), 'Готово')]")
    BUTTON_CREATE = (By.XPATH, "//button[contains(text(), 'Создать')]")

    BUTTON_EDIT_REST = (By.XPATH, "//a[contains(text(), 'Редактировать ресторан')]")


    BUTTON_CHOOSE_FILE = (By.CSS_SELECTOR, "#pictureFile_file")


    SEARCH = (By.XPATH, "//span/ul/li[text()='Пожалуйста, введите еще хотя бы 3 символa']//parent::ul//parent::span//preceding-sibling::span//input")
     # = (By.CSS_SELECTOR, "")

    BUTTON_SUCCESS = (By.XPATH, "//a[contains(text(), 'Отменить')]//following-sibling::button[contains(text(), 'Сохранить')]")

    XXX = (By.CSS_SELECTOR, f"//li[text() = '{partner_data.name}']")


class PlacePage(BasePage):
    def __init__(self, driver, url):
        super().__init__(driver, url)

    def enter_place_name(self, name):
        input_name = self.element_is_present(PlacePageLocator.PLACE_NAME)
        input_name.click()
        input_name.send_keys(name)

    def choose_country(self):
        self.element_is_present(PlacePageLocator.COUNTRY).click()
        self.element_is_present(PlacePageLocator.OPTION_COUNTRY_IS_RUS).click()

    def choose_region(self):
        self.element_is_present(PlacePageLocator.REGION).click()
        self.element_is_present(PlacePageLocator.OPTION_REGION_IS_MOSCOW).click()
        time.sleep(3)

    def choose_brand(self, name):
        self.element_is_present(PlacePageLocator.BRAND).click()
        search = self.element_is_present(PlacePageLocator.SEARCH)
        search.click()
        search.send_keys(name)
        self.element_is_present((By.XPATH, f"//li[contains(text(), '{name}')]")).click()

    def choose_delivery_type(self, delivery_type):
        pass

    def enter_address(self):
        self.element_is_present(PlacePageLocator.ADDRESS).click()
        search = self.element_is_present(PlacePageLocator.SEARCH)
        search.click()
        search.send_keys("Москва, улица Охотный Ряд, 1")
        self.element_is_present((By.XPATH, "//li[contains(text(), 'Москва, улица Охотный Ряд, 1')]")).click()

    def enter_phone(self):
        input_phone = self.element_is_present(PlacePageLocator.PHONE_NUMBER)
        input_phone.click()
        input_phone.send_keys("+73333333344")

    def choose_phone_number_type(self):
        self.element_is_present(PlacePageLocator.PHONE_NUMBER_TYPE).click()
        self.element_is_present(PlacePageLocator.OPTION_PHONE_NUMBER_TYPE_IS_AUTO_CALL).click()

    def enter_email(self):
        input_email = self.element_is_present(PlacePageLocator.EMAIL)
        input_email.click()
        input_email.send_keys("example@ya.ru")
        input_email.send_keys(Keys.ENTER)

    def choose_group(self, name):
        self.element_is_present(PlacePageLocator.PLACE_GROUP).click()
        self.element_is_present((By.XPATH, f"//li[text() = '{name}']")).click()

    def enter_origin_id(self, origin_id):
        input_origin_id = self.element_is_present(PlacePageLocator.ORIGIN_ID)
        input_origin_id.click()
        input_origin_id.send_keys(origin_id)

    def enter_rating(self):
        input_rating = self.element_is_present(PlacePageLocator.RATING)
        input_rating.click()
        input_rating.clear()
        input_rating.send_keys("3,0")

    def choose_sales(self): # Необязательно к заполнению
        self.element_is_present(PlacePageLocator.SALES).click()
        search = self.element_is_present(PlacePageLocator.SEARCH)
        search.click()
        search.send_keys("default_sales")
        search.send_keys(Keys.ENTER)

    def set_checkbox_service_eda(self):
        self.element_is_present(PlacePageLocator.CHECKBOX_SERVICE_EDA).click()

    def click_button_success(self):
        self.element_is_present(PlacePageLocator.BUTTON_SUCCESS).click()

    def get_place_id(self):
        current_url = self.get_current_url()
        place_id = current_url[44:-5]
        return place_id



    # Добавление Биллинговой информации
    def click_billing_info(self):
        self.element_is_present(PlacePageLocator.BILLING_INFO).click()

    def enter_clients_inn(self, inn):
        self.element_is_present(PlacePageLocator.INN).click()
        self.element_is_present(PlacePageLocator.INN).send_keys(inn)
        self.element_is_present(PlacePageLocator.BUTTON_FIND_CLIENT).click()
        self.element_is_present((By.XPATH, "//a[@data-client-id = '3686']")).click()





    # Добавление комиссии
    def click_commission_link(self):
        self.element_is_present(PlacePageLocator.COMMISSION).click()
        self.element_is_present(PlacePageLocator.MAIN_COMMISSION).click()

    def enter_percent_commission(self):
        self.element_is_present(PlacePageLocator.PERCENT_COMMISSION).click()
        self.element_is_present(PlacePageLocator.PERCENT_COMMISSION).send_keys('3')

    def set_available_from_line(self, current_date):
        self.element_is_present(PlacePageLocator.AVAILABLE_FROM).click()
        self.element_is_present(PlacePageLocator.AVAILABLE_FROM).clear()
        time.sleep(7)
        self.element_is_present(PlacePageLocator.AVAILABLE_FROM).send_keys(current_date)

    def enter_ticket(self):
        self.element_is_present(PlacePageLocator.TICKET).click()
        self.element_is_present(PlacePageLocator.TICKET).send_keys('EDACOMISSION-2')

    def click_save_commission(self):
        self.element_is_present(PlacePageLocator.BUTTON_SAVE_COMMISSION).click()

    def click_watch_draft(self):
        self.element_is_present(PlacePageLocator.BUTTON_WATCH_DRAFT).click()
        time.sleep(10)

    def click_accept_draft(self):
        self.element_is_present(PlacePageLocator.BUTTON_ACCEPT_DRAFT).click()



    # Добавление зоны
    def click_delivery_zone(self):
        self.element_is_present(PlacePageLocator.DELIVERY_ZONE).click()

    def enter_delivery_zone_name(self):
        self.element_is_present(PlacePageLocator.NAME_ZONE).click()
        self.element_is_present(PlacePageLocator.NAME_ZONE).send_keys("НД Москва: Доставка: 99р., 39р. Бесплатно от: 900р. [Д]")

    def select_zone_condition(self):
        self.element_is_present(PlacePageLocator.ZONE_CONDITION).click()
        self.element_is_present(PlacePageLocator.SEARCH).click()
        self.element_is_present(PlacePageLocator.SEARCH).send_keys("НД Москва: Доставка: 99р., 39р. Бесплатно от: 900р. [Д]")
        self.element_is_present(PlacePageLocator.SELECT_RESULT_ZONE_CONDITION).click()

    def choose_place_for_copy_zone(self):
        self.element_is_present(PlacePageLocator.PLACE_FOR_COPY_ZONE).click()
        self.element_is_present(PlacePageLocator.SEARCH).click()
        self.element_is_present(PlacePageLocator.SEARCH).send_keys("Сосисочная (тест интеграции)")
        self.element_is_present(PlacePageLocator.SELECT_RESULT_PLACE_FOR_COPY_ZONE).click()
        time.sleep(1)

    def click_button_copy_zone(self):
        self.element_is_present(PlacePageLocator.BUTTON_COPT_ZONE).click()
        time.sleep(1)

    def save_delivery_zone(self):
        self.element_is_present(PlacePageLocator.BUTTON_READY).click()
        self.element_is_present(PlacePageLocator.BUTTON_CREATE).click()


#//label[text() = 'Ресторан:']//following-sibling::span




