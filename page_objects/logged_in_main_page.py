from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class LoggedInMainPage(BasePage):
    """ A class that contains all the methods that are used in the main page of the application. """

    __URL = "https://automationexercise.com/"
    __LOGOUT_BUTTON = (By.XPATH, "//ul[contains(@class, 'nav')]//a[contains(@href, 'logout')]")
    __USER_NAME = (By.XPATH, "//ul[contains(@class, 'nav')]//a[contains(text(), 'Logged in as')]/b")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        """Opens the login page."""
        super().open_url(self.__URL)

    def expected_user_name(self, user_name):
        """
        Returns the expected user's name and prints a message with it.
        """
        print("The expected user's name is: " + user_name)
        return user_name

    def get_user_name(self):
        """
        Returns the user's name of the logged-in user and prints a message with it.
        """
        print("The user's name is: " + super()._get_text(self.__USER_NAME))
        return super()._get_text(self.__USER_NAME)

    def is_logout_button_visible(self):
        """
        Returns a boolean indicating whether the logout button is visible.
        """
        return super()._is_displayed(self.__LOGOUT_BUTTON)
