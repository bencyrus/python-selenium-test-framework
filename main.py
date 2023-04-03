from selenium import webdriver
from tests.test_login_page import TestLoginPage
from tests.test_product_page import TestProductPage

if __name__ == "__main__":

    login_test = TestLoginPage() # create an instance of the TestLoginPage class
    product_test = TestProductPage() # create an instance of the TestProductPage class
    
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
