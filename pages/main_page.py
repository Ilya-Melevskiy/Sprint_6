from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MainPage(BasePage):
    HOW_MUCH_DOES_IT_COST_AND_HOW_DO_I_PAY_BUTTON = [By.XPATH, "//*[@id='accordion__heading-0']"]
    I_WANT_SEVERAL_SCOOTERS_AT_ONCE_IS_THAT_POSSIBLE_BUTTON = [By.XPATH, "//*[@id='accordion__heading-1']"]
    HOW_IS_THE_RENTAL_PERIOD_CALCULATED_I_PAY_BUTTON = [By.XPATH, "//*[@id='accordion__heading-2']"]
    IS_IT_POSSIBLE_TO_ORDER_A_SCOOTER_FOR_TODAY_BUTTON = [By.XPATH, "//*[@id='accordion__heading-3']"]
    IS_IT_POSSIBLE_TO_EXTEND_AN_ORDER_OR_RETURN_THE_SCOOTER_EARLIER_BUTTON = [By.XPATH, "//*[@id='accordion__heading-4']"]
    DO_YOU_BRING_A_CHARGER_WITH_THE_SCOOTER_BUTTON = [By.XPATH, "//*[@id='accordion__heading-5']"]
    IS_IT_POSSIBLE_TO_CANCEL_AN_ORDER_BUTTON = [By.XPATH, "//*[@id='accordion__heading-6']"]
    I_LIVE_OUTSIDE_THE_MOSCOW_RING_ROAD_CAN_YOU_BRING_ME_BUTTON = [By.XPATH, "//*[@id='accordion__heading-7']"]
    HOW_MUCH_DOES_IT_COST_AND_HOW_DO_I_PAY_ACCORDEON_PANEL = [By.XPATH, "//*[@id='accordion__panel-0']//p"]
    I_WANT_SEVERAL_SCOOTERS_AT_ONCE_IS_THAT_POSSIBLE_ACCORDEON_PANEL = [By.XPATH, "//*[@id='accordion__panel-1']//p"]
    HOW_IS_THE_RENTAL_PERIOD_CALCULATED_I_PAY_ACCORDEON_PANEL = [By.XPATH, "//*[@id='accordion__panel-2']//p"]
    IS_IT_POSSIBLE_TO_ORDER_A_SCOOTER_FOR_TODAY_ACCORDEON_PANEL = [By.XPATH, "//*[@id='accordion__panel-3']//p"]
    IS_IT_POSSIBLE_TO_EXTEND_AN_ORDER_OR_RETURN_THE_SCOOTER_EARLIER_ACCORDEON_PANEL = [By.XPATH, "//*[@id='accordion__panel-4']//p"]
    DO_YOU_BRING_A_CHARGER_WITH_THE_SCOOTER_ACCORDEON_PANEL = [By.XPATH, "//*[@id='accordion__panel-5']//p"]
    IS_IT_POSSIBLE_TO_CANCEL_AN_ORDER_ACCORDEON_PANEL = [By.XPATH, "//*[@id='accordion__panel-6']//p"]
    I_LIVE_OUTSIDE_THE_MOSCOW_RING_ROAD_CAN_YOU_BRING_ME_ACCORDEON_PANEL = [By.XPATH, "//*[@id='accordion__panel-7']//p"]
    ORDER_BUTTON_IN_HEADER= [By.XPATH, "//*[@class='Button_Button__ra12g']"]
    ORDER_BUTTON_IN_HOW_DOES_THIS_WORK= [By.XPATH, "(//*[text()='Заказать'])[2]"]

    def __init__(self, driver):
        super().__init__(driver)

    def open_main_page(self):
        self.open('https://qa-scooter.praktikum-services.ru/')

    def click_question_in_accordeon(self, locator):
        self.click(locator)

    def text_response_in_accordeon(self, locator):
        return self.text(locator)

    def click_order_button(self, locator):
        self.click(locator)

    def click_order_button_in_header(self):
        self.click(self.ORDER_BUTTON_IN_HEADER)