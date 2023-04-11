from page_objects.base_page import BasePage

from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

class ShoppingCartPage(BasePage):
    # A class that contains all the methods that are used in the shopping cart page.
    __URL = "https://automationexercise.com/view_cart"
    __CART_EMPTY_MESSAGE = (By.XPATH, "//div[contains(@id, 'cart_info')]//b[contains(text(), 'Cart is empty!')]")
    __ITEM_TO_DELETE = (By.XPATH, "//table[contains(@id, 'cart_info_table')]//tr[1]//a[contains(@class, 'cart_quantity_delete')]")
    __CHECKOUT_BUTTON = (By.XPATH, "//a[contains(@class, 'check_out')]")
    __CHECKOU_MODAL_LOGIN_BUTTON = (By.XPATH, "//div[contains(@id, 'checkoutModal')]//a[contains(@href, 'login')]")

    def __init__(self, driver):
        super().__init__(driver)

    def open(self):
        # Opens the shopping cart page.
        super()._log("Opening the shopping cart page.")
        super()._open_url(self.__URL)

    def is_cart_empty(self):
        # Returns True if the cart is empty; otherwise, False.
        super()._log("Checking if the cart is empty.")
        try:
            return super()._is_displayed(self.__CART_EMPTY_MESSAGE, 1)
        except TimeoutException:
            super()._log("Cart is not empty.")
            return False
    
    def delete_item_from_cart(self):
        # Deletes an item from the cart.
        super()._log("Deleting an item from the cart.")
        super()._click(self.__ITEM_TO_DELETE)

    def proceed_to_checkout(self):
        # Clicks the checkout button.
        super()._log("Proceeding to checkout.")
        super()._click(self.__CHECKOUT_BUTTON)

    def get_shopping_cart_page_url(self):
        # Returns the shopping cart URL.
        super()._log("Getting the shopping cart page URL.")
        return self.__URL

    def is_shopping_cart_page_opened(self):
        # Returns True if the shopping cart page is opened; otherwise, False.
        super()._log("Checking if the shopping cart page is opened.")
        return self.__URL in super()._get_current_url()
