from pages.main_page import MainPage
from pages.base_page import BasePage

class TestLogoHeader:

    def test_click_scooter_logo_open_main_page(self, driver):
        main_page = MainPage(driver)
        base_page = BasePage(driver)
        main_page.open()
        main_page.click_order_button_in_header()
        base_page.click_scooter_logo_in_header()
        assert base_page.get_current_url() == 'https://qa-scooter.praktikum-services.ru/'

    def test_click_yandex_logo_open_dzen_page(self, driver):
        main_page = MainPage(driver)
        base_page = BasePage(driver) 
        main_page.open()
        base_page.click_yandex_logo_in_header()
        base_page.switch_to_window(1)
        base_page.wait_news_text_in_dzen_page()
        assert base_page.get_current_url() == 'https://dzen.ru/?yredirect=true'
