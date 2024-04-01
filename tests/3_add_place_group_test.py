import pytest

from pages.place_group_page import PlaceGroupPage
import time
import partner_data


# @pytest.mark.skip
def test_add_group(driver):
    group_page = PlaceGroupPage(driver, "https://admin.eda.tst.yandex-team.ru/place_groups/add")
    group_page.open()
    group_page.enter_group_name(partner_data.name)
    group_page.choose_parser_menu()
    group_page.choose_integration_engine()
    group_page.choose_use_client_categories()
    group_page.set_checkbox_use_client_categories_sync_with_menu()
    group_page.set_checkbox_updating_to_terminal_status()
    group_page.enter_host_of_integration_engine(partner_data.host)
    group_page.enter_client_id_of_integration_engine(partner_data.client_id)
    group_page.enter_client_secret_of_integration_engine(partner_data.client_secret)
    group_page.enter_group_scope_of_integration_engine()
    group_page.set_checkbox_order_update()
    group_page.choose_cancel_method()
    group_page.choose_api_version_of_integration_engine()
    group_page.set_checkbox_should_update_catchweight_order()
    group_page.set_checkbox_dont_stop_update()
    group_page.set_checkbox_taken_by_courier_notification()
    group_page.set_checkbox_delivring_notification()
    group_page.set_checkbox_retries()
    group_page.enter_client_id_of_menu_parser(partner_data.client_id)
    group_page.enter_client_secret_of_menu_parser(partner_data.client_secret)
    group_page.enter_group_scope_of_menu_parser()
    group_page.enter_host_of_menu_parser(partner_data.host)
    group_page.set_checkbox_move_dishes_to_others_categories()
    group_page.set_checkbox_support_catch_weight_goods()
    group_page.choose_api_version_of_menu_parser()
    time.sleep(2)
    group_page.click_button_success()

    time.sleep(7)

    # Поправить версии апи для парсинга и движка заказов