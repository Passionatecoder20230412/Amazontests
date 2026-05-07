# conftest.py

import pytest
from selenium import webdriver

from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def pytest_addoption(parser):

    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser name: chrome / edge / firefox"
    )

    parser.addoption(
        "--url",
        action="store",
        default="https://www.amazon.in/",
        help="Application URL"
    )

    parser.addoption(
        "--headless",
        action="store_true",
        help="Run tests in headless mode"
    )


@pytest.fixture(scope="function")
def init_driver(request):

    browser = request.config.getoption("--browser").lower()
    url = request.config.getoption("--url")
    headless = request.config.getoption("--headless")

    driver = None

    # ---------- CHROME ---------- #

    if browser == "chrome":

        options = ChromeOptions()

        if headless:
            options.add_argument("--headless=new")

        options.add_argument("--start-maximized")

        driver = webdriver.Chrome(options=options)

    # ---------- EDGE ---------- #

    elif browser == "edge":

        options = EdgeOptions()

        if headless:
            options.add_argument("--headless=new")

        options.add_argument("--start-maximized")

        driver = webdriver.Edge(options=options)

    # ---------- FIREFOX ---------- #

    elif browser == "firefox":

        options = FirefoxOptions()

        if headless:
            options.add_argument("--headless")

        driver = webdriver.Firefox(options=options)
        driver.maximize_window()

    else:
        raise Exception(f"Unsupported browser: {browser}")

    # Common setup
    driver.implicitly_wait(10)
    driver.get(url)

    yield driver

    print("Closing browser...")
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