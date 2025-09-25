from pages.main_page import MainPage
from pages.base_page import BasePage
import pytest

class TestAccordeonMainPage:

    test_accordeon=[
        {
        'question': MainPage.HOW_MUCH_DOES_IT_COST_AND_HOW_DO_I_PAY_BUTTON ,
        'response': MainPage.HOW_MUCH_DOES_IT_COST_AND_HOW_DO_I_PAY_ACCORDEON_PANEL,
        'expected_response': 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'
        },
        {
        'question': MainPage.I_WANT_SEVERAL_SCOOTERS_AT_ONCE_IS_THAT_POSSIBLE_BUTTON ,
        'response': MainPage.I_WANT_SEVERAL_SCOOTERS_AT_ONCE_IS_THAT_POSSIBLE_ACCORDEON_PANEL,
        'expected_response': ("Пока что у нас так: один заказ — один самокат. Если хотите покататься "
        "с друзьями, можете просто сделать несколько заказов — один за другим.")
        },
        {
        'question': MainPage.HOW_IS_THE_RENTAL_PERIOD_CALCULATED_I_PAY_BUTTON ,
        'response': MainPage.HOW_IS_THE_RENTAL_PERIOD_CALCULATED_I_PAY_ACCORDEON_PANEL,
        'expected_response': ("Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. "
        "Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, " 
        "суточная аренда закончится 9 мая в 20:30.")
        },
        {
        'question': MainPage.IS_IT_POSSIBLE_TO_ORDER_A_SCOOTER_FOR_TODAY_BUTTON ,
        'response': MainPage.IS_IT_POSSIBLE_TO_ORDER_A_SCOOTER_FOR_TODAY_ACCORDEON_PANEL,
        'expected_response': "Только начиная с завтрашнего дня. Но скоро станем расторопнее."
        },
        {
        'question': MainPage.IS_IT_POSSIBLE_TO_EXTEND_AN_ORDER_OR_RETURN_THE_SCOOTER_EARLIER_BUTTON ,
        'response': MainPage.IS_IT_POSSIBLE_TO_EXTEND_AN_ORDER_OR_RETURN_THE_SCOOTER_EARLIER_ACCORDEON_PANEL,
        'expected_response': 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'
        },
        {
        'question': MainPage.DO_YOU_BRING_A_CHARGER_WITH_THE_SCOOTER_BUTTON ,
        'response': MainPage.DO_YOU_BRING_A_CHARGER_WITH_THE_SCOOTER_ACCORDEON_PANEL,
        'expected_response': ("Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — "
        "даже если будете кататься без передышек и во сне. Зарядка не понадобится.")
        },
        {
        'question': MainPage.IS_IT_POSSIBLE_TO_CANCEL_AN_ORDER_BUTTON ,
        'response': MainPage.IS_IT_POSSIBLE_TO_CANCEL_AN_ORDER_ACCORDEON_PANEL,
        'expected_response': "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."
        },
        {
        'question': MainPage.I_LIVE_OUTSIDE_THE_MOSCOW_RING_ROAD_CAN_YOU_BRING_ME_BUTTON ,
        'response': MainPage.I_LIVE_OUTSIDE_THE_MOSCOW_RING_ROAD_CAN_YOU_BRING_ME_ACCORDEON_PANEL,
        'expected_response': "Да, обязательно. Всем самокатов! И Москве, и Московской области."
        }
    ]

    @pytest.mark.parametrize('accordeon', test_accordeon)
    def test_check_text_in_how_much_does_it_cost_and_how_do_i_pay_accordeon_panel(self, driver, accordeon):
        main_page = MainPage(driver)
        base_page = BasePage(driver)
        main_page.open()
        base_page.click_accept_cookie()
        main_page.click_question_in_accordeon(accordeon['question'])
        assert main_page.text_response_in_accordeon(accordeon['response']) == accordeon['expected_response']
        

    # def test_check_text_in_i_want_several_scooters_at_once_is_that_possible_accordeon_panel(self, driver):
    #     main_page = MainPage(driver)
    #     base_page = BasePage(driver)
    #     main_page.open()
    #     base_page.click_accept_cookie()
    #     main_page.click_i_want_several_scooters_at_once_is_that_possible_button()
    #     assert main_page.text_i_want_several_scooters_at_once_is_that_possible_accordeon_panel() == (
    #         "Пока что у нас так: один заказ — один самокат. Если хотите покататься "
    #         "с друзьями, можете просто сделать несколько заказов — один за другим."
    #     )

    # def test_check_text_in_how_is_the_rental_period_calculated_i_pay_accordeon_panel(self, driver):
    #     main_page = MainPage(driver)
    #     base_page = BasePage(driver)
    #     main_page.open()
    #     base_page.click_accept_cookie()
    #     main_page.click_how_is_the_rental_period_calculated_i_pay_button()
    #     assert main_page.text_how_is_the_rental_period_calculated_i_pay_accordeon_panel() == (
    #     "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. "
    #     "Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, " 
    #     "суточная аренда закончится 9 мая в 20:30."
    #     )

    # def test_check_text_in_is_it_possible_to_order_a_scooter_for_today_accordeon_panel(self, driver):
    #     main_page = MainPage(driver)
    #     base_page = BasePage(driver)
    #     main_page.open()
    #     base_page.click_accept_cookie()
    #     main_page.click_is_it_possible_to_order_a_scooter_for_today_button()
    #     assert main_page.text_is_it_possible_to_order_a_scooter_for_today_accordeon_panel() == (
    #     "Только начиная с завтрашнего дня. Но скоро станем расторопнее."
    #     )

    # def test_check_text_in_it_possible_to_extend_an_order_or_return_the_scooter_earlier_accordeon_panel(self, driver):
    #     main_page = MainPage(driver)
    #     base_page = BasePage(driver)
    #     main_page.open()
    #     base_page.click_accept_cookie()
    #     main_page.click_is_it_possible_to_extend_an_order_or_return_the_scooter_earlier_button()
    #     assert main_page.text_is_it_possible_to_extend_an_order_or_return_the_scooter_earlier_accordeon_panel() == (
    #     "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."
    #     )

    # def test_check_text_in_do_you_bring_a_charger_with_the_scooter_accordeon_panel(self, driver):
    #     main_page = MainPage(driver)
    #     base_page = BasePage(driver)
    #     main_page.open()
    #     base_page.click_accept_cookie()
    #     main_page.click_do_you_bring_a_charger_with_the_scooter_button()
    #     assert main_page.text_do_you_bring_a_charger_with_the_scooter_accordeon_panel() == (
    #     "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — "
    #     "даже если будете кататься без передышек и во сне. Зарядка не понадобится."
    #     )

    # def test_check_text_in_is_it_possible_to_cancel_an_order_accordeon_panel(self, driver):
    #     main_page = MainPage(driver)
    #     base_page = BasePage(driver)
    #     main_page.open()
    #     base_page.click_accept_cookie()
    #     main_page.click_is_it_possible_to_cancel_an_order_button()
    #     assert main_page.text_is_it_possible_to_cancel_an_order_accordeon_panel() == (
    #     "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."
    #     )

    # def test_check_text_in_i_live_outside_the_moscow_ring_road_can_you_bring_me_accordeon_panel(self, driver):
    #     main_page = MainPage(driver)
    #     base_page = BasePage(driver)
    #     main_page.open()
    #     base_page.click_accept_cookie()
    #     main_page.click_i_live_outside_the_moscow_ring_road_can_you_bring_me_button()
    #     assert main_page.text_i_live_outside_the_moscow_ring_road_can_you_bring_me_accordeon_panel() == (
    #     "Да, обязательно. Всем самокатов! И Москве, и Московской области."
    #     )

    

    