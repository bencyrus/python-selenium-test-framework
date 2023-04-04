from page_objects.payment_done_page import PaymentDonePage

class TestPaymentDonePage():
    # Test cases for the payment done page.

    def test_payment_done(self, driver):
        # Test executing a payment.

        payment_done_page = PaymentDonePage(driver)

        assert payment_done_page.is_order_confirmation_message_displayed() == True, "The order confirmation message is not displayed."
        payment_done_page.download_invoice()

        print("Execute payment done test passed")