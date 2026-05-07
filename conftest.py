import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):

    parser.addoption(
        "--url",
        action="store",
        default="https://www.amazon.in/",
        help="Application URL"
    )

    parser.addoption(
        "--headless",
        action="store_true",
        help="Run in headless mode"
    )


@pytest.fixture(scope="function")
def init_driver(request):

    url = request.config.getoption("--url")
    headless = request.config.getoption("--headless")

    options = Options()

    # headless only if passed
    if headless:
        options.add_argument("--headless=new")

    options.add_argument("--start-maximized")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)

    # driver.implicitly_wait(10)
    driver.get(url)

    yield driver

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
