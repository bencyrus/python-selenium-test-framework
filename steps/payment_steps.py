from behave import given, when, then


@given("I am on the payment page")
def step_impl(context):
    assert context.payment_page.is_payment_page_opened(), \
        "Payment page not opened"


@when("I enter the credit card information with the following details")
def step_impl(context):
    card_info = {}
    for row in context.table:
        card_info[row["field"]] = row["value"]
    context.payment_page.enter_payment_information(card_info["card holder"], card_info["card number"], card_info["cvv"],
                                                   card_info["expiry month"], card_info["expiry year"])


@then("I should be able to confirm and pay the order")
def step_impl(context):
    context.payment_page.execute_pay_and_confirm_order()


@when("I see order confirmation message")
def step_impl(context):
    assert context.payment_done_page.is_order_confirmation_message_displayed(), \
        "Order confirmation message not displayed"


@then("I should be able to download the invoice")
def step_impl(context):
    context.payment_done_page.download_invoice()
