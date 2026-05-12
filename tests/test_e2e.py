import random
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ---------- SETUP ----------
def test_end_to_end():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.amazon.in/")

    wait = WebDriverWait(driver, 10)

    # ---------- LOCATORS ----------
    SEARCH = (By.ID, "twotabsearchtextbox")
    SEARCH_BTN = (By.ID, "nav-search-submit-button")
    VIEW_CART = (By.ID, "nav-cart")
    PRODUCT_CARDS = (By.XPATH, '//div[@data-cy="asin-faceout-container"]')

    CHECKOUT = (By.CSS_SELECTOR,'[name="proceedToRetailCheckout"]')
    LOGIN_CREDENTIALS_ENTER = (By.CSS_SELECTOR,'[aria-label="Enter mobile number or email"]')
    CONTINUE = (By.CSS_SELECTOR,'[class="a-button-input"]')
    PASSWORD = (By.CSS_SELECTOR,'[type="password"]')
    SIGN_IN = (By.CSS_SELECTOR,'[id="signInSubmit"]')
    NAV_CART = (By.CSS_SELECTOR,'[href="/gp/cart/view.html?ref_=nav_cart"]')
    SELECT_PAYMENT = (By.CSS_SELECTOR,'[value="SelectableAddCreditCard"]')
    ADD_NEW_CARD = (By.XPATH,'(//a[contains(text(),"Add a new credit or debit card")])[1]')
    FRAME = (By.CSS_SELECTOR,'[name="ApxSecureIframe"]')
    CARD_NUMBER = (By.CSS_SELECTOR,'[name="addCreditCardNumber"]')
    AC_HOLDER_NAME = (By.CSS_SELECTOR,'[name="ppw-accountHolderName"]')
    SELECT_MONTH = (By.CSS_SELECTOR,'[name="ppw-expirationDate_month"]')
    EXPIRY_YEAR = (By.CSS_SELECTOR,'[name="ppw-expirationDate_year"]')
    CONTINUE_CARD=(By.CSS_SELECTOR,'[name="ppw-widgetEvent:AddCreditCardEvent"]')
    CVV=(By.CSS_SELECTOR,'[class="card-cvv"]')
    PAYMENT_CONTINUE=(By.CSS_SELECTOR,'[data-testid="secondary-continue-button"]')
    CARD_WITHOUT_SAVE=(By.XPATH,'//*[contains(text(),"Continue without saving")]')
    CARD_WITH_SAVE=(By.XPATH,'//*[contains(text(),"Save card & continue")]')
    # ---------- SEARCH ----------
    wait.until(EC.visibility_of_element_located(SEARCH)).send_keys("Samsung A17 5G")
    driver.find_element(*SEARCH_BTN).click()

    # ---------- GET PRODUCTS ----------
    products = wait.until(EC.presence_of_all_elements_located(PRODUCT_CARDS))

    # ---------- SELECT RANDOM PRODUCTS ----------
    selected_products = random.sample(products, 3)

    for i, product in enumerate(selected_products, start=1):
        print(f"Product {i}")

        title = product.find_element(By.XPATH, './/h2/span').text
        print(title)

        add_to_cart = product.find_element(By.XPATH, './/button[@name="submit.addToCart"]')

        driver.execute_script("arguments[0].scrollIntoView();", add_to_cart)
        add_to_cart.click()

        # wait for cart update
        wait.until(EC.presence_of_element_located((By.ID, "nav-cart-count")))

    # ---------- GO TO CART ----------
    driver.find_element(*VIEW_CART).click()

    # ---------- CHECKOUT ----------
    wait.until(EC.element_to_be_clickable(CHECKOUT)).click()

    # ---------- LOGIN ----------
    wait.until(EC.visibility_of_element_located(LOGIN_CREDENTIALS_ENTER)).send_keys("7207962483")
    driver.find_element(*CONTINUE).click()

    wait.until(EC.visibility_of_element_located(PASSWORD)).send_keys("Vijay@8500")
    driver.find_element(*SIGN_IN).click()

    # ---------- BACK TO CART ----------
    wait.until(EC.element_to_be_clickable(NAV_CART)).click()
    wait.until(EC.element_to_be_clickable(CHECKOUT)).click()

    # ---------- PAYMENT ----------
    wait.until(EC.element_to_be_clickable(SELECT_PAYMENT)).click()
    wait.until(EC.element_to_be_clickable(ADD_NEW_CARD)).click()

    # switch to iframe
    wait.until(EC.frame_to_be_available_and_switch_to_it(FRAME))

    wait.until(EC.visibility_of_element_located(CARD_NUMBER)).send_keys("1234567812345678")
    ele=(driver.find_element(*AC_HOLDER_NAME))
    ele.clear()
    ele.send_keys("Vijay")

    # select dropdowns
    from selenium.webdriver.support.ui import Select

    Select(driver.find_element(*SELECT_MONTH)).select_by_visible_text("12")
    Select(driver.find_element(*EXPIRY_YEAR)).select_by_visible_text("2030")
    time.sleep(5)
    driver.find_element(*CONTINUE_CARD).click()
    driver.find_element(*CVV).send_keys("786")
    driver.find_element(*PAYMENT_CONTINUE).click()
    driver.find_element(*CARD_WITHOUT_SAVE).click()
    print("✅ Flow completed")

    # driver.quit()