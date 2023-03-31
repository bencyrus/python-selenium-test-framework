from page_objects.logged_in_main_page import LoggedInMainPage
from page_objects.login_page import LoginPage


class TestLoginPage:
    # Test cases for the login functionality.

    def test_login_with_valid_credentials(self, driver):
        # Test logging in with valid credentials.
        login_page = LoginPage(driver)  # create an instance of the LoginPage class
        login_page.open()  # open the login page
        login_page.execute_login("mahdi.mohaghegh2001@gmail.com", "12345678")  # execute a login
        logged_in_main_page = LoggedInMainPage(driver)  # create an instance of the LoggedInMainPage class

        # verify that the user is logged in
        actual_user_name = logged_in_main_page.get_user_name()
        expected_user_name = "Ben Cyrus"
        assert logged_in_main_page.expected_user_name(expected_user_name) == actual_user_name, \
            f"Expected user name '{expected_user_name}' but got {actual_user_name}"
        assert logged_in_main_page.is_logout_button_visible(), "The logout button is not visible"

    def test_login_with_invalid_credentials(self, driver):
        # Test logging in with invalid credentials.
        login_page = LoginPage(driver)  # create an instance of the LoginPage class
        login_page.open()  # open the login page
        login_page.execute_login("invalid_mahdi.mohaghegh2001@gmail.com", "invalid_12345678")  # execute a login with invalid credentials

        # verify that the user is not logged in
        assert login_page.is_login_failed_message_displayed(), "The login failed message is not visible"
