from page_objects.base_page import BasePage

from selenium.webdriver.common.by import By

class ShoppingCartPage(BasePage):
    # A class that contains all the methods that are used in the shopping cart page.
    __URL = "https://automationexercise.com/view_cart"
    __CART_EMPTY_MESSAGE = (By.XPATH, "//div[contains(@id, 'cart_info')]//b[contains(text(), 'Cart is empty!')]")
    __ITEM_TO_DELETE = (By.XPATH, "//table[@id='cart_info_table']//tr[1]//a[@class='cart_quantity_delete']")

    def __init__(self, driver):
        super().__init__(driver)

    def open(self):
        # Opens the shopping cart page.
        super()._open_url(self.__URL)

    def is_cart_empty(self):
        # Returns True if the cart is empty; otherwise, False.
        return super()._is_displayed(self.__CART_EMPTY_MESSAGE)
    
    def delete_item_from_cart(self, item_name):
        # Deletes an item from the cart.
        xpath = f"//td[contains(text(), '{item_name}')]/following-sibling::td//a[contains(text(), 'Delete')]"
        super()._click((By.XPATH, xpath))