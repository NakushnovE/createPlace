import time
import datetime
import partner_data
from pages.place_page import PlacePage
import pytest

# place_id = "481043"
current_date = datetime.datetime.now().strftime('%d.%m.%Y 00:00')


@pytest.mark.skip
def test_add_place(driver):
    place_page = PlacePage(driver, "https://admin.eda.tst.yandex-team.ru/places/add")
    place_page.open()
    place_page.enter_place_name(partner_data.name)
    place_page.choose_country()
    time.sleep(3)
    place_page.choose_region()
    place_page.choose_brand(partner_data.name)
    # place_page.choose_delivery_type()
    place_page.enter_address()
    place_page.enter_phone()
    place_page.choose_phone_number_type()
    place_page.enter_email()
    time.sleep(2)
    place_page.choose_group(partner_data.name)
    place_page.enter_origin_id(partner_data.origin_id)
    place_page.enter_rating()
    # place_page.choose_sales()
    place_page.set_checkbox_service_eda()

    time.sleep(3)
    place_page.click_button_success()
    time.sleep(10)

    global place_id
    place_id = place_page.get_place_id()
    time.sleep(20)


# @pytest.mark.skip
def test_add_billing_info(driver):
    place_page = PlacePage(driver, f"https://admin.eda.tst.yandex-team.ru/places/{place_id}/edit#legal-info")
    place_page.open()
    place_page.click_billing_info()
    place_page.enter_clients_inn('7731586383')
    time.sleep(4)
    place_page.click_button_success()
#надеждее будет прописать конкретные значения в необходимых полях, а не выбирать клиента по инн




@pytest.mark.skip
def test_add_commission(driver):
    place_page = PlacePage(driver, f"https://admin.eda.tst.yandex-team.ru/places/{place_id}/edit#commission")
    place_page.open()
    time.sleep(4)
    place_page.enter_percent_commission()
    place_page.set_available_from_line(current_date)
    time.sleep(3)
    place_page.enter_ticket()
    place_page.click_save_commission()
    place_page.click_watch_draft()
    # place_page.click_accept_draft() # не работает, нужен переход на страницу


# @pytest.mark.skip
def test_add_delivery_zone(driver):
    place_page = PlacePage(driver, f"https://admin.eda.tst.yandex-team.ru/place-delivery-zones/{place_id}/add")
    place_page.open()
    place_page.enter_delivery_zone_name()
    place_page.select_zone_condition()
    place_page.choose_place_for_copy_zone()
    place_page.click_button_copy_zone()
    place_page.save_delivery_zone()


    time.sleep(27)