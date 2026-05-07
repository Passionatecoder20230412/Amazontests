from selenium.webdriver.common.by import By


from pages.BasePage import BasePage


class HomePage(BasePage):
    def __init__(self,init_driver):
        super().__init__(init_driver)
    HOMEPAGE=(By.CSS_SELECTOR,'[href="/"]')
    SIGNUP=(By.CSS_SELECTOR,'[href="/login"]')
    USER_NAME=(By.CSS_SELECTOR,'[data-qa="login-email"]')
    PASSWORD=(By.CSS_SELECTOR,'[data-qa="login-password"]')
    LOGIN_BTN=(By.CSS_SELECTOR,'[data-qa="login-button"]')
    def home_text(self):
        return self.get_text(self.HOMEPAGE)

    def signup_click(self):
        self.click_button(self.SIGNUP)
    def enter_username(self,username):
        self.enter_text(self.USER_NAME,username)
    def enter_pwd(self,pwd):
        self.enter_text(self.PASSWORD,pwd)
    def login_click(self):
        self.click_button(self.LOGIN_BTN)