from behave import given, when, then
from page_objects.shopping_cart_page import ShoppingCartPage


@given("I am on the shopping cart page")
def step_impl(context):
    context.shopping_cart_page = ShoppingCartPage(context.driver)
    assert context.shopping_cart_page.is_shopping_cart_page_opened(), \
        "Shopping cart page not opened"


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
