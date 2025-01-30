from selenium.webdriver.common.by import By
from .base_page import BasePage

class SearchResultsPage(BasePage):
    PRODUCT_TITLES = (By.XPATH, "//span[@class='a-size-medium a-color-base a-text-normal']")
    PRODUCT_LINKS = (By.XPATH, "//a[@class='a-link-normal s-no-outline']")  
    PRODUCT_PRICES = (By.XPATH, "//span[@class='a-price-whole']")  
    PRODUCT_RATINGS = (By.XPATH, "//span[@class='a-icon-alt']")

    NEXT_PAGE = (By.XPATH, "//a[contains(@class, 's-pagination-next')]")

    def get_products(self):
        """Extract product details from the current search results page."""
        titles = self.find_elements(self.PRODUCT_TITLES)
        links = self.find_elements(self.PRODUCT_LINKS)
        prices = self.find_elements(self.PRODUCT_PRICES)
        ratings = self.find_elements(self.PRODUCT_RATINGS)

        products = []
        for i in range(len(titles)):
            try:
                product_name = titles[i].text
                product_url = links[i].get_attribute('href')
                product_price = prices[i].text if i < len(prices) else "N/A"
                product_rating = ratings[i].text if i < len(ratings) else "N/A"

                products.append({
                    "name": product_name,
                    "price": product_price,
                    "rating": product_rating,
                    "url": product_url
                })
            except:
                continue

        return products

    def go_to_next_page(self):
        next_buttons = self.find_elements(self.NEXT_PAGE)
        if len(next_buttons) > 0:
            next_buttons[0].click()
            return True
        return False
