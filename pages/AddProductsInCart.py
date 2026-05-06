import random

from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class AddProductsInCart(BasePage):
    def __init__(self,driver):
        super().__init__(driver)

    PRODUCTS=(By.CSS_SELECTOR,'[href="/products"]')
    CONTINUE_SHOPPING=(By.XPATH,'//button[contains(text(),"Continue Shopping")]')
    ADD_TO_CART_PRODUCT7=(By.CSS_SELECTOR,'[data-product-id="7"]')
    VIEW_CART=(By.XPATH,'//u[contains(text(),"View Cart")]')
    PRICE_IN_CART=(By.XPATH,'//tr[@id="product-1"]/td[@class="cart_price"]/p')
    CART_INFO=(By.XPATH,'//tr')


    def add_products_feature(self):
        self.click_button(self.PRODUCTS)
        for i in range(1,6):
            num=random.randint(1,5)
            print(f"product details of {num}")
            ADD_TO_CART_PRODUCT = (By.CSS_SELECTOR, f'[data-product-id="{num}"]')
            PROD_NAME = (By.XPATH, f'//a[@data-product-id="{num}"]/parent::div/p')
            PRICE = (By.XPATH, f'//a[@data-product-id="{num}"]/parent::div/h2')
            self.get_text(PROD_NAME)
            self.get_text(PRICE)
            self.click_button(ADD_TO_CART_PRODUCT)
            self.click_button(self.CONTINUE_SHOPPING)

        self.click_button(self.ADD_TO_CART_PRODUCT7)
        self.click_button(self.VIEW_CART)
        self.get_text(self.PRICE_IN_CART)
        self.get_text(self.CART_INFO)
