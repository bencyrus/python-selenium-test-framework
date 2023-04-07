from selenium import webdriver
from page_objects.login_page import LoginPage
from page_objects.main_page import MainPage
from page_objects.products_page import ProductsPage
from page_objects.shopping_cart_page import ShoppingCartPage
from page_objects.checkout_page import CheckoutPage
from page_objects.payment_page import PaymentPage
from page_objects.payment_done_page import PaymentDonePage


def before_all(context):
    # Create a webdriver instance (replace with your preferred browser)
    context.driver = webdriver.Chrome()
    context.login_page = LoginPage(context.driver)
    context.main_page = MainPage(context.driver)
    context.products_page = ProductsPage(context.driver)
    context.shopping_cart_page = ShoppingCartPage(context.driver)
    context.checkout_page = CheckoutPage(context.driver)
    context.payment_page = PaymentPage(context.driver)
    context.payment_done_page = PaymentDonePage(context.driver)


def after_all(context):
    # Quit the webdriver instance
    context.driver.quit()
