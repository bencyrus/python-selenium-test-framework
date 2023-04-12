from behave import given, when, then


@given("I am logged in successfully with the user name {user_name}")
def step_impl(context, user_name):
    assert context.main_page.is_user_name_correct(user_name), \
        "Incorrect user name displayed. Current user name: " + context.main_page.get_user_name() + ". "+ "Expected user name: " + user_name + "."


@when("I open the products page")
def step_impl(context):
    context.main_page.open_products_page()


@then("I should see the All Products title")
def step_impl(context):
    assert context.products_page.is_all_products_title_displayed(), \
        "All Products title not displayed"


@when("I search for {product_name}")
def step_impl(context, product_name):
    context.products_page.execute_product_search(product_name)


@then("I should see the Searched Products title")
def step_impl(context):
    assert context.products_page.is_searched_products_title_displayed(), \
        "Searched products title not displayed"
    assert context.products_page.is_product_search_results_displayed(), \
        "Product search results not displayed"


@when("I add the product number {count:d} to the cart")
def step_impl(context, count):
    context.products_page.add_product_to_cart(count)


@then("I should be able to view the cart")
def step_impl(context):
    context.products_page.view_cart()
