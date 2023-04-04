from page_objects.payment_page import PaymentPage

class TestPaymentPage:
    # Test cases for the payment page.

    def test_payment(self, driver):
        # Test executing a payment.
        payment_page = PaymentPage(driver)
        payment_page.enter_payment_information("John Doe", "4242424242424242", "123", "12", "2026")
        payment_page.execute_pay_and_confirm_order()

        print("Execute payment test passed")