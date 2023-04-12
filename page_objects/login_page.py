from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class LoginPage(BasePage):
    # A class that contains all the methods that are used in the login page.

    __URL = "https://automationexercise.com/login"
    __EMAIL_FIELD = (By.XPATH, "//div[contains(@class, 'login-form')]//input[@name='email']")
    __PASSWORD_FIELD = (By.XPATH, "//div[contains(@class, 'login-form')]//input[@name='password']")
    __LOGIN_BUTTON = (By.XPATH, "//div[contains(@class, 'login-form')]//button[@type='submit']")
    __LOGIN_FAILED_MESSAGE = (By.XPATH, "//div[contains(@class, 'login-form')]"
                                        "//p[contains(text(), 'Your email or password is incorrect!')]")

    def __init__(self, driver):
        super().__init__(driver)

    def open(self):
        # Opens the login page.
        super()._log("Opening the login page.")
        super()._open_url(self.__URL)

    def is_login_page_url_correct(self):
        # Returns a boolean indicating whether the login page URL is correct.
        super()._log("Checking if the login page URL is correct.")
        return self.__URL in super()._get_current_url()
    
    def get_login_page_url(self):
        # Returns the login page URL.
        super()._log("Getting the login page URL.")
        return self.__URL

    def execute_login(self, email, password):
        # Executes a login in the application.
        super()._log("Executing login.")
        super()._log(f"Entering email: {email}")
        super()._type(self.__EMAIL_FIELD, email)
        super()._log(f"Entering password: {password}")
        super()._type(self.__PASSWORD_FIELD, password)
        super()._log("Clicking the login button.")
        super()._click(self.__LOGIN_BUTTON)

    def is_login_failed_message_displayed(self):
        # Returns True if the login failed message is displayed; otherwise, False.
        super()._log("Checking if the login failed message is displayed.")
        is_displayed = super()._is_displayed(self.__LOGIN_FAILED_MESSAGE)
        if is_displayed:
            super()._log("Login failed message is displayed.")
        else:
            super()._log("Login failed message is not displayed.")
        return is_displayed
