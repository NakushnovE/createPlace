from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time
from pages.base_page import BasePage


class PlaceGroupPageLocators:
    PLACE_GROUP_NAME = (By.CSS_SELECTOR, "#place_group_name")
    MENU_PARSER_NAME = (By.XPATH, "//select[@id = 'place_group_menuParserName']//following-sibling::span")
    OPTION_MENU_PARSER_NAME_IS_RETAIL = (By.XPATH, "//li[text()='Retail API']")
    INTEGRATION_ENGINE = (By.XPATH, "//select[@id = 'place_group_integrationEngine']//following-sibling::span")
    OPTION_INTEGRATION_ENGINE_IS_RETAIL = (By.XPATH, "//li[text()='YandexEdaRetailEngine']")
    USE_CLIENT_CATEGORIES = (By.CSS_SELECTOR, "#place_group_integrationProcessToUseClientCategories")
    OPTION_USE_CLIENT_CATEGORIES_IS_Y = (By.XPATH, "//select[@id='place_group_integrationProcessToUseClientCategories']//option[text()='Да']")
    USE_CLIENT_CATEGORIES_SYNCHRONIZATION_WITH_MENU = (By.CSS_SELECTOR, "#place_group_useClientCategoriesSynchronizationWithMenu")
    UPDATING_TO_TERMINAL_STATUS = (By.CSS_SELECTOR, "#place_group_updatingToTerminalStatus")

    HOST_OF_INTEGRATION_ENGINE = (By.CSS_SELECTOR, "#place_group_vendorHost")
    CLIENT_ID_OF_INTEGRATION_ENGINE = (By.CSS_SELECTOR, "#place_group_clientId")
    CLIENT_SECRET_OF_INTEGRATION_ENGINE = (By.CSS_SELECTOR, "#place_group_clientSecret")
    GROUP_SCOPE_OF_INTEGRATION_ENGINE = (By.CSS_SELECTOR, "#place_group_scope")
    CHECKBOX_ORDER_UPDATE = (By.CSS_SELECTOR, "#place_group_orderUpdate")
    CANCEL_METHOD = (By.CSS_SELECTOR, "#place_group_cancelMethod")
    OPTION_CANCEL_METHOD_IS_PUT = (By.CSS_SELECTOR, "option[value='PUT']")
    API_VERSION_OF_INTEGRATION_ENGINE = (By.CSS_SELECTOR, "#place_group_apiVersion")
    OPTION_API_VERSION_OF_INTEGRATION_ENGINE_IS_V2 = (By.XPATH, "//select[@id='place_group_apiVersion']//child::option[@value='v2']")
    CHECKBOX_SHOULD_UPDATE_CATCHWEIGHT_ORDER = (By.CSS_SELECTOR, "#place_group_shouldUpdateCatchweightOrder")
    CHECKBOX_DONT_STOP_UPDATE = (By.CSS_SELECTOR, "#place_group_dontStopUpdateOrderWithoutItem")
    CHECKBOX_TAKEN_BY_COURIER_NOTIFICATION = (By.CSS_SELECTOR, "#place_group_orderTakenByCourierNotificationEnabled")
    CHECKBOX_DELIVERING_NOTIFICATION = (By.CSS_SELECTOR, "#place_group_orderDeliveringNotificationEnabled")
    CHECKBOX_RETRIES_ENABLED = (By.CSS_SELECTOR, "#place_group_isSendOrderRetriesEnabled")

    CLIENT_ID_OF_MENU_PARSER = (By.CSS_SELECTOR, "#place_group_menuParserClientId")
    CLIENT_SECRET_OF_MENU_PARSER = (By.CSS_SELECTOR, "#place_group_menuParserClientSecret")
    GROUP_SCOPE_OF_MENU_PARSER = (By.CSS_SELECTOR, "#place_group_menuParserScope")
    HOST_OF_MENU_PARSER = (By.CSS_SELECTOR, "#place_group_menuParserVendorHost")
    CHECKBOX_MOVE_DISHES_TO_OTHERS_CATEGORIES = (By.CSS_SELECTOR, "#place_group_menuParserMoveDishesToOthersCategory")
    CHECKBOX_SUPPORT_CATCH_WEIGHT_GOODS = (By.CSS_SELECTOR, "#place_group_menuParserSupportCatchWeightGoods")
    API_VERSION_OF_MENU_PARSER = (By.CSS_SELECTOR, "#place_group_menuParserApiVersion")
    OPTION_API_VERSION_OF_MENU_PARSER_IS_V1 = (By.XPATH, "//select[@id='place_group_menuParserApiVersion']//child::option[@value='v1']")

    BUTTON_SUCCESS = (By.CSS_SELECTOR, ".btn-success")


