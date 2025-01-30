from selenium.webdriver.common.by import By
from .base_page import BasePage

class ProductPage(BasePage):
    ADD_TO_CART_BTN = (By.ID, "add-to-cart-button")
    PRODUCT_DETAILS_SECTION = (By.ID, "feature-bullets")
    IMAGE_GALLERY = (By.ID, "imageBlock_feature_div")

    def validate_add_to_cart_button(self):
        return self.wait_for_element(self.ADD_TO_CART_BTN, timeout=10)

    def validate_product_details_section(self):
        return self.wait_for_element(self.PRODUCT_DETAILS_SECTION, timeout=10)

    def validate_image_gallery(self):
        return self.wait_for_element(self.IMAGE_GALLERY, timeout=10)
