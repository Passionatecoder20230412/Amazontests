# Test Case 1: Register User
# 1. Launch browser
# 2. Navigate to url 'http://automationexercise.com'
# 3. Verify that home page is visible successfully
# 4. Click on 'Signup / Login' button
# 5. Verify 'New User Signup!' is visible
# 6. Enter name and email address
# 7. Click 'Signup' button
# 8. Verify that 'ENTER ACCOUNT INFORMATION' is visible
# 9. Fill details: Title, Name, Email, Password, Date of birth
# 10. Select checkbox 'Sign up for our newsletter!'
# 11. Select checkbox 'Receive special offers from our partners!'
# 12. Fill details: First name, Last name, Company, Address, Address2, Country, State, City, Zipcode, Mobile Number
# 13. Click 'Create Account button'
# 14. Verify that 'ACCOUNT CREATED!' is visible
# 15. Click 'Continue' button
# 16. Verify that 'Logged in as username' is visible
# 17. Click 'Delete Account' button
# 18. Verify that 'ACCOUNT DELETED!' is visible and click 'Continue' button
import random

from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class CreateAccount(BasePage):
    def __init__(self,driver):
        super().__init__(driver)


    SIGNUP_LINK=(By.CSS_SELECTOR,'[href="/login"]')
    NEW_ACCOUNT=(By.XPATH,'//div[@class="signup-form"]/h2')
    NAME=(By.CSS_SELECTOR,'[data-qa="signup-name"]')
    EMAIL = (By.CSS_SELECTOR, '[data-qa="signup-email"]')
    SIGNUP = (By.CSS_SELECTOR, '[data-qa="signup-button"]')
    ACCOUNT_INFO_TEXT=(By.XPATH,'//div[@class="login-form"]/h2/b')
    GENDER=(By.CSS_SELECTOR,f'[id="id_gender{random.randint(1,2)}"]')
    PASSWORD=(By.CSS_SELECTOR,'[data-qa="password"]')
    DOB_DAY=(By.CSS_SELECTOR,'[data-qa="days"]')
    DOB_MONTH=(By.CSS_SELECTOR,'[data-qa="months"]')
    DOB_YEAR=(By.CSS_SELECTOR,'[data-qa="years"]')
    NEWSLETTER_CHECKBOX=(By.CSS_SELECTOR,'[name="newsletter"]')
    RECEIVE_OFFERS=(By.CSS_SELECTOR,'[name="optin"]')
    FIRST_NAME=(By.CSS_SELECTOR,'[data-qa="first_name"]')
    LAST_NAME=(By.CSS_SELECTOR,'[data-qa="last_name"]')
    COMPANY=(By.CSS_SELECTOR,'[data-qa="company"]')
    ADDRESS=(By.CSS_SELECTOR,'[data-qa="address"]')
    ADDRESS2 = (By.CSS_SELECTOR, '[data-qa="address2"]')
    COUNTRY=(By.CSS_SELECTOR,'[data-qa="country"]')
    STATE=(By.CSS_SELECTOR,'[data-qa="state"]')
    CITY=(By.CSS_SELECTOR,'[data-qa="city"]')
    ZIPCODE=(By.CSS_SELECTOR,'[data-qa="zipcode"]')
    MOBILE_NUMBER=(By.CSS_SELECTOR,'[data-qa="mobile_number"]')
    CREATE_NEW_ACCOUNT=(By.CSS_SELECTOR,'[data-qa="create-account"]')
    ACCOUNT_CREATED=(By.XPATH,'//h2[@data-qa="account-created"]/b')
    CONTINUE=(By.CSS_SELECTOR,'[data-qa="continue-button"]')
    LOGGED_IN_BY=(By.XPATH,'//a/b')
    DELETE_ACCOUNT=(By.CSS_SELECTOR,'[href="/delete_account"]')
    VERIFY_AC_DELETED=(By.XPATH,'//h2/b')

    def home_text(self):
        return self.get_title()
    def click_signup(self):
        self.click_button(self.SIGNUP_LINK)
    def new_account_text(self):
        return self.get_text(self.NEW_ACCOUNT)
    def new_use_visible(self):
        return self.is_visible(self.NEW_ACCOUNT)
    def user_details(self,name,email,password,day,month,year,first_name,last_name,company,address,address2,country,state,city,zipcode,mobile_number):
        self.enter_text(self.NAME,name)
        self.enter_text(self.EMAIL,email)
        self.click_button(self.SIGNUP)
        self.is_visible(self.ACCOUNT_INFO_TEXT)
        self.click_button(self.GENDER)
        self.enter_text(self.PASSWORD,password)
        self.select_options_text(self.DOB_DAY,day)
        self.select_options_text(self.DOB_MONTH,month)
        self.select_options_text(self.DOB_YEAR,year)
        # NEWSLETTER_CHECKBOX = (By.CSS_SELECTOR, '[name="newsletter"]')
        self.click_button(self.NEWSLETTER_CHECKBOX)
        # RECEIVE_OFFERS = (By.CSS_SELECTOR, '[name="optin"]')
        self.click_button(self.RECEIVE_OFFERS)
        # FIRST_NAME = (By.CSS_SELECTOR, '[data-qa="first_name"]')
        self.enter_text(self.FIRST_NAME,first_name)
        # LAST_NAME = (By.CSS_SELECTOR, '[data-qa="last_name"]')
        self.enter_text(self.LAST_NAME,last_name)
        # COMPANY = (By.CSS_SELECTOR, '[data-qa="company"]')
        self.enter_text(self.COMPANY,company)
        # ADDRESS = (By.CSS_SELECTOR, '[data-qa="address"]')
        self.enter_text(self.ADDRESS,address)
        # ADDRESS2 = (By.CSS_SELECTOR, '[data-qa="address2"]')
        self.enter_text(self.ADDRESS2,address2)
        # COUNTRY = (By.CSS_SELECTOR, '[data-qa="country"]')
        self.select_options_text(self.COUNTRY,country)
        # STATE = (By.CSS_SELECTOR, '[data-qa="state"]')
        self.enter_text(self.STATE,state)
        # CITY = (By.CSS_SELECTOR, '[data-qa="city"]')
        self.enter_text(self.CITY,city)
        # ZIPCODE = (By.CSS_SELECTOR, '[data-qa="zipcode"]')
        self.enter_text(self.ZIPCODE,zipcode)
        # MOBILE_NUMBER = (By.CSS_SELECTOR, '[data-qa="mobile_number"]')
        self.enter_text(self.MOBILE_NUMBER,mobile_number)

        self.click_button(self.CREATE_NEW_ACCOUNT)
        #verify that account created
        self.get_text(self.ACCOUNT_CREATED)
        self.click_button(self.CONTINUE)
        self.get_text(self.LOGGED_IN_BY)
        # self.click_button(self.DELETE_ACCOUNT)
        # assert self.get_text(self.VERIFY_AC_DELETED)=="Account Deleted!","Not able to delete the account"














