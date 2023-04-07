from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


# A class that contains all the methods that are used in the main page of the application.
class MainPage(BasePage):
    __URL = "https://automationexercise.com/"
    __LOGOUT_BUTTON = (By.XPATH, "//ul[contains(@class, 'nav')]//a[contains(@href, 'logout')]")
    __USER_NAME = (By.XPATH, "//ul[contains(@class, 'nav')]//a[contains(text(), 'Logged in as')]/b")
    __PAGE_TITLE = (By.XPATH, "//section[contains(@id, 'slider')]//span[contains(text(), 'Automation')]")
    __PRODUCTS_BUTTON = (By.XPATH, "//ul[contains(@class, 'nav')]//a[contains(@href, 'products')]")

    def __init__(self, driver):
        super().__init__(driver)

    def open(self):
        # Opens the login page.
        super()._open_url(self.__URL)

    def get_title(self):
        return super()._get_text(self.__PAGE_TITLE)

    def expected_user_name(self, user_name):
        # Returns the expected user's name and prints a message with it.
        print("The expected user's name is: " + user_name)
        return user_name

    def get_user_name(self):
        # Returns the user's name of the logged-in user and prints a message with it.
        return super()._get_text(self.__USER_NAME)

    def is_logout_button_visible(self):
        # Returns a boolean indicating whether the logout button is visible.
        return super()._is_displayed(self.__LOGOUT_BUTTON)

    def is_main_page_url_correct(self):
        # Returns a boolean indicating whether the main page URL is correct.
        return self.__URL == self.driver.current_url

    def is_user_name_correct(self, user_name):
        # Returns a boolean indicating whether the user's name is correct.
        return user_name in super()._get_text(self.__USER_NAME)

    def is_main_page_title_correct(self, expected_title):
        # Returns a boolean indicating whether the main page title is correct.
        return super()._get_text(self.__PAGE_TITLE) == expected_title

    def open_products_page(self):
        # Opens the products page.
        super()._click(self.__PRODUCTS_BUTTON)
        if "#google_vignette" in self.driver.current_url:
            super()._go_back()
            super()._click(self.__PRODUCTS_BUTTON)
