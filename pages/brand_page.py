from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class BrandsPageLocators:
    BRAND_NAME = (By.CSS_SELECTOR, "#brand_name")
    BRAND_TYPE = (By.CSS_SELECTOR, "#brand_brandType")
    OPTION_BRAND_TYPE_IS_NOT_REST = (By.CSS_SELECTOR, "option[value='not_restaurant']")
    BUSINESS_TYPE = (By.CSS_SELECTOR, "#brand_businessType")
    OPTION_BUSINESS_TYPE_IS_SHOP = (By.CSS_SELECTOR, "option[value='shop']")
    REST_TYPE = (By.CSS_SELECTOR, "#brand_types")
    DELETE_REST_TYPE = (By.CSS_SELECTOR, ".select2-selection__choice__remove")
    OPTION_REST_TYPE_IS_SHOP = (By.CSS_SELECTOR, "option[value='41']")
    IS_STOCK_SUPPORTED = (By.CSS_SELECTOR, "#brand_isStockSupported")
    CATEGORY_TYPE = (By.CSS_SELECTOR, "#brand_categoryType")
    OPTION_CATEGORY_TYPE_IS_CLIENT = (By.CSS_SELECTOR, "option[value='client']")
    BRAND_SETTINGS_ALLOW_CANCEL = (By.CSS_SELECTOR, "#brand_brandSettings_allow_cancel")

    BUTTON_SUCCESS = (By.CSS_SELECTOR, ".btn-success")


class BrandPage(BasePage):
    def __init__(self, driver, url):
        super().__init__(driver, url)

    def enter_brand_name(self, name):
        input_brand_name = self.element_is_present(BrandsPageLocators.BRAND_NAME)
        input_brand_name.click()
        input_brand_name.send_keys(name)

    def choose_brand_type(self):
        self.element_is_present(BrandsPageLocators.BRAND_TYPE).click()
        self.element_is_present(BrandsPageLocators.OPTION_BRAND_TYPE_IS_NOT_REST).click()

    def choose_business_type(self):
        self.element_is_present(BrandsPageLocators.BUSINESS_TYPE).click()
        self.element_is_present(BrandsPageLocators.OPTION_BUSINESS_TYPE_IS_SHOP).click()

    def set_rest_type(self):
        self.element_is_present(BrandsPageLocators.DELETE_REST_TYPE).click()
        self.element_is_present(BrandsPageLocators.OPTION_REST_TYPE_IS_SHOP).click()

    def set_checkbox_is_supported_stock(self):
        self.element_is_present(BrandsPageLocators.IS_STOCK_SUPPORTED).click()

    def choose_category_type(self):
        self.element_is_present(BrandsPageLocators.CATEGORY_TYPE).click()
        self.element_is_present(BrandsPageLocators.OPTION_CATEGORY_TYPE_IS_CLIENT).click()

    def set_checkbox_brand_setting_allow_cancel(self):
        self.element_is_present(BrandsPageLocators.BRAND_SETTINGS_ALLOW_CANCEL).click()

    def click_button_success(self):
        self.element_is_present(BrandsPageLocators.BUTTON_SUCCESS).click()