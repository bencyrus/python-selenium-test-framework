from behave import given, when, then


@given("I am on the login page")
def step_impl(context):
    # context.login_page = LoginPage(context.driver)
    context.login_page.open()


@when("I execute login with {email} as email and {password} as password")
def step_impl(context, email, password):
    context.login_page.execute_login(email, password)


@then("I should see a login failed message")
def step_impl(context):
    assert context.login_page.is_login_failed_message_displayed(), "Login failed message not displayed"


@then("I should be redirected to the main page with the title {title}")
def step_impl(context, title):
    assert context.main_page.is_main_page_url_correct(), \
        "Not redirected to main page"
    assert context.main_page.is_main_page_title_correct(title), \
        "Incorrect main page title"


@then("I should see the logout button")
def step_impl(context):
    assert context.main_page.is_logout_button_visible(), "Logout button not visible"


@then("the user name should be {user_name}")
def step_impl(context, user_name):
    assert context.main_page.is_user_name_correct(user_name), \
        "Incorrect user name displayed"