class PlaceGroupPage(BasePage):
    def __init__(self, driver, url):
        super().__init__(driver, url)

    def enter_group_name(self, name):
        input_group_name = self.element_is_present(PlaceGroupPageLocators.PLACE_GROUP_NAME)
        input_group_name.click()
        input_group_name.send_keys(name)

    def choose_parser_menu(self):
        self.element_is_present(PlaceGroupPageLocators.MENU_PARSER_NAME).click()
        self.element_is_present(PlaceGroupPageLocators.OPTION_MENU_PARSER_NAME_IS_RETAIL).click()

    def choose_integration_engine(self):
        self.element_is_present(PlaceGroupPageLocators.INTEGRATION_ENGINE).click()
        self.element_is_present(PlaceGroupPageLocators.OPTION_INTEGRATION_ENGINE_IS_RETAIL).click()

    def choose_use_client_categories(self):
        self.element_is_present(PlaceGroupPageLocators.USE_CLIENT_CATEGORIES).click()
        self.element_is_present(PlaceGroupPageLocators.OPTION_USE_CLIENT_CATEGORIES_IS_Y).click()

    def set_checkbox_use_client_categories_sync_with_menu(self):
        self.element_is_present(PlaceGroupPageLocators.USE_CLIENT_CATEGORIES_SYNCHRONIZATION_WITH_MENU).click()

    def set_checkbox_updating_to_terminal_status(self):
        self.element_is_present(PlaceGroupPageLocators.UPDATING_TO_TERMINAL_STATUS).click()

    def enter_host_of_integration_engine(self, host):
        input_integration_host = self.element_is_present(PlaceGroupPageLocators.HOST_OF_INTEGRATION_ENGINE)
        input_integration_host.click()
        input_integration_host.send_keys(host)

    def enter_client_id_of_integration_engine(self, client_id):
        input_client_id = self.element_is_present(PlaceGroupPageLocators.CLIENT_ID_OF_INTEGRATION_ENGINE)
        input_client_id.click()
        input_client_id.send_keys(client_id)

    def enter_client_secret_of_integration_engine(self, client_secret):
        input_client_secret = self.element_is_present(PlaceGroupPageLocators.CLIENT_SECRET_OF_INTEGRATION_ENGINE)
        input_client_secret.click()
        input_client_secret.send_keys(client_secret)

    def enter_group_scope_of_integration_engine(self):
        input_group_scope = self.element_is_present(PlaceGroupPageLocators.GROUP_SCOPE_OF_INTEGRATION_ENGINE)
        input_group_scope.click()
        input_group_scope.send_keys("read write")

    def set_checkbox_order_update(self):
        self.element_is_present(PlaceGroupPageLocators.CHECKBOX_ORDER_UPDATE).click()

    def choose_cancel_method(self):
        self.element_is_present(PlaceGroupPageLocators.CANCEL_METHOD).click()
        self.element_is_present(PlaceGroupPageLocators.OPTION_CANCEL_METHOD_IS_PUT).click()

    def choose_api_version_of_integration_engine(self):
        self.element_is_present(PlaceGroupPageLocators.API_VERSION_OF_INTEGRATION_ENGINE).click()
        self.element_is_present(PlaceGroupPageLocators.OPTION_API_VERSION_OF_INTEGRATION_ENGINE_IS_V2).click()

    def set_checkbox_should_update_catchweight_order(self):
        self.element_is_present(PlaceGroupPageLocators.CHECKBOX_SHOULD_UPDATE_CATCHWEIGHT_ORDER).click()

    def set_checkbox_dont_stop_update(self):
        self.element_is_present(PlaceGroupPageLocators.CHECKBOX_DONT_STOP_UPDATE).click()

    def set_checkbox_taken_by_courier_notification(self):
        self.element_is_present(PlaceGroupPageLocators.CHECKBOX_TAKEN_BY_COURIER_NOTIFICATION).click()

    def set_checkbox_delivring_notification(self):
        self.element_is_present(PlaceGroupPageLocators.CHECKBOX_DELIVERING_NOTIFICATION).click()

    def set_checkbox_retries(self):
        self.element_is_present(PlaceGroupPageLocators.CHECKBOX_RETRIES_ENABLED).click()

    def enter_client_id_of_menu_parser(self, client_id):
        input_client_id = self.element_is_present(PlaceGroupPageLocators.CLIENT_ID_OF_MENU_PARSER)
        input_client_id.click()
        input_client_id.send_keys(client_id)

    def enter_client_secret_of_menu_parser(self, client_secret):
        input_client_secret = self.element_is_present(PlaceGroupPageLocators.CLIENT_SECRET_OF_MENU_PARSER)
        input_client_secret.click()
        input_client_secret.send_keys(client_secret)

    def enter_group_scope_of_menu_parser(self):
        input_group_scope = self.element_is_present(PlaceGroupPageLocators.GROUP_SCOPE_OF_MENU_PARSER)
        input_group_scope.click()
        input_group_scope.send_keys("read write")

    def enter_host_of_menu_parser(self, host):
        input_host = self.element_is_present(PlaceGroupPageLocators.HOST_OF_MENU_PARSER)
        input_host.click()
        input_host.send_keys(host)

    def set_checkbox_move_dishes_to_others_categories(self):
        self.element_is_present(PlaceGroupPageLocators.CHECKBOX_MOVE_DISHES_TO_OTHERS_CATEGORIES).click()

    def set_checkbox_support_catch_weight_goods(self):
        self.element_is_present(PlaceGroupPageLocators.CHECKBOX_SUPPORT_CATCH_WEIGHT_GOODS).click()

    def choose_api_version_of_menu_parser(self):
        self.element_is_present(PlaceGroupPageLocators.API_VERSION_OF_MENU_PARSER).click()
        self.element_is_present(PlaceGroupPageLocators.OPTION_API_VERSION_OF_MENU_PARSER_IS_V1).click()

    def click_button_success(self):
        self.element_is_present(PlaceGroupPageLocators.BUTTON_SUCCESS).click()

