from selenium import webdriver
from tests.test_login_page import TestLoginPage
from tests.test_product_page import TestProductPage

if __name__ == "__main__":
    
    # Run the login tests
    login_test = TestLoginPage() # create an instance of the TestLoginPage class
    
    # Run success login test
    with webdriver.Chrome() as driver: # create a Chrome driver instance
        login_test.test_login_with_valid_credentials(driver) # run the test_login_with_valid_credentials method
    
    # Run fail login test
    with webdriver.Chrome() as driver: # create a Chrome driver instance
        login_test.test_login_with_invalid_credentials(driver) # run the test_login_with_invalid_credentials method


    # Run the product tests
    product_test = TestProductPage() # create an instance of the TestProductPage class

    # Run all products displayed test
    with webdriver.Chrome() as driver: # create a Chrome driver instance
        product_test.test_all_products_displayed(driver) # run the test_all_products_displayed method
    
    # Run search product test
    with webdriver.Chrome() as driver: # create a Chrome driver instance
        product_test.test_search_product(driver) # run the test_search_product method
    
    # Run add product to cart test
    with webdriver.Chrome() as driver: # create a Chrome driver instance
        product_test.test_add_product_to_cart(driver) # run the test_add_product_to_cart method
