from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


# LoggedInMainPage is a class that contains all the methods that are used in the main page of the application.
class LoggedInMainPage(BasePage):
    # The __url, __logout_button and __user_name variables are used to store the locators of the elements in the page.
    __url = "https://automationexercise.com/"
    __logout_button = (By.XPATH, "//ul[contains(@class, 'nav')]//a[contains(@href, 'logout')]")
    __user_name = (By.XPATH, "//ul[contains(@class, 'nav')]//a[contains(text(), 'Logged in as')]/b")

    # The constructor of the class receives the driver as a parameter.
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    # Public methods

    # The open method is used to open the main page of the application.
    # This method calls the open_url method of the BasePage class.
    def open(self):
        super().open_url(self.__url)

    # The expected_user_name method is used to give public access to the __user_name variable.
    def expected_user_name(self):
        return self.__user_name

    # The get_user_name method is used to get the user's name of the logged in user.
    def get_user_name(self):
        return super().get_text(self.__user_name)

    # The is_logout_button_visible method is used to check if the logout button is visible.
    def is_logout_button_visible(self):
        return super().is_displayed(self.__logout_button)
