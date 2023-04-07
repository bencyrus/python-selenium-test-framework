from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class PaymentPage(BasePage):
    # A class that contains all the methods that are used in the payment page.

    __URL = "https://automationexercise.com/payment"
    __NAME_ON_CARD_FIELD = (By.XPATH, "//input[contains(@name, 'name_on_card')]")
    __CARD_NUMBER_FIELD = (By.XPATH, "//input[contains(@name, 'card_number')]")
    __CVC_FIELD = (By.XPATH, "//input[contains(@name, 'cvc')]")
    __EXPIRATION_MONTH_FIELD = (By.XPATH, "//input[contains(@name, 'expiry_month')]")
    __EXPIRATION_YEAR_FIELD = (By.XPATH, "//input[contains(@name, 'expiry_year')]")
    __PAY_AND_CONFIRM_BUTTON = (By.XPATH, "//button[contains(text(), 'Pay and Confirm Order')]")
    __PAGE_TITLE = (By.XPATH, "//li[contains(@class, 'active')]")

    def __init__(self, driver):
        super().__init__(driver)

    def open(self):
        # Opens the payment page.
        super()._open_url(self.__URL)

    def is_payment_page_opened(self):
        # Returns True if the payment page is opened; otherwise, False.
        return super()._get_text(self.__PAGE_TITLE) == "Payment"

    def enter_payment_information(self, name_on_card, card_number, cvc, expiration_month, expiration_year):
        # Enters the payment information.
        super()._type(self.__NAME_ON_CARD_FIELD, name_on_card)
        super()._type(self.__CARD_NUMBER_FIELD, card_number)
        super()._type(self.__CVC_FIELD, cvc)
        super()._type(self.__EXPIRATION_MONTH_FIELD, expiration_month)
        super()._type(self.__EXPIRATION_YEAR_FIELD, expiration_year)

    def execute_pay_and_confirm_order(self):
        # Executes a product search in the application.
        super()._click(self.__PAY_AND_CONFIRM_BUTTON)
