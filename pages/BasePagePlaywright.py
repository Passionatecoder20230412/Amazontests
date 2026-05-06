from playwright.sync_api import Page, expect


class BasePagePlaywright:
    """
    BasePage class
    ----------------
    Contains reusable methods for all pages.
    Every page class should inherit this.
    """

    def __init__(self, page: Page):
        self.page = page

    # ---------------------------
    # 🔹 Element Actions
    # ---------------------------

    def find_element(self, locator: str):
        """
        Returns locator object
        (Playwright works with locator instead of WebElement)
        """
        return self.page.locator(locator)

    def find_elements(self, locator: str):
        """
        Returns list of elements
        """
        return self.page.locator(locator).all()

    def click_button(self, locator: str):
        """
        Click on element
        Auto-wait handled by Playwright
        """
        self.page.click(locator)

    def enter_text(self, locator: str, text: str):
        """
        Fill input field (clears automatically before typing)
        """
        self.page.fill(locator, text)

    def append_text(self, locator: str, text: str):
        """
        Type text without clearing existing value
        """
        self.page.type(locator, text)

    # ---------------------------
    # 🔹 Getters
    # ---------------------------

    def get_text(self, locator: str) -> str:
        """
        Get visible text of element
        """
        return self.page.text_content(locator)

    def get_title(self) -> str:
        """
        Get page title
        """
        return self.page.title()

    def get_attribute(self, locator: str, attr: str):
        """
        Get attribute value
        """
        return self.page.get_attribute(locator, attr)

    # ---------------------------
    # 🔹 Waits (Optional - Playwright auto waits)
    # ---------------------------

    def wait_for_element_visible(self, locator: str, timeout: int = 5000):
        """
        Wait until element is visible
        """
        self.page.wait_for_selector(locator, state="visible", timeout=timeout)

    def wait_for_element_attached(self, locator: str, timeout: int = 5000):
        """
        Wait until element is present in DOM
        """
        self.page.wait_for_selector(locator, state="attached", timeout=timeout)

    # ---------------------------
    # 🔹 Validations / Checks
    # ---------------------------

    def is_visible(self, locator: str) -> bool:
        """
        Check element visibility
        """
        return self.page.is_visible(locator)

    def is_enabled(self, locator: str) -> bool:
        """
        Check if element is enabled
        """
        return self.page.is_enabled(locator)

    # ---------------------------
    # 🔹 Dropdown Handling
    # ---------------------------

    def select_by_text(self, locator: str, text: str):
        """
        Select dropdown by visible text
        """
        self.page.select_option(locator, label=text)

    def select_by_value(self, locator: str, value: str):
        """
        Select dropdown by value
        """
        self.page.select_option(locator, value=value)

    # ---------------------------
    # 🔹 Navigation
    # ---------------------------

    def navigate_to(self, url: str):
        """
        Open URL
        """
        self.page.goto(url)

    def refresh_page(self):
        """
        Refresh current page
        """
        self.page.reload()

    def go_back(self):
        """
        Navigate back
        """
        self.page.go_back()

    # ---------------------------
    # 🔹 Keyboard Actions
    # ---------------------------

    def press_key(self, locator: str, key: str):
        """
        Press keyboard key (e.g., Enter, Tab)
        """
        self.page.press(locator, key)

    # ---------------------------
    # 🔹 Mouse Actions
    # ---------------------------

    def hover_element(self, locator: str):
        """
        Hover over element
        """
        self.page.hover(locator)

    # ---------------------------
    # 🔹 Scroll
    # ---------------------------

    def scroll_to_element(self, locator: str):
        """
        Scroll element into view
        """
        self.page.locator(locator).scroll_into_view_if_needed()

    # ---------------------------
    # 🔹 Frames
    # ---------------------------

    def switch_to_frame(self, frame_name: str):
        """
        Switch to iframe
        """
        return self.page.frame(name=frame_name)

    # ---------------------------
    # 🔹 Alerts / Dialogs
    # ---------------------------

    def accept_alert(self):
        """
        Accept alert
        """
        self.page.on("dialog", lambda dialog: dialog.accept())

    def dismiss_alert(self):
        """
        Dismiss alert
        """
        self.page.on("dialog", lambda dialog: dialog.dismiss())

    # ---------------------------
    # 🔹 File Upload
    # ---------------------------

    def upload_file(self, locator: str, file_path: str):
        """
        Upload file
        """
        self.page.set_input_files(locator, file_path)

    # ---------------------------
    # 🔹 Screenshot
    # ---------------------------

    def take_screenshot(self, path: str = "screenshot.png"):
        """
        Capture screenshot
        """
        self.page.screenshot(path=path)
