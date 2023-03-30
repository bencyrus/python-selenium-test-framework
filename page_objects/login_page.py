from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from page_objects.base_page import BasePage

class LoginPage(BasePage):
    __url = "https://automationexercise.com/login"
    __email_field = (By.XPATH, "//div[contains(@class, 'login-form')]//input[@name='email']")
    __password_field = (By.XPATH, "//div[contains(@class, 'login-form')]//input[@name='password']")
    __login_button = (By.XPATH, "//div[contains(@class, 'login-form')]//button[@type='submit']")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        self.driver.get(self.__url)

    def enter_email(self, email):
        self.driver.find_element_by_id(self.__email_field).clear()
        self.driver.find_element_by_id(self.__email_field).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element_by_id(self.__password_field).clear()
        self.driver.find_element_by_id(self.__password_field).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_id(self.__login_button).click()

    def execute_login(self, username, password):
        wait = WebDriverWait(self.driver, 10)

        wait.until(ec.visibility_of_element_located(self.__email_field))
        self.enter_email(username)
        wait.until(ec.visibility_of_element_located(self.__password_field))
        self.enter_password(password)
        wait.until(ec.visibility_of_element_located(self.__login_button))
        self.click_login()
