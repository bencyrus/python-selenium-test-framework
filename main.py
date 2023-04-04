from selenium import webdriver
from tests.test_login_page import TestLoginPage
from tests.test_product_page import TestProductPage
from tests.test_checkout_page import TestCheckoutPage
from tests.test_payment_page import TestPaymentPage
from tests.test_payment_done_page import TestPaymentDonePage

import time

if __name__ == "__main__":

    login_test = TestLoginPage() # create an instance of the TestLoginPage class
    product_test = TestProductPage() # create an instance of the TestProductPage class
    checkout_test = TestCheckoutPage() # create an instance of the TestCheckoutPage class
    payment_test = TestPaymentPage() # create an instance of the TestPaymentPage class
    payment_done_test = TestPaymentDonePage() # create an instance of the TestPaymentDonePage class
    
    with webdriver.Chrome() as driver: # create a Chrome driver instance
        # Run fail login test
        login_test.test_login_with_invalid_credentials(driver) # run the test_login_with_invalid_credentials method
        # Run success login test
        login_test.test_login_with_valid_credentials(driver) # run the test_login_with_valid_credentials method
        # Run all products displayed test
        product_test.test_all_products_displayed(driver) # run the test_all_products_displayed method
        # Run search product test
        product_test.test_search_product(driver) # run the test_search_product method
        # Run add product to cart test
        product_test.test_add_product_to_cart(driver) # run the test_add_product_to_cart method
        # Run remove product from cart test
        product_test.test_remove_product_from_cart(driver) # run the test_remove_product_from_cart method
        # Run checkout test
        product_test.test_checkout(driver) # run the test_checkout method
        # Run place order test
        checkout_test.test_execute_place_order(driver) # run the test_execute_place_order method
        # Run payment test
        payment_test.test_payment(driver) # run the test_payment method
        # Run payment done test
        payment_done_test.test_payment_done(driver) # run the test_payment_done method

        time.sleep(5) # wait 5 seconds before closing the browser
