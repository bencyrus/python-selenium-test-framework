from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage

class CheckoutPage(BasePage):
    # A class that contains all the methods that are used in the checkout page.

    __URL = "https://automationexercise.com/checkout"
    __PLACE_ORDER_BUTTON = (By.XPATH, "//section[contains(@id, 'cart_items')]//a[contains(@href, 'payment')]")

    def __init__(self, driver):
        super().__init__(driver)

    def open(self):
        # Opens the checkout page.
        super()._open_url(self.__URL)

    def execute_place_order(self):
        # Executes a product search in the application.
        super()._scroll_to_element(self.__PLACE_ORDER_BUTTON)
        super()._click(self.__PLACE_ORDER_BUTTON)