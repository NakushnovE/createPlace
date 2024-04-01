# import time
import datetime
#
# from pages.base_page import BasePage
#
#
# def test_open(driver):
#     url = BasePage(driver, "https://admin.eda.tst.yandex-team.ru/")
#     # url = BasePage(driver, "https://passport.yandex-team.ru/auth?retpath=https://admin.eda.tst.yandex-team.ru/")
#     url.setCoockies()
#     url.open()
#
#     url.getCoockies()
#     time.sleep(27)

url = "https://admin.eda.tst.yandex-team.ru/places/480600/edit"
ur = url[44:-5]

current_date = datetime.datetime.now().strftime('%d.%m.%Y 00:00')
print(current_date)