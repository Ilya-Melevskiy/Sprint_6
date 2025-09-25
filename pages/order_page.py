from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



class OrderPage:
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
        self.driver = driver 

    def set_first_name_input(self, first_name):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.FIRST_NAME_INPUT))
        self.driver.find_element(*self.FIRST_NAME_INPUT).send_keys(first_name)

    def set_last_name_input(self, last_name):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.LAST_NAME_INPUT))
        self.driver.find_element(*self.LAST_NAME_INPUT).send_keys(last_name)

    def set_address_input(self, address):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.ADDRESS_INPUT))
        self.driver.find_element(*self.ADDRESS_INPUT).send_keys(address)

    def click_metro_station_input(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.METRO_STATION_INPUT))
        self.driver.find_element(*self.METRO_STATION_INPUT).click()

    def set_metro_station_input(self,locator):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    def set_phone_number_input(self, phone_number):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.PHONE_NUMBER_INPUT))
        self.driver.find_element(*self.PHONE_NUMBER_INPUT).send_keys(phone_number)

    def click_next_button(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.NEXT_BUTTON))
        self.driver.find_element(*self.NEXT_BUTTON).click()

    def click_when_to_bring_input(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.WHEN_TO_BRING_INPUT))
        self.driver.find_element(*self.WHEN_TO_BRING_INPUT).click()  

    def set_when_to_bring_input(self, locator):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()
     
    def click_rental_period_input(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.RENTAL_PERIOD_INPUT))
        self.driver.find_element(*self.RENTAL_PERIOD_INPUT).click()

    def set_rental_period_input(self, locator):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    def click_color_checkboxes(self, locator):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()   

    def set_comment_input(self, comment):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.COMMENT_INPUT))
        self.driver.find_element(*self.COMMENT_INPUT).send_keys(comment)

    def click_order_button_in_order_form(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.ORDER_BUTTON_IN_ORDER_FORM))
        self.driver.find_element(*self.ORDER_BUTTON_IN_ORDER_FORM).click()

    def click_yes_button_in_want_to_place_an_order_window(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.YES_BUTTON_IN_WANT_TO_PLACE_AN_ORDER_WINDOW))
        self.driver.find_element(*self.YES_BUTTON_IN_WANT_TO_PLACE_AN_ORDER_WINDOW).click()

    def text_order_has_been_placed_text_in_modal_window (self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.ORDER_HAS_BEEN_PLACED_TEXT_IN_MODAL_WINDOW))
        return self.driver.find_element(*self.ORDER_HAS_BEEN_PLACED_TEXT_IN_MODAL_WINDOW).text