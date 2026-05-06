from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
from Utils.logger import TestLogger


class RegisterWithExistingMail(BasePage):
    SIGN_IN_HOVER = (By.XPATH, '//div[@class="nav-line-1-container"]/span')
    REGISTER = (By.XPATH, '//a[contains(text(),"Start here")]')
    EMAIL_OR_NUMBER = (By.CSS_SELECTOR, '[id="ap_email_login"]')
    CONTINUE = (By.CSS_SELECTOR, '[class="a-button-input"]')
    SIGN_IN_TEXT = (By.XPATH, '//h1[contains(text(),"Sign in")]')
    NEW_REG_TEXT = (By.XPATH, '//h1[contains(text(),"It looks like you are new to Amazon")]')

    def __init__(self, driver):
        super().__init__(driver)
        self.logger = TestLogger(self.__class__.__name__).get_logger()

    def web_link(self):
        self.logger.info("Opening URL")
        return self.current_url()

    def register_with_existing_mail(self, email_num):
        self.logger.info("Hover on Sign In")
        self.mouse_hover(self.SIGN_IN_HOVER)

        self.logger.info("Click Register")
        self.click_button(self.REGISTER)

        self.logger.info(f"Entering email: {email_num}")
        self.enter_text(self.EMAIL_OR_NUMBER, email_num)

        self.logger.info("Click Continue")
        self.click_button(self.CONTINUE)

        # 🔥 Better handling
        if self.ele_visible(self.NEW_REG_TEXT):
            text = self.get_text(self.NEW_REG_TEXT)
            self.logger.info(f"New user detected: {text}")
            return "NEW USER"

        elif self.ele_visible(self.SIGN_IN_TEXT):
            text = self.get_text(self.SIGN_IN_TEXT)
            self.logger.info(f"Existing user detected: {text}")
            return "EXISTING USER"

        else:
            self.logger.error("No expected text found")
            return "FAILED"