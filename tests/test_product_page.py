from page_objects.products_page import ProductPage
from page_objects.shopping_cart_page import ShoppingCartPage


class TestProductPage:
    # Test cases for the product page.

    def test_all_products_displayed(self, driver):
        # Test that all products are displayed.
        product_page = ProductPage(driver) # create an instance of the ProductPage class
        product_page.open() # open the product page
        assert product_page.is_all_products_title_displayed(), "The all products title is not visible" # verify that the all products title is displayed

        print("All products displayed test passed") # print a test success message

    def test_search_product(self, driver):
        # Test searching a product.
        product_page = ProductPage(driver) # create an instance of the ProductPage class
        product_page.open() # open the product page
        product_page.execute_product_search("tshirt") # execute a product search for "tshirt"
        assert product_page.is_searched_products_title_displayed(), "The searched products title is not visible" # verify that the searched products title is displayed
        assert product_page.is_product_search_results_displayed(), "The product search results are not visible" # verify that the product search results are displayed

        print("Search product test passed") # print a test success message

    def test_add_product_to_cart(self, driver):
        # Test adding a product to the cart.
        product_page = ProductPage(driver) # create an instance of the ProductPage class
        product_page.add_product_to_cart(0)
        product_page.add_product_to_cart(1)
        product_page.view_cart()
        shopping_cart_page = ShoppingCartPage(driver)
        assert not shopping_cart_page.is_cart_empty(), "The cart is empty"

        print("Add products to cart test passed") # print a test success message

    def test_remove_product_from_cart(self, driver):
        # Test removing a product from the cart.
        shopping_cart_page = ShoppingCartPage(driver)
        shopping_cart_page.delete_item_from_cart()
        assert not shopping_cart_page.is_cart_empty(), "The cart is not empty"

        print("Remove product from cart test passed") # print a test success message
    
    def test_checkout(self, driver):
        # Test checking out.
        shopping_cart_page = ShoppingCartPage(driver)
        shopping_cart_page.proceed_to_checkout()
        
        print("Checkout test passed")