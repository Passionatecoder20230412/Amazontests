from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class ProceedToCheckout(BasePage):
    def __init__(self,driver):
        super().__init__(driver)

    CHECKOUT=(By.CSS_SELECTOR,'[name="proceedToRetailCheckout"]')
    LOGIN_CREDENTIALS_ENTER=(By.CSS_SELECTOR,'[aria-label="Enter mobile number or email"]')
    CONTINUE=(By.CSS_SELECTOR,'[class="a-button-input"]')
    PASSWORD=(By.CSS_SELECTOR,'[type="password"]')
    SIGN_IN=(By.CSS_SELECTOR,'[id="signInSubmit"]')
    NAV_CART=(By.CSS_SELECTOR,'[href="/gp/cart/view.html?ref_=nav_cart"]')
    SELECT_PAYMENT=(By.CSS_SELECTOR,'[value="SelectableAddCreditCard"]')
    ADD_NEW_CARD=(By.XPATH,'(//a[contains(text(),"Add a new credit or debit card")])[1]')
    FRAME=(By.CSS_SELECTOR,'[name="ApxSecureIframe"]')
    CARD_NUMBER=(By.CSS_SELECTOR,'[name="addCreditCardNumber"]')
    AC_HOLDER_NAME=(By.CSS_SELECTOR,'[name="ppw-accountHolderName"]')
    SELECT_MONTH=(By.CSS_SELECTOR,'[name="ppw-expirationDate_month"]')
    EXPIRY_YEAR=(By.CSS_SELECTOR,'[name="ppw-expirationDate"]')

    def proceed_to_checkout(self,email,password,card_num,name,attr_name,month,year):
        self.click_button(self.CHECKOUT)
        self.enter_text(self.LOGIN_CREDENTIALS_ENTER,email)
        self.click_button(self.CONTINUE)
        self.enter_text(self.PASSWORD,password)
        self.click_button(self.SIGN_IN)
        self.click_button(self.NAV_CART)
        self.click_button(self.CHECKOUT)
        self.click_button(self.SELECT_PAYMENT)
        self.click_button(self.ADD_NEW_CARD)
        self.driver.switch_to.frame(self.driver.find_element(*self.FRAME))
        self.enter_text(self.CARD_NUMBER,card_num)
        self.enter_text(self.AC_HOLDER_NAME,name)
        self.get_attr_value(self.AC_HOLDER_NAME,attr_name)
        self.select_options_text(self.SELECT_MONTH,month)
        self.select_options_text(self.EXPIRY_YEAR,year)

