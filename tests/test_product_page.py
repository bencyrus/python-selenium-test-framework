from page_objects.products_page import ProductPage


class TestProductPage:
    # Test cases for the product page.
    
    def test_all_products_displayed(self, driver):
        # Test that all products are displayed.
        product_page = ProductPage(driver) # create an instance of the ProductPage class
        product_page.open() # open the product page
        assert product_page.is_all_products_title_displayed(), "The all products title is not visible" # verify that the all products title is displayed

    def test_search_product(self, driver):
        # Test searching a product.
        product_page = ProductPage(driver) # create an instance of the ProductPage class
        product_page.open() # open the product page
        product_page.execute_product_search("tshirt") # execute a product search for "tshirt"
        assert product_page.is_searched_products_title_displayed(), "The searched products title is not visible" # verify that the searched products title is displayed
        assert product_page.is_product_search_results_displayed("shirt"), "The product search results are not visible" # verify that the product search results are displayed