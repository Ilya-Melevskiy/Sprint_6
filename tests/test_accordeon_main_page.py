from pages.main_page import MainPage
from pages.base_page import BasePage

class TestAccordeonMainPage:

    def test_check_text_in_how_much_does_it_cost_and_how_do_i_pay_accordeon_panel(self, driver):
        main_page = MainPage(driver)
        base_page = BasePage(driver)
        main_page.open()
        base_page.click_accept_cookie()
        main_page.click_how_much_does_it_cost_and_how_do_i_pay()
        assert main_page.text_how_much_does_it_cost_and_how_do_i_pay_accordeon_panel() == \
        "Сутки — 400 рублей. Оплата курьеру — наличными или картой."

    def test_check_text_in_i_want_several_scooters_at_once_is_that_possible_accordeon_panel(self, driver):
        main_page = MainPage(driver)
        base_page = BasePage(driver)
        main_page.open()
        base_page.click_accept_cookie()
        main_page.click_i_want_several_scooters_at_once_is_that_possible_button()
        assert main_page.text_i_want_several_scooters_at_once_is_that_possible_accordeon_panel() == (
            "Пока что у нас так: один заказ — один самокат. Если хотите покататься "
            "с друзьями, можете просто сделать несколько заказов — один за другим."
        )

    def test_check_text_in_how_is_the_rental_period_calculated_i_pay_accordeon_panel(self, driver):
        main_page = MainPage(driver)
        base_page = BasePage(driver)
        main_page.open()
        base_page.click_accept_cookie()
        main_page.click_how_is_the_rental_period_calculated_i_pay_button()
        assert main_page.text_how_is_the_rental_period_calculated_i_pay_accordeon_panel() == (
        "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. "
        "Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, " 
        "суточная аренда закончится 9 мая в 20:30."
        )

    def test_check_text_in_is_it_possible_to_order_a_scooter_for_today_accordeon_panel(self, driver):
        main_page = MainPage(driver)
        base_page = BasePage(driver)
        main_page.open()
        base_page.click_accept_cookie()
        main_page.click_is_it_possible_to_order_a_scooter_for_today_button()
        assert main_page.text_is_it_possible_to_order_a_scooter_for_today_accordeon_panel() == (
        "Только начиная с завтрашнего дня. Но скоро станем расторопнее."
        )

    def test_check_text_in_it_possible_to_extend_an_order_or_return_the_scooter_earlier_accordeon_panel(self, driver):
        main_page = MainPage(driver)
        base_page = BasePage(driver)
        main_page.open()
        base_page.click_accept_cookie()
        main_page.click_is_it_possible_to_extend_an_order_or_return_the_scooter_earlier_button()
        assert main_page.text_is_it_possible_to_extend_an_order_or_return_the_scooter_earlier_accordeon_panel() == (
        "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."
        )

    def test_check_text_in_do_you_bring_a_charger_with_the_scooter_accordeon_panel(self, driver):
        main_page = MainPage(driver)
        base_page = BasePage(driver)
        main_page.open()
        base_page.click_accept_cookie()
        main_page.click_do_you_bring_a_charger_with_the_scooter_button()
        assert main_page.text_do_you_bring_a_charger_with_the_scooter_accordeon_panel() == (
        "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — "
        "даже если будете кататься без передышек и во сне. Зарядка не понадобится."
        )

    def test_check_text_in_is_it_possible_to_cancel_an_order_accordeon_panel(self, driver):
        main_page = MainPage(driver)
        base_page = BasePage(driver)
        main_page.open()
        base_page.click_accept_cookie()
        main_page.click_is_it_possible_to_cancel_an_order_button()
        assert main_page.text_is_it_possible_to_cancel_an_order_accordeon_panel() == (
        "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."
        )

    def test_check_text_in_i_live_outside_the_moscow_ring_road_can_you_bring_me_accordeon_panel(self, driver):
        main_page = MainPage(driver)
        base_page = BasePage(driver)
        main_page.open()
        base_page.click_accept_cookie()
        main_page.click_i_live_outside_the_moscow_ring_road_can_you_bring_me_button()
        assert main_page.text_i_live_outside_the_moscow_ring_road_can_you_bring_me_accordeon_panel() == (
        "Да, обязательно. Всем самокатов! И Москве, и Московской области."
        )

    

    