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
        super()._log("Opening the payment page.")
        super()._open_url(self.__URL)

    def get_page_title(self):
        # Returns the payment page title.
        super()._log("Getting the payment page title.")
        return super()._get_text(self.__PAGE_TITLE)

    def is_payment_page_opened(self):
        # Returns True if the payment page is opened; otherwise, False.
        super()._log("Checking if the payment page is opened.")
        return super()._get_text(self.__PAGE_TITLE) == "Payment"

    def enter_payment_information(self, name_on_card, card_number, cvc, expiration_month, expiration_year):
        # Enters the payment information.
        super()._log("Entering payment information.")
        super()._log(f"Entering name on card: {name_on_card}")
        super()._type(self.__NAME_ON_CARD_FIELD, name_on_card)
        super()._log(f"Entering card number: {card_number}")
        super()._type(self.__CARD_NUMBER_FIELD, card_number)
        super()._log(f"Entering CVC: {cvc}")
        super()._type(self.__CVC_FIELD, cvc)
        super()._log(f"Entering expiration month: {expiration_month}")
        super()._type(self.__EXPIRATION_MONTH_FIELD, expiration_month)
        super()._log(f"Entering expiration year: {expiration_year}")
        super()._type(self.__EXPIRATION_YEAR_FIELD, expiration_year)

    def execute_pay_and_confirm_order(self):
        # Executes a product search in the application.
        super()._log("Clicking the 'Pay and Confirm Order' button.")
        super()._click(self.__PAY_AND_CONFIRM_BUTTON)
