from pages.main_page import MainPage
from pages.order_page import OrderPage
import pytest


class TestOrderScooter:

    test_order_form = [
    {'button_order': MainPage.ORDER_BUTTON_IN_HEADER ,
    'first_name': 'Тест',
    'last_name': 'Тестов',
    'address': 'Москва, ул. Ленина',
    'metro_station': OrderPage.SOKOLNIKI_IN_METRO_STATION_INPUT ,
    'phone_number': '89001002030',
    'when_to_bring': OrderPage.OCTOBER_5TH_IN_WHEN_TO_BRING_INPUT ,
    'rental_period': OrderPage.ONE_DAY_IN_RENTAL_PERIOD_INPUT ,
    'color': OrderPage.BLACK_PEARL_IN_COLOR_CHECKBOXES ,
    'comment': 'Тестовый комментарий'
    },
    {'button_order': MainPage.ORDER_BUTTON_IN_HOW_DOES_THIS_WORK ,
    'first_name': 'Человек',
    'last_name': 'Человеков',
    'address': 'Москва, ул. Пушкина',
    'metro_station': OrderPage.LYBANKA_IN_METRO_STATION_INPUT ,
    'phone_number': '89001002030',
    'when_to_bring': OrderPage.OCTOBER_4TH_IN_WHEN_TO_BRING_INPUT ,
    'rental_period': OrderPage.TWO_DAYS_IN_RENTAL_PERIOD_INPUT ,
    'color': OrderPage.GRAY_HOPELESSNESS_IN_COLOR_CHECKBOXES ,
    'comment': 'Что-то написано'
    }
    ]

    @pytest.mark.parametrize('order_form', test_order_form)
    def test_order_scooter_success(self, driver, order_form):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.open_main_page()
        main_page.click_accept_cookie()
        main_page.scroll_to_element(order_form['button_order'])
        main_page.click_order_button(order_form['button_order'])
        order_page.set_first_name_input(order_form['first_name'])
        order_page.set_last_name_input(order_form['last_name'])
        order_page.set_address_input(order_form['address'])
        order_page.click_metro_station_input()
        order_page.set_metro_station_input(order_form['metro_station'])
        order_page.set_phone_number_input(order_form['phone_number'])
        order_page.click_next_button()
        order_page.click_when_to_bring_input()
        order_page.set_when_to_bring_input(order_form['when_to_bring'])
        order_page.click_rental_period_input()
        order_page.set_rental_period_input(order_form['rental_period'])
        order_page.click_color_checkboxes(order_form['color'])
        order_page.set_comment_input(order_form['comment'])
        order_page.click_order_button_in_order_form()
        order_page.click_yes_button_in_want_to_place_an_order_window()
        assert 'Заказ оформлен' in order_page.text_order_has_been_placed_text_in_modal_window()
        

