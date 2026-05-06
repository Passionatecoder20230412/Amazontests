from email.contentmanager import get_text_content

from selenium.webdriver.common.by import By

from pages.BasePage import BasePage
# 1. Launch browser
# 2. Navigate to url 'http://automationexercise.com'
# 3. Verify that home page is visible successfully
# 4. Click on 'Signup / Login' button
# 5. Verify 'Login to your account' is visible
# 6. Enter correct email address and password
# 7. Click 'login' button
# 8. Verify that 'Logged in as username' is visible
# 9. Click 'Delete Account' button
# 10. Verify that 'ACCOUNT DELETED!' is visible
class LoginWithValidInvalidDetails(BasePage):

    SIGN_IN_HOVER = (By.XPATH, '//div[@class="nav-line-1-container"]/span')
    SIGN_IN=(By.XPATH,'//a[@data-nav-ref="nav_signin"]/span')
    EMAIL_OR_PASSWORD=(By.CSS_SELECTOR,'[type="email"]')
    CONTINUE=(By.CSS_SELECTOR,'[class="a-button-input"]')
    PASSWORD=(By.CSS_SELECTOR,'[id="ap_password"]')
    SIGN_IN_BUTTON=(By.CSS_SELECTOR,'[type="submit"]')
    HOVER_AFTER_SIGN_IN=(By.XPATH,'//div[@class="nav-line-1-container"]/span')
    TEXT_ASSERT=(By.XPATH,'//a[@id="nav-item-signout"]/span')


    def __init__(self,driver):
        super().__init__(driver)



    def get_url(self):
        return self.current_url()
    def login_check(self,email,password):
        self.mouse_hover(self.SIGN_IN_HOVER)
        self.click_button(self.SIGN_IN)
        self.enter_text(self.EMAIL_OR_PASSWORD,email)
        self.click_button(self.CONTINUE)
        self.enter_text(self.PASSWORD,password)
        self.click_button(self.SIGN_IN_BUTTON)
        self.mouse_hover(self.HOVER_AFTER_SIGN_IN)
    def assert_text(self):
        return self.get_text(self.TEXT_ASSERT)


