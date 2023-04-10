import time

from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage\



class ProductsPage(BasePage):
    # A class that contains all the methods that are used in the product page.

    __URL = "https://automationexercise.com/products"
    __ALL_PRODUCTS_TITLE = (By.XPATH, "//h2[contains(text(), 'All Products')]")
    __SEARCH_FIELD = (By.XPATH, "//input[@name='search']")
    __SEARCH_BUTTON = (By.XPATH, "//button[@id='submit_search']")
    __SEARCHED_PRODUCT_TITLE = (By.XPATH, "//h2[contains(text(), 'Searched Products')]")
    __PRODUCT_SEARCH_RESULTS = (
    By.XPATH, "(//div[contains(@class, 'productinfo')]//a[contains(text(), 'Add to cart')])")
    __ADDED_PRODUCT_TO_CART_MODAL = (By.XPATH, "//div[contains(@id, 'cartModal')]")
    __CONTINUE_SHOPPING_BUTTON = (
        By.XPATH, "//button[contains(text(), 'Continue Shopping')]")
    __VIEW_CART_BUTTON = (By.XPATH, "//a[contains(@href, 'view_cart')]")

    def __init__(self, driver):
        super().__init__(driver)

    def open(self):
        # Opens the product page.
        super()._open_url(self.__URL)

    def is_all_products_title_displayed(self):
        # Returns True if the product name is displayed; otherwise, False.
        return super()._is_displayed(self.__ALL_PRODUCTS_TITLE)

    def execute_product_search(self, product_name):
        # Executes a product search in the application.
        super()._type(self.__SEARCH_FIELD, product_name)
        super()._click(self.__SEARCH_BUTTON)

    def is_searched_products_title_displayed(self):
        # Returns True if the searched product is displayed; otherwise, False.
        return super()._is_displayed(self.__SEARCHED_PRODUCT_TITLE)

    def is_product_search_results_displayed(self):
        # Returns True if the searched product is displayed; otherwise, False.
        return super()._is_displayed(self.__PRODUCT_SEARCH_RESULTS)

    def add_product_to_cart(self, product_index):
        # Adds a specified product to the cart.
        xpath = f"{self.__PRODUCT_SEARCH_RESULTS[1]}[{product_index + 1}]"
        super()._click((By.XPATH, xpath))  # click add the product

    def view_cart(self):
        # Clicks the view cart button.
        super()._click(self.__VIEW_CART_BUTTON)
