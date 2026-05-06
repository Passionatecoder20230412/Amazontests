from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class LogoutAmazon(BasePage):

    SIGN_IN_HOVER = (By.XPATH, '//div[@class="nav-line-1-container"]/span')
    SIGN_IN = (By.XPATH, '//a[@data-nav-ref="nav_signin"]/span')
    EMAIL_OR_PASSWORD = (By.CSS_SELECTOR, '[type="email"]')
    CONTINUE = (By.CSS_SELECTOR, '[class="a-button-input"]')
    PASSWORD = (By.CSS_SELECTOR, '[id="ap_password"]')
    SIGN_IN_BUTTON = (By.CSS_SELECTOR, '[type="submit"]')
    SIGN_IN_AS=(By.CSS_SELECTOR, '[id="nav-link-accountList-nav-line-1"]')
    HOVER=(By.CSS_SELECTOR, '[class="nav-flyout-button nav-icon nav-arrow nav-active"]')
    SIGN_OUT=(By.CSS_SELECTOR, '[id="nav-item-signout"]')
    NAV_SIGNIN_AGAIN=(By.XPATH, '//h1[contains(text(),"Sign in or create account")]')

    def __init__(self,driver):
        super().__init__(driver)
    def logout_user(self,email_num,password):

        self.mouse_hover(self.SIGN_IN_HOVER)
        self.click_button(self.SIGN_IN)
        self.enter_text(self.EMAIL_OR_PASSWORD, email_num)
        self.click_button(self.CONTINUE)
        self.enter_text(self.PASSWORD, password)
        self.click_button(self.SIGN_IN_BUTTON)
        a=self.get_text(self.SIGN_IN_AS)
        self.mouse_hover(self.SIGN_IN_HOVER)
        self.click_button(self.SIGN_OUT)
        b=self.get_text(self.NAV_SIGNIN_AGAIN)
        return [a,b]




