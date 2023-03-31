from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class LoginPage(BasePage):
    """A class that contains all the methods that are used in the login page."""

    __URL = "https://automationexercise.com/login"
    __EMAIL_FIELD = (By.XPATH, "//div[contains(@class, 'login-form')]//input[@name='email']")
    __PASSWORD_FIELD = (By.XPATH, "//div[contains(@class, 'login-form')]//input[@name='password']")
    __LOGIN_BUTTON = (By.XPATH, "//div[contains(@class, 'login-form')]//button[@type='submit']")
    __LOGIN_FAILED_MESSAGE = (By.XPATH, "//div[contains(@class, 'login-form')]"
                                        "//p[contains(text(), 'Your email or password is incorrect!')]")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        """Opens the login page."""
        super()._open_url(self.__URL)

    def execute_login(self, email, password):
        """Executes a login in the application."""
        super()._type(self.__EMAIL_FIELD, email)
        super()._type(self.__PASSWORD_FIELD, password)
        super()._click(self.__LOGIN_BUTTON)

    def is_login_failed_message_displayed(self):
        """Returns True if the login failed message is displayed; otherwise, False."""
        return super()._is_displayed(self.__LOGIN_FAILED_MESSAGE)
