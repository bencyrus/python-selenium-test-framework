from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class LoggedInMainPage:
    __url = "https://automationexercise.com/"
    __logout_button = (By.XPATH, "//ul[contains(@class, 'nav')]//a[contains(@href, 'logout')]")
    __user_name = (By.XPATH, "//ul[contains(@class, 'nav')]//a[contains(text(), 'Logged in as')]/b")

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open(self):
        self.driver.get(self.__url)

    def expected_user_name(self):
        return self.__user_name

    def get_user_name(self):
        return self.driver.find_element_by_id(self.__user_name).text

    def is_logout_button_visible(self):
        return self.driver.find_element_by_id(self.__logout_button).is_displayed()
