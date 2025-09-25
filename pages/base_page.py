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

    def find_element(self, locator):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(locator))
        return self.driver.find_element(*locator)

    def click(self, locator):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(locator))
        self.find_element(locator).click()

    def text(self, locator):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(locator))
        return self.find_element(locator).text
    
    def wait_presence(self, locator):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(locator))

    def send_keys(self, locator, text):
        self.find_element(locator).clear()
        self.find_element(locator).send_keys(text)
        
    def open(self, url):
        self.driver.get(url)

    def click_accept_cookie(self):
        self.click(self.ACCEPT_COOKIE_BUTTON)

    def click_scooter_logo_in_header(self):
        self.click(self.SCOOTER_LOGO_IN_HEADER)

    def click_yandex_logo_in_header(self):
        self.click(self.YANDEX_LOGO_IN_HEADER)

    def get_current_url(self):
        return self.driver.current_url
    
    def switch_to_window(self, number):
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[number])
    
    def wait_news_text_in_dzen_page(self):
        self.wait_presence(self.NEWS_TEXT_IN_DZEN_PAGE)

    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)