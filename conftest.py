import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

CURRENT_URL = "https://www.amazon.in/"

@pytest.fixture(scope="function")
def init_driver():

    options = Options()

    # 🔥 REQUIRED for Jenkins / CI
    options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")

    # start chrome safely
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    driver.implicitly_wait(10)
    driver.get(CURRENT_URL)

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
