from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class OrderPage(BasePage):
    FIRST_NAME_INPUT = [By.XPATH, "//*[@placeholder='* Имя']"]
    LAST_NAME_INPUT = [By.XPATH, "//*[@placeholder='* Фамилия']"]
    ADDRESS_INPUT = [By.XPATH, "//*[@placeholder='* Адрес: куда привезти заказ']"]
    METRO_STATION_INPUT = [By.XPATH, "//*[@placeholder='* Станция метро']"]
    SOKOLNIKI_IN_METRO_STATION_INPUT = [By.XPATH, "//div[text()='Сокольники']/parent::*[@class='Order_SelectOption__82bhS select-search__option']"]
    LYBANKA_IN_METRO_STATION_INPUT = [By.XPATH, "//div[text()='Лубянка']/parent::*[@class='Order_SelectOption__82bhS select-search__option']"]
    PHONE_NUMBER_INPUT = [By.XPATH, "//*[@placeholder='* Телефон: на него позвонит курьер']"]
    NEXT_BUTTON = [By.XPATH, "//button[text()='Далее' and @class='Button_Button__ra12g Button_Middle__1CSJM']"]
    WHEN_TO_BRING_INPUT = [By.XPATH, "//*[@placeholder='* Когда привезти самокат']"]
    OCTOBER_4TH_IN_WHEN_TO_BRING_INPUT = [By.XPATH, "//*[@aria-label='Choose суббота, 4-е октября 2025 г.']"]
    OCTOBER_5TH_IN_WHEN_TO_BRING_INPUT = [By.XPATH, "//*[@aria-label='Choose воскресенье, 5-е октября 2025 г.']"]
    RENTAL_PERIOD_INPUT = [By.XPATH, "//*[@class='Dropdown-root']"]
    ONE_DAY_IN_RENTAL_PERIOD_INPUT = [By.XPATH, "//div[text()='сутки']"]
    TWO_DAYS_IN_RENTAL_PERIOD_INPUT = [By.XPATH, "//div[text()='двое суток']"]
    BLACK_PEARL_IN_COLOR_CHECKBOXES = [By.XPATH, "//*[@id='black']"]
    GRAY_HOPELESSNESS_IN_COLOR_CHECKBOXES = [By.XPATH, "//*[@id='grey']"]
    COMMENT_INPUT = [By.XPATH, "//*[@placeholder='Комментарий для курьера']"]
    ORDER_BUTTON_IN_ORDER_FORM = [By.XPATH, "//button[text()='Заказать' and @class='Button_Button__ra12g Button_Middle__1CSJM']"]
    YES_BUTTON_IN_WANT_TO_PLACE_AN_ORDER_WINDOW = [By.XPATH, "//button[text()='Да']"]
    ORDER_HAS_BEEN_PLACED_TEXT_IN_MODAL_WINDOW = [By.XPATH, "//*[@class='Order_ModalHeader__3FDaJ']"]
    SCOOTER_LOGO = [By.XPATH, "//img[@alt='Scooter']"]


    def __init__(self, driver):
        super().__init__(driver)

    def set_first_name_input(self, first_name):
        self.send_keys(self.FIRST_NAME_INPUT, first_name)

    def set_last_name_input(self, last_name):
        self.send_keys(self.LAST_NAME_INPUT, last_name)

    def set_address_input(self, address):
        self.send_keys(self.ADDRESS_INPUT, address)

    def click_metro_station_input(self):
        self.click(self.METRO_STATION_INPUT)

    def set_metro_station_input(self,station_locator):
        self.click(station_locator)

    def set_phone_number_input(self, phone_number):
        self.send_keys(self.PHONE_NUMBER_INPUT, phone_number)

    def click_next_button(self):
        self.click(self.NEXT_BUTTON)

    def click_when_to_bring_input(self):
        self.click(self.WHEN_TO_BRING_INPUT)  

    def set_when_to_bring_input(self, date_locator):
        self.click(date_locator)
     
    def click_rental_period_input(self):
        self.click(self.RENTAL_PERIOD_INPUT)

    def set_rental_period_input(self, period_locator):
        self.click(period_locator)

    def click_color_checkboxes(self, color_locator):
        self.click(color_locator)   

    def set_comment_input(self, comment):
        self.send_keys(self.COMMENT_INPUT, comment)

    def click_order_button_in_order_form(self):
        self.click(self.ORDER_BUTTON_IN_ORDER_FORM)

    def click_yes_button_in_want_to_place_an_order_window(self):
        self.click(self.YES_BUTTON_IN_WANT_TO_PLACE_AN_ORDER_WINDOW)

    def text_order_has_been_placed_text_in_modal_window (self):
        return self.text(self.ORDER_HAS_BEEN_PLACED_TEXT_IN_MODAL_WINDOW)