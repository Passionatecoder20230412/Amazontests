import pytest
from selenium import webdriver

# CURRENT_URL = "https://www.amazon.in/"
CURRENT_URL="https://automationexercise.com/"

@pytest.fixture(scope="function")  # default scope anyway
def init_driver():
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.implicitly_wait(300)
    driver.get(CURRENT_URL)

    yield driver

    print("closing browser")
    driver.quit()

# import pytest
# from playwright.sync_api import sync_playwright
#
# CURRENT_URL = "https://automationexercise.com/"
#
#
# @pytest.fixture(scope="function")   # same as your Selenium
# def init_page():
#     # Start Playwright
#     playwright = sync_playwright().start()
#
#     # Launch browser
#     browser = playwright.chromium.launch(headless=False)
#
#     # Create new context (like fresh browser profile)
#     context = browser.new_context(
#         viewport={"width": 1920, "height": 1080}
#     )
#
#     # Open new page (tab)
#     page = context.new_page()
#
#     # Navigate to URL
#     page.goto(CURRENT_URL)
#
#     # Yield page (same as driver)
#     yield page
#
#     # Teardown (same as quit)
#     print("closing browser")
#     context.close()
#     browser.close()
#     playwright.stop()