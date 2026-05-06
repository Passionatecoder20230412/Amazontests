from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestPage:

    def test_page(self,init_driver):
        self.driver = init_driver
        self.driver.find_element(By.XPATH,'//a[@href="/login"]').click()
        self.wait=WebDriverWait(self.driver,10,ignored_exceptions=[NoSuchElementException])
        try:
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'[data-qa="signup-nam"]'))).send_keys("vijay anegondi")
        except Exception as e:
            print(e)

