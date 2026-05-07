from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import (
    TimeoutException,
    NoSuchElementException,
    ElementClickInterceptedException,
    StaleElementReferenceException,
    ElementNotInteractableException,
    NoSuchFrameException
)


class BasePage:

    def __init__(self, driver):

        self.driver = driver

        self.wait = WebDriverWait(
            driver,
            3,
            poll_frequency=1,
            ignored_exceptions=[
                NoSuchElementException,
                StaleElementReferenceException
            ]
        )

    # ---------------------------------------------------------
    # Find Single Element
    # ---------------------------------------------------------

    def find_element(self, locator):

        try:
            element = self.wait.until(
                EC.presence_of_element_located(locator)
            )

            return element

        except TimeoutException:
            print(f"[TIMEOUT] Element not found: {locator}")

        except Exception as e:
            print(f"[ERROR] find_element failed for {locator} | {e}")

        return None

    # ---------------------------------------------------------
    # Find Multiple Elements
    # ---------------------------------------------------------

    def find_elements(self, locator):

        try:
            elements = self.wait.until(
                EC.presence_of_all_elements_located(locator)
            )

            return elements

        except TimeoutException:
            print(f"[TIMEOUT] Elements not found: {locator}")

        except Exception as e:
            print(f"[ERROR] find_elements failed for {locator} | {e}")

        return []

    # ---------------------------------------------------------
    # Enter Text
    # ---------------------------------------------------------

    def enter_text(self, locator, text):

        try:
            element = self.wait.until(
                EC.visibility_of_element_located(locator)
            )

            element.clear()
            element.send_keys(text)

            print(f"[INFO] Entered text into: {locator}")

        except TimeoutException:
            print(f"[TIMEOUT] Unable to enter text. Element not visible: {locator}")

        except ElementNotInteractableException:
            print(f"[INTERACT ERROR] Element not interactable: {locator}")

        except Exception as e:
            print(f"[ERROR] enter_text failed for {locator} | {e}")

    # ---------------------------------------------------------
    # Click Element
    # ---------------------------------------------------------

    def click_button(self, locator):

        try:
            element = self.wait.until(
                EC.element_to_be_clickable(locator)
            )

            element.click()

            print(f"[INFO] Clicked element: {locator}")

        except TimeoutException:
            print(f"[TIMEOUT] Element not clickable: {locator}")

        except ElementClickInterceptedException:
            print(f"[CLICK ERROR] Click intercepted for: {locator}")

        except Exception as e:
            print(f"[ERROR] click_button failed for {locator} | {e}")

    # ---------------------------------------------------------
    # Get Text
    # ---------------------------------------------------------

    def get_text(self, locator):

        try:
            element = self.wait.until(
                EC.visibility_of_element_located(locator)
            )

            text = element.text

            print(f"[INFO] Text from {locator} => {text}")

            return text

        except TimeoutException:
            print(f"[TIMEOUT] Unable to get text from: {locator}")

        except Exception as e:
            print(f"[ERROR] get_text failed for {locator} | {e}")

        return ""

    # ---------------------------------------------------------
    # Get Title
    # ---------------------------------------------------------

    def get_title(self):

        try:
            title = self.driver.title

            print(f"[INFO] Page Title => {title}")

            return title

        except Exception as e:
            print(f"[ERROR] get_title failed | {e}")

        return ""

    # ---------------------------------------------------------
    # Element Visible
    # ---------------------------------------------------------

    def is_visible(self, locator):

        try:
            element = self.wait.until(
                EC.visibility_of_element_located(locator)
            )

            return element.is_displayed()

        except TimeoutException:
            print(f"[TIMEOUT] Element not visible: {locator}")

        except Exception as e:
            print(f"[ERROR] is_visible failed for {locator} | {e}")

        return False

    # ---------------------------------------------------------
    # Select Dropdown by Visible Text
    # ---------------------------------------------------------

    def select_options_text(self, locator, text):

        try:
            element = self.wait.until(
                EC.presence_of_element_located(locator)
            )

            dropdown = Select(element)

            dropdown.select_by_visible_text(text)

            print(f"[INFO] Selected '{text}' from dropdown")

        except NoSuchElementException:
            print(f"[NOT FOUND] Dropdown option '{text}' not found")

        except Exception as e:
            print(f"[ERROR] select_options_text failed | {e}")

    # ---------------------------------------------------------
    # Get Attribute Value
    # ---------------------------------------------------------

    def get_attr_value(self, locator, attribute_name):

        try:
            element = self.wait.until(
                EC.presence_of_element_located(locator)
            )

            value = element.get_attribute(attribute_name)

            print(f"[INFO] Attribute '{attribute_name}' => {value}")

            return value

        except Exception as e:
            print(f"[ERROR] get_attr_value failed | {e}")

        return None

    # ---------------------------------------------------------
    # Switch Frame
    # ---------------------------------------------------------

    def switch_frames(self, locator):

        try:
            frame = self.wait.until(
                EC.presence_of_element_located(locator)
            )

            self.driver.switch_to.frame(frame)

            print(f"[INFO] Switched to frame: {locator}")

        except NoSuchFrameException:
            print(f"[FRAME ERROR] Frame not found: {locator}")

        except Exception as e:
            print(f"[ERROR] switch_frames failed | {e}")

    # ---------------------------------------------------------
    # Current URL
    # ---------------------------------------------------------

    def current_url(self):

        try:
            url = self.driver.current_url

            print(f"[INFO] Current URL => {url}")

            return url

        except Exception as e:
            print(f"[ERROR] current_url failed | {e}")

        return ""

    # ---------------------------------------------------------
    # Mouse Hover
    # ---------------------------------------------------------

    def mouse_hover(self, locator):

        try:
            element = self.wait.until(
                EC.visibility_of_element_located(locator)
            )

            ActionChains(self.driver).move_to_element(element).perform()

            print(f"[INFO] Hovered on element: {locator}")

        except Exception as e:
            print(f"[ERROR] mouse_hover failed | {e}")

    # ---------------------------------------------------------
    # Element Displayed
    # ---------------------------------------------------------

    def ele_visible(self, locator):

        try:
            element = self.wait.until(
                EC.presence_of_element_located(locator)
            )

            return element.is_displayed()

        except Exception:
            print(f"[INFO] Element not displayed: {locator}")

        return False

    # ---------------------------------------------------------
    # Find Elements List
    # ---------------------------------------------------------

    def find_elements_list(self, locator):

        try:
            return self.driver.find_elements(*locator)

        except Exception as e:
            print(f"[ERROR] find_elements_list failed | {e}")

        return []

    # ---------------------------------------------------------
    # Navigate Back
    # ---------------------------------------------------------

    def nav_to_previous(self):

        try:
            self.driver.back()

            print("[INFO] Navigated back")

        except Exception as e:
            print(f"[ERROR] nav_to_previous failed | {e}")

    # ---------------------------------------------------------
    # Refresh Page
    # ---------------------------------------------------------

    def refresh(self):

        try:
            self.driver.refresh()

            print("[INFO] Page refreshed")

        except Exception as e:
            print(f"[ERROR] refresh failed | {e}")