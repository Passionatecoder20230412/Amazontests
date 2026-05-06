from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v144.dom import get_attributes
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

class BasePage:
    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(self.driver,30)

    def find_element(self,locator):
        try:
            self.wait.until(EC.presence_of_element_located(*locator))
        except Exception as e:
            print(e, "ele exception")
    def find_elements(self,locator):
        return self.wait.until(EC.presence_of_all_elements_located(*locator))

    def enter_text(self,locator,text):
            return self.driver.find_element(*locator).send_keys(text)

    def click_button(self,locator):
        try:
            self.wait.until(EC.element_to_be_clickable(locator)).click()
        except Exception as e:
            print(e, "ele exception and ",False)

    def get_text(self,locator):
            a=self.driver.find_element(*locator).text
            print(a)
            return a
    def get_title(self):
        return self.driver.title
    def is_visible(self,locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def select_options_text(self,locator,text):
        ele=self.driver.find_element(*locator)
        opt=Select(ele)
        opt.select_by_visible_text(text)
    def get_attr_value(self,locator,text):
        attribute_value=self.driver.find_element(*locator).get_attribute(text)
        print(attribute_value)
        return attribute_value
    def switch_frames(self,locator):
        self.driver.switch_to.frame(self.driver.find_element(*locator))
    def current_url(self):
        return self.driver.current_url
    def mouse_hover(self,locator):
        ele=self.driver.find_element(*locator)
        ac=ActionChains(self.driver)
        ac.move_to_element(ele).perform()
    def ele_visible(self,locator):
        try:
            return self.driver.find_element(*locator).is_displayed()
        except:
            return False
    def find_elements_list(self,locator):
        return self.driver.find_elements(*locator)

    def nav_to_previous(self):
        self.driver.back()
    def refresh(self):
        self.driver.refresh()




