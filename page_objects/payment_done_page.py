from page_objects.base_page import BasePage

from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

class PaymentDonePage(BasePage):
    # A class that contains all the methods that are used in the payment page.

    __URL = "https://automationexercise.com/payment_done"
    __ORDER_CONFIRMATION_MESSAGE = (By.XPATH, "//p[contains(text(), 'Congratulations! Your order has been confirmed!')]")
    __DOWNLOAD_INVOICE_BUTTON = (By.XPATH, "//a[contains(@href, 'download_invoice')]")

    def __init__(self, driver):
        super().__init__(driver)

    def open(self):
        # Opens the payment page.
        super()._open_url(self.__URL)

    def is_order_confirmation_message_displayed(self):
        # Returns True if the order confirmation message is displayed; otherwise, False.
        try:
            return super()._is_displayed(self.__ORDER_CONFIRMATION_MESSAGE, 1)
        except TimeoutException:
            return False
    
    def download_invoice(self):
        # Downloads the invoice.
        super()._click(self.__DOWNLOAD_INVOICE_BUTTON)