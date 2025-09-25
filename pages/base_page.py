from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BasePage:
    ACCEPT_COOKIE_BUTTON = [By.XPATH, "//*[@class='App_CookieButton__3cvqF']"]
    SCOOTER_LOGO_IN_HEADER = (By.XPATH, "//*[@class='Header_LogoScooter__3lsAR']")
    YANDEX_LOGO_IN_HEADER = (By.XPATH, "//*[@class='Header_LogoYandex__3TSOI']")
    NEWS_TEXT_IN_DZEN_PAGE = (By.XPATH, "//*[@class='dzen-desktop--floor-title__title-2v']")

    def __init__(self, driver): 
        self.driver = driver 

    def click_accept_cookie(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.ACCEPT_COOKIE_BUTTON))
        self.driver.find_element(*self.ACCEPT_COOKIE_BUTTON).click()

    def click_scooter_logo_in_header(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.SCOOTER_LOGO_IN_HEADER))
        self.driver.find_element(*self.SCOOTER_LOGO_IN_HEADER).click()

    def click_yandex_logo_in_header(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.YANDEX_LOGO_IN_HEADER))
        self.driver.find_element(*self.YANDEX_LOGO_IN_HEADER).click()

    def get_current_url(self):
        return self.driver.current_url
    
    def switch_to_window(self, number):
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[number])
    
    def wait_news_text_in_dzen_page(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.NEWS_TEXT_IN_DZEN_PAGE))