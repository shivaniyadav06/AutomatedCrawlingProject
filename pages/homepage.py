from selenium.webdriver.common.by import By
from .base_page import BasePage

class HomePage(BasePage):
    SEARCH_BAR = (By.ID, "twotabsearchtextbox")
    SEARCH_BUTTON = (By.ID, "nav-search-submit-button")

    def search_for_item(self, item):
        self.find_element(self.SEARCH_BAR).clear()
        self.find_element(self.SEARCH_BAR).send_keys(item)
        self.find_element(self.SEARCH_BUTTON).click()
