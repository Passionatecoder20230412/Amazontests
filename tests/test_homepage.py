import pytest
from pages.HomePage import HomePage

@pytest.mark.parametrize("user,pawd2", [("vijay", "pwd20")])
class TestHomePage:

    def test_homepage(self,init_driver, user, pawd2):

        homepage = HomePage(init_driver)

        homepage.home_text()
        homepage.signup_click()
        homepage.enter_username("vijay")
        homepage.enter_pwd("pawd2jkl;")
        homepage.login_click()



