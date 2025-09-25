from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class MainPage:
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
        self.driver = driver 

    def open(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
    

    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def click_question_in_accordeon(self, locator):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    # def click_i_want_several_scooters_at_once_is_that_possible_button(self):
    #     WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.I_WANT_SEVERAL_SCOOTERS_AT_ONCE_IS_THAT_POSSIBLE_BUTTON))
    #     self.driver.find_element(*self.I_WANT_SEVERAL_SCOOTERS_AT_ONCE_IS_THAT_POSSIBLE_BUTTON).click()

    # def click_how_is_the_rental_period_calculated_i_pay_button(self):
    #     WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.HOW_IS_THE_RENTAL_PERIOD_CALCULATED_I_PAY_BUTTON))
    #     self.driver.find_element(*self.HOW_IS_THE_RENTAL_PERIOD_CALCULATED_I_PAY_BUTTON).click()

    # def click_is_it_possible_to_order_a_scooter_for_today_button(self):
    #     WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.IS_IT_POSSIBLE_TO_ORDER_A_SCOOTER_FOR_TODAY_BUTTON))
    #     self.driver.find_element(*self.IS_IT_POSSIBLE_TO_ORDER_A_SCOOTER_FOR_TODAY_BUTTON).click()

    # def click_is_it_possible_to_extend_an_order_or_return_the_scooter_earlier_button(self):
    #     WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.IS_IT_POSSIBLE_TO_EXTEND_AN_ORDER_OR_RETURN_THE_SCOOTER_EARLIER_BUTTON))
    #     self.driver.find_element(*self.IS_IT_POSSIBLE_TO_EXTEND_AN_ORDER_OR_RETURN_THE_SCOOTER_EARLIER_BUTTON).click()

    # def click_do_you_bring_a_charger_with_the_scooter_button(self):
    #     WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.DO_YOU_BRING_A_CHARGER_WITH_THE_SCOOTER_BUTTON))
    #     self.driver.find_element(*self.DO_YOU_BRING_A_CHARGER_WITH_THE_SCOOTER_BUTTON).click()

    # def click_is_it_possible_to_cancel_an_order_button(self):
    #     WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.IS_IT_POSSIBLE_TO_CANCEL_AN_ORDER_BUTTON))
    #     self.driver.find_element(*self.IS_IT_POSSIBLE_TO_CANCEL_AN_ORDER_BUTTON).click()

    # def click_i_live_outside_the_moscow_ring_road_can_you_bring_me_button(self):
    #     WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.I_LIVE_OUTSIDE_THE_MOSCOW_RING_ROAD_CAN_YOU_BRING_ME_BUTTON))
    #     self.driver.find_element(*self.I_LIVE_OUTSIDE_THE_MOSCOW_RING_ROAD_CAN_YOU_BRING_ME_BUTTON).click()

    def text_response_in_accordeon(self, locator):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))
        text_in_accordeon_panel = self.driver.find_element(*locator).text
        return text_in_accordeon_panel 

    # def text_i_want_several_scooters_at_once_is_that_possible_accordeon_panel(self):
    #     WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.I_WANT_SEVERAL_SCOOTERS_AT_ONCE_IS_THAT_POSSIBLE_ACCORDEON_PANEL))
    #     text_in_accordeon_panel = self.driver.find_element(*self.I_WANT_SEVERAL_SCOOTERS_AT_ONCE_IS_THAT_POSSIBLE_ACCORDEON_PANEL).text
    #     return text_in_accordeon_panel 
    
    # def text_how_is_the_rental_period_calculated_i_pay_accordeon_panel(self):
    #     WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.HOW_IS_THE_RENTAL_PERIOD_CALCULATED_I_PAY_ACCORDEON_PANEL))
    #     text_in_accordeon_panel = self.driver.find_element(*self.HOW_IS_THE_RENTAL_PERIOD_CALCULATED_I_PAY_ACCORDEON_PANEL).text
    #     return text_in_accordeon_panel

    # def text_is_it_possible_to_order_a_scooter_for_today_accordeon_panel(self):
    #     WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.IS_IT_POSSIBLE_TO_ORDER_A_SCOOTER_FOR_TODAY_ACCORDEON_PANEL))
    #     text_in_accordeon_panel = self.driver.find_element(*self.IS_IT_POSSIBLE_TO_ORDER_A_SCOOTER_FOR_TODAY_ACCORDEON_PANEL).text
    #     return text_in_accordeon_panel 

    # def text_is_it_possible_to_extend_an_order_or_return_the_scooter_earlier_accordeon_panel(self):
    #     WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.IS_IT_POSSIBLE_TO_EXTEND_AN_ORDER_OR_RETURN_THE_SCOOTER_EARLIER_ACCORDEON_PANEL))
    #     text_in_accordeon_panel = self.driver.find_element(*self.IS_IT_POSSIBLE_TO_EXTEND_AN_ORDER_OR_RETURN_THE_SCOOTER_EARLIER_ACCORDEON_PANEL).text
    #     return text_in_accordeon_panel 
    
    # def text_do_you_bring_a_charger_with_the_scooter_accordeon_panel(self):
    #     WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.DO_YOU_BRING_A_CHARGER_WITH_THE_SCOOTER_ACCORDEON_PANEL))
    #     text_in_accordeon_panel = self.driver.find_element(*self.DO_YOU_BRING_A_CHARGER_WITH_THE_SCOOTER_ACCORDEON_PANEL).text
    #     return text_in_accordeon_panel

    # def text_is_it_possible_to_cancel_an_order_accordeon_panel(self):
    #     WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.IS_IT_POSSIBLE_TO_CANCEL_AN_ORDER_ACCORDEON_PANEL))
    #     text_in_accordeon_panel = self.driver.find_element(*self.IS_IT_POSSIBLE_TO_CANCEL_AN_ORDER_ACCORDEON_PANEL).text
    #     return text_in_accordeon_panel

    # def text_i_live_outside_the_moscow_ring_road_can_you_bring_me_accordeon_panel(self):
    #     WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.I_LIVE_OUTSIDE_THE_MOSCOW_RING_ROAD_CAN_YOU_BRING_ME_ACCORDEON_PANEL))
    #     text_in_accordeon_panel = self.driver.find_element(*self.I_LIVE_OUTSIDE_THE_MOSCOW_RING_ROAD_CAN_YOU_BRING_ME_ACCORDEON_PANEL).text
    #     return text_in_accordeon_panel

    def click_order_button(self, locator):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    def click_order_button_in_header(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.ORDER_BUTTON_IN_HEADER))
        self.driver.find_element(*self.ORDER_BUTTON_IN_HEADER).click()