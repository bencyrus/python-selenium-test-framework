from page_objects.logged_in_main_page import LoggedInMainPage
from page_objects.login_page import LoginPage


# The test_positive_login method is used to test the login functionality.
def test_positive_login(self, driver):
    # Try to log in with valid credentials

    # Create an instance of the LoginPage class
    login_page = LoginPage(driver)

    # Open the login page
    login_page.open()

    # Execute a login
    login_page.execute_login("mahdi.mohaghegh2001@gmail.com", "12345678")

    # Verify that the user is logged in

    # Create an instance of the LoggedInMainPage class
    logged_in_main_page = LoggedInMainPage(driver)

    # Verify that the user's name is correct
    assert logged_in_main_page.expected_user_name() == logged_in_main_page.get_user_name(), \
        "The user's name is not correct"

    # Verify that the logout button is visible
    assert logged_in_main_page.is_logout_button_visible(), \
        "The logout button is not visible"
