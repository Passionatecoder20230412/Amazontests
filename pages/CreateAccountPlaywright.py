import random


from pages.BasePagePlaywright import BasePagePlaywright


class CreateAccountPlaywright(BasePagePlaywright):

    # ---------------------------
    # 🔹 Locators (Playwright uses strings)
    # ---------------------------

    SIGNUP_LINK = '[href="/login"]'
    NEW_ACCOUNT = '//div[@class="signup-form"]/h2'
    NAME = '[data-qa="signup-name"]'
    EMAIL = '[data-qa="signup-email"]'
    SIGNUP = '[data-qa="signup-button"]'
    ACCOUNT_INFO_TEXT = '//div[@class="login-form"]/h2/b'

    PASSWORD = '[data-qa="password"]'
    DOB_DAY = '[data-qa="days"]'
    DOB_MONTH = '[data-qa="months"]'
    DOB_YEAR = '[data-qa="years"]'

    NEWSLETTER_CHECKBOX = '[name="newsletter"]'
    RECEIVE_OFFERS = '[name="optin"]'

    FIRST_NAME = '[data-qa="first_name"]'
    LAST_NAME = '[data-qa="last_name"]'
    COMPANY = '[data-qa="company"]'
    ADDRESS = '[data-qa="address"]'
    ADDRESS2 = '[data-qa="address2"]'
    COUNTRY = '[data-qa="country"]'
    STATE = '[data-qa="state"]'
    CITY = '[data-qa="city"]'
    ZIPCODE = '[data-qa="zipcode"]'
    MOBILE_NUMBER = '[data-qa="mobile_number"]'

    CREATE_NEW_ACCOUNT = '[data-qa="create-account"]'
    ACCOUNT_CREATED = '//h2[@data-qa="account-created"]/b'
    CONTINUE = '[data-qa="continue-button"]'
    LOGGED_IN_BY = '//a/b'
    DELETE_ACCOUNT = '[href="/delete_account"]'
    VERIFY_AC_DELETED = '//h2/b'

    # ---------------------------
    # 🔹 Actions
    # ---------------------------

    def home_text(self):
        return self.get_title()

    def click_signup(self):
        self.click_button(self.SIGNUP_LINK)

    def new_account_text(self):
        return self.get_text(self.NEW_ACCOUNT)

    def new_user_visible(self):
        return self.is_visible(self.NEW_ACCOUNT)

    def user_details(
        self,
        name,
        email,
        password,
        day,
        month,
        year,
        first_name,
        last_name,
        company,
        address,
        address2,
        country,
        state,
        city,
        zipcode,
        mobile_number,
    ):
        # Signup
        self.enter_text(self.NAME, name)
        self.enter_text(self.EMAIL, email)
        self.click_button(self.SIGNUP)

        # Account Info
        self.wait_for_element_visible(self.ACCOUNT_INFO_TEXT)

        # Random gender selection (dynamic locator)
        gender_locator = f'#id_gender{random.randint(1,2)}'
        self.click_button(gender_locator)

        self.enter_text(self.PASSWORD, password)

        self.select_by_text(self.DOB_DAY, day)
        self.select_by_text(self.DOB_MONTH, month)
        self.select_by_text(self.DOB_YEAR, year)

        # Checkboxes
        self.click_button(self.NEWSLETTER_CHECKBOX)
        self.click_button(self.RECEIVE_OFFERS)

        # Address Info
        self.enter_text(self.FIRST_NAME, first_name)
        self.enter_text(self.LAST_NAME, last_name)
        self.enter_text(self.COMPANY, company)
        self.enter_text(self.ADDRESS, address)
        self.enter_text(self.ADDRESS2, address2)

        self.select_by_text(self.COUNTRY, country)

        self.enter_text(self.STATE, state)
        self.enter_text(self.CITY, city)
        self.enter_text(self.ZIPCODE, zipcode)
        self.enter_text(self.MOBILE_NUMBER, mobile_number)

        # Create Account
        self.click_button(self.CREATE_NEW_ACCOUNT)

        # Verify Account Created
        self.wait_for_element_visible(self.ACCOUNT_CREATED)

        self.click_button(self.CONTINUE)

        # Verify Logged In
        self.wait_for_element_visible(self.LOGGED_IN_BY)

        # Delete Account
        self.click_button(self.DELETE_ACCOUNT)

        # Verify Deleted
        deleted_text = self.get_text(self.VERIFY_AC_DELETED)
        print(deleted_text)
        assert deleted_text == "Account Deleted!", "Not able to delete the account"