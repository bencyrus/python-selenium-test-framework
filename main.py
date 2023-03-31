from selenium import webdriver
from tests.test_login_page import TestLoginPage

if __name__ == "__main__":
    
    # Run the login tests
    login_test = TestLoginPage()
    
    # Run success login test
    with webdriver.Chrome() as driver:
        login_test.test_login_with_valid_credentials(driver)
    
    # Run fail login test
    with webdriver.Chrome() as driver:
        login_test.test_login_with_invalid_credentials(driver)
