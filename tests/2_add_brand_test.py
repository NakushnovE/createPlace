import time
import partner_data
from pages.brand_page import BrandPage
import pytest


# @pytest.mark.skip
def test_add_brand(driver):
    brand_page = BrandPage(driver, "https://admin.eda.tst.yandex-team.ru/brands/add")
    brand_page.open()
    brand_page.enter_brand_name(partner_data.name)
    brand_page.choose_brand_type()
    brand_page.choose_business_type()
    brand_page.set_rest_type()
    brand_page.set_checkbox_is_supported_stock()
    brand_page.choose_category_type()
    brand_page.set_checkbox_brand_setting_allow_cancel()
    time.sleep(2)
    brand_page.click_button_success()

    time.sleep(7)

# почемуто иногда выпадает нотификация что такой бренд уже существует