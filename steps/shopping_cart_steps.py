from behave import given, when, then


@given("I am on the shopping cart page")
def step_impl(context):
    assert context.shopping_cart_page.is_shopping_cart_page_opened(), \
        "Shopping cart page not opened. Current URL: " + context.driver.current_url + ". "+ "Expected URL: " + context.shopping_cart_page.get_shopping_cart_page_url() + "."


@given("The cart is not empty")
def step_impl(context):
    assert not context.shopping_cart_page.is_cart_empty(), \
        "Cart is empty"


@when("I remove the product number 1 from the cart")
def step_impl(context):
    context.shopping_cart_page.delete_item_from_cart()


@then("I should be able to proceed to checkout")
def step_impl(context):
    context.shopping_cart_page.proceed_to_checkout()


@then("I should be able to place the order")
def step_impl(context):
    context.checkout_page.execute_place_order()
