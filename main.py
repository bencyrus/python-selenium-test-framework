from selenium import webdriver
from tests.test_login_page import TestLoginPage

if __name__ == "__main__":
    # Create a driver
    driver = webdriver.Chrome()

    # Run the test
    login_test = TestLoginPage()
    login_test.test_success_login(driver)
