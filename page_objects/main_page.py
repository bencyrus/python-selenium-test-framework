from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class MainPage(BasePage):
    # A class that contains all the methods that are used in the main page of the application.
    __URL = "https://automationexercise.com/"
    __LOGIN_BUTTON = (By.XPATH, "//ul[contains(@class, 'nav')]//a[contains(@href, 'login')]")
    __LOGOUT_BUTTON = (By.XPATH, "//ul[contains(@class, 'nav')]//a[contains(@href, 'logout')]")
    __USER_NAME = (By.XPATH, "//ul[contains(@class, 'nav')]//a[contains(text(), 'Logged in as')]/b")
    __PAGE_TITLE = (By.XPATH, "//section[contains(@id, 'slider')]//span[contains(text(), 'Automation')]")
    __PRODUCTS_BUTTON = (By.XPATH, "//ul[contains(@class, 'nav')]//a[contains(@href, 'products')]")

    def __init__(self, driver):
        super().__init__(driver)

    def open(self):
        # Opens the main page.
        super()._log("Opening the main page.")
        super()._open_url(self.__URL)

    def is_logout_button_visible(self):
        # Returns a boolean indicating whether the logout button is visible.
        super()._log("Checking if the logout button is visible.")
        return super()._is_displayed(self.__LOGOUT_BUTTON)
    
    def get_main_page_url(self):
        # Returns the main page URL.
        super()._log("Getting the main page URL.")
        return self.__URL

    def is_main_page_url_correct(self):
        # Returns a boolean indicating whether the main page URL is correct.
        super()._log("Checking if the main page URL is correct.")
        return self.__URL == super()._get_current_url()
    
    def get_user_name(self):
        # Returns the user name.
        super()._log("Getting the user name from the main page.")
        return super()._get_text(self.__USER_NAME)

    def is_user_name_correct(self, user_name):
        # Returns a boolean indicating whether the user's name is correct.
        super()._log(f"Checking if the user name '{user_name}' is correct.")
        return user_name in super()._get_text(self.__USER_NAME)
    
    def get_main_page_title(self):
        # Returns the main page title.
        super()._log("Getting the main page title.")
        return super()._get_text(self.__PAGE_TITLE)

    def is_main_page_title_correct(self, expected_title):
        # Returns a boolean indicating whether the main page title is correct.
        super()._log(f"Checking if the main page title is '{expected_title}'.")
        return super()._get_text(self.__PAGE_TITLE) == expected_title

    def open_products_page(self):
        # Opens the products page.
        super()._log("Opening the products page.")
        super()._click(self.__PRODUCTS_BUTTON)
        
        if "#google_vignette" in super()._get_current_url():
            super()._log("Google Ads encountered. Going back and trying again.")
            super()._go_back()
            super()._log("Opening the products page.")
            super()._click(self.__PRODUCTS_BUTTON)

    def open_login_page(self):
        # Opens the login page.
        super()._log("Opening the login page.")
        super()._click(self.__LOGIN_BUTTON)
        
        if "#google_vignette" in super()._get_current_url():
            super()._log("Google Ads encountered. Going back and trying again.")
            super()._go_back()
            super()._log("Opening the login page.")
            super()._click(self.__LOGIN_BUTTON)