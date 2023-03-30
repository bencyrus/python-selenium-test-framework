from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


# LoginPage is a class that contains all the methods that are used in the login page.
class LoginPage(BasePage):
    __url = "https://automationexercise.com/login"
    __email_field = (By.XPATH, "//div[contains(@class, 'login-form')]//input[@name='email']")
    __password_field = (By.XPATH, "//div[contains(@class, 'login-form')]//input[@name='password']")
    __login_button = (By.XPATH, "//div[contains(@class, 'login-form')]//button[@type='submit']")

    # The constructor of the class receives the driver as a parameter.
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    # Public methods

    # The open method is used to open the login page. This method calls the open_url method of the BasePage class.
    def open(self):
        super()._open_url(self.__url)

    # The execute_login method is used to execute a login in the application.
    # This method calls the _type and _click methods of the BasePage class.
    def execute_login(self, email, password):
        super()._type(self.__email_field, email)
        super()._type(self.__password_field, password)
        super()._click(self.__login_button)
