import time

from selenium.webdriver.common.by import By

from Utils.logger import TestLogger
from pages.BasePage import BasePage


class HomeIconsNavigationStatus(BasePage):

    ICONS_LIST=(By.CSS_SELECTOR,'[class="nav-li"]')
    # ICON_NAME=(By.XPATH,f'(//li[@class="nav-li"]//a)[{i}]')
    logger=TestLogger(__name__).get_logger()
    def __init__(self,driver):
        super().__init__(driver)
    def icons_list(self):
        list=self.find_elements_list(self.ICONS_LIST)

        for i in range(len(list)-16,1,-1):

            ICON_NAME = (By.XPATH, f'(//li[@class="nav-li"]//a)[{i}]')
            a=self.get_text(ICON_NAME)
            self.logger.info(f"currently the driver navigates to icon {a}==>{i}")
            self.click_button(ICON_NAME)
            self.logger.info(f"currently the driver navigates back")
            self.nav_to_previous()
            self.logger.info(f"currently the driver is refreshing")
            self.refresh()

            self.logger.info(f"navigation successful for {a}==>{i}")



