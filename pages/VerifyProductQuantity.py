import time

from selenium.webdriver.common.by import By

from pages.BasePage import BasePage

# Test Case 13: Verify Product quantity in Cart
# 1. Launch browser
# 2. Navigate to url 'http://automationexercise.com'
# 3. Verify that home page is visible successfully
# 4. Click 'View Product' for any product on home page
# 5. Verify product detail is opened
# 6. Increase quantity to 4
# 7. Click 'Add to cart' button
# 8. Click 'View Cart' button
# 9. Verify that product is displayed in cart page with exact quantity
class VerifyProductQuantity(BasePage):

    SEARCH=(By.CSS_SELECTOR,'[id="twotabsearchtextbox"]')
    CASIO=(By.XPATH,'//div[contains(.,"calculator original")]/span')
    DATA=(By.XPATH,'//h2[@aria-label="Sponsored Ad - 991ES Plus Scientific Calculator | 417 Functions | Four-Line Natural Display | Dual Power Solar & Battery | Engineering & Student Calculator | Black"]/span')
    ADD_TO_CART=(By.CSS_SELECTOR,'[id="a-autoid-1-announce"]')
    INCREMENT=(By.CSS_SELECTOR,'[data-a-selector="increment-icon"]')
    SELECTING_TIMES=(By.CSS_SELECTOR,'[data-a-selector="value"]')
    CART=(By.CSS_SELECTOR,'[id="nav-cart"]')
    CART_COUNT=(By.CSS_SELECTOR,'[data-a-selector="inner-value"]')

    def __init__(self,driver):
        super().__init__(driver)
    def get_url(self):
        return self.current_url()
    def verify_product_quantity(self,text,repeat):
        self.enter_text(self.SEARCH,text)
        self.click_button(self.CASIO)
        data=self.get_text(self.DATA)
        self.click_button(self.ADD_TO_CART)

        for i in range(repeat-1):
            self.click_button(self.INCREMENT)
            time.sleep(1)



        if self.get_text(self.SELECTING_TIMES)==str(repeat):
            print(f"we go for cart to check same {repeat} times ")

        self.click_button(self.CART)
        count=self.get_text(self.CART_COUNT)

        return [data,count]








