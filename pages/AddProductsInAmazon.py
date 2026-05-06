import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.BasePage import BasePage


class AddProductsInAmazon(BasePage):

    SEARCH = (By.ID, "twotabsearchtextbox")
    SEARCH_BTN = (By.ID, "nav-search-submit-button")

    VIEW_CART = (By.ID, "nav-cart")

    PRODUCT_CARDS = (By.XPATH, '//div[@data-cy="asin-faceout-container"]')

    def add_products_feature20(self):

        wait = WebDriverWait(self.driver, 10)

        # search
        wait.until(EC.visibility_of_element_located(self.SEARCH)).send_keys("Samsung A17 5G")
        self.click_button(self.SEARCH_BTN)

        # wait for products
        products = wait.until(
            EC.presence_of_all_elements_located(self.PRODUCT_CARDS)
        )

        # pick 3 random products safely
        selected_products = random.sample(products, 3)

        for i, product in enumerate(selected_products, start=1):
            print(f"product details of {i}")

            title = product.find_element(By.XPATH, './/h2/span').text
            print(title)

            add_to_cart = product.find_element(By.XPATH, './/button[@name="submit.addToCart"]')

            self.driver.execute_script("arguments[0].scrollIntoView();", add_to_cart)
            add_to_cart.click()

            # wait for cart confirmation (important)
            wait.until(EC.presence_of_element_located((By.ID, "nav-cart-count")))

        # go to cart
        self.click_button(self.VIEW_CART)

        print("done")



# import random
# import time
#
# from selenium.webdriver.common.by import By
#
# from pages.BasePage import BasePage
#
#
# class AddProductsInAmazon(BasePage):
#     def __init__(self,driver):
#         super().__init__(driver)
#
#     # num=random.randint(1,9)
#     SEARCH=(By.ID,'twotabsearchtextbox')
#     # ADD_TO_CART_PRODUCT=(By.CSS_SELECTOR,f'[data-product-id="{num}"]')
#     SAMSUNG=(By.XPATH,'//span[contains(text(),"sung a17 5g")]')
#
#     VIEW_CART=(By.CSS_SELECTOR,'[href="/gp/cart/view.html?ref_=nav_cart"]')
#     # PROD_NAME=(By.XPATH,f'//a[@data-product-id="{num}"]/parent::div/p')
#     # PRICE=(By.XPATH,f'//a[@data-product-id="{num}"]/parent::div/h2')
#     PRICE_IN_CART=(By.XPATH,'//tr[@id="product-1"]/td[@class="cart_price"]/p')
#     CART_INFO=(By.XPATH,'//tr')
#
#
#     def add_products_feature20(self):
#         self.click_button(self.SEARCH)
#         self.enter_text(self.SEARCH,"sam")
#         self.click_button(self.SAMSUNG)
#         for i in range(1,4):
#             num=random.randint(1,4)
#             print(f"product details of {num}")
#             PRODUCT_INFO=(By.XPATH,f'//div[@data-cel-widget="search_result_{num}"]//h2/span[contains(text(),"Galaxy A17 5G")]')
#             ADD_TO_CART_PRODUCT= (By.XPATH,f'//div[@data-cel-widget="search_result_{num}"]//button')
#
#             self.get_text(PRODUCT_INFO)
#             self.click_button(ADD_TO_CART_PRODUCT)
#             time.sleep(3)
#
#         self.click_button(self.VIEW_CART)
#         # time.sleep(200)
#         print("done")
