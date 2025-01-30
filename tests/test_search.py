import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import config
from pages.homepage import HomePage
from pages.search_results_page import SearchResultsPage
from utils.logger import LOGGER
from utils.csv_writer import write_products_to_csv

@pytest.mark.usefixtures("init_driver")
class TestSearch:
    def test_valid_search_and_extract(self):
        LOGGER.info("Starting test: Valid search and extract products")

        home_page = HomePage(self.driver)
        home_page.visit(config.BASE_URL)

        home_page.search_for_item(config.SEARCH_KEYWORD_VALID)

        search_page = SearchResultsPage(self.driver)
        all_products = []

        page_count = 0
        while page_count < config.MAX_PAGES_TO_CRAWL:
            products = search_page.get_products()
            all_products.extend(products)
            LOGGER.info(f"Extracted {len(products)} products from page {page_count+1}.")
            
            if not search_page.go_to_next_page():
                LOGGER.info("No more pages to crawl.")
                break
            page_count += 1

        write_products_to_csv(all_products)
        LOGGER.info(f"Total products extracted: {len(all_products)}. Written to CSV.")

        assert len(all_products) > 0, "No products found or extracted."

    def test_invalid_search(self):
        LOGGER.info("Starting test: Invalid search scenario")

        home_page = HomePage(self.driver)
        home_page.visit(config.BASE_URL)

        home_page.search_for_item(config.SEARCH_KEYWORD_INVALID)

        search_page = SearchResultsPage(self.driver)
        products = search_page.get_products()

        if len(products) == 0:
            LOGGER.info("Invalid search returned 0 products as expected.")
            assert True
        else:
            LOGGER.warning("Invalid search returned some products, which is unexpected.")
            assert False, "Expected no products for invalid search query."
