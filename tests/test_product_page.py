import pytest
import config
from pages.homepage import HomePage
from pages.search_results_page import SearchResultsPage
from pages.product_page import ProductPage
from utils.logger import LOGGER

@pytest.mark.usefixtures("init_driver")
class TestProductPage:
    def test_product_page_elements(self):
        LOGGER.info("Starting test: Product page elements validation")

        home_page = HomePage(self.driver)
        home_page.visit(config.BASE_URL)
        home_page.search_for_item(config.SEARCH_KEYWORD_VALID)

        search_page = SearchResultsPage(self.driver)
        products = search_page.get_products()

        if len(products) == 0:
            pytest.fail("No products found to validate on the product page.")

        first_product_url = products[0]["url"]
        self.driver.get(first_product_url)

        product_page = ProductPage(self.driver)

        add_to_cart_exists = product_page.validate_add_to_cart_button()
        product_details_exists = product_page.validate_product_details_section()
        image_gallery_exists = product_page.validate_image_gallery()

        LOGGER.info(f"Add to Cart Button presence: {add_to_cart_exists}")
        LOGGER.info(f"Product Details presence: {product_details_exists}")
        LOGGER.info(f"Image Gallery presence: {image_gallery_exists}")

        assert add_to_cart_exists, "Add to Cart button not found."
        assert product_details_exists, "Product details section not found."
        assert image_gallery_exists, "Image gallery not found."
