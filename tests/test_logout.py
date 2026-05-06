import pytest

from pages.LogoutAmazon import LogoutAmazon
@pytest.mark.logout
@pytest.mark.parametrize("email_num,password",[("7207962483","Vijay@8500")])
class TestLogout:
    def test_logout(self,init_driver,email_num,password):
        logout=LogoutAmazon(init_driver)
        re=logout.logout_user(email_num,password)
        print(re)
        a=re[0].split()
        print(a)
        assert re[0]=="Hello, Rajeswari","Login Failed"
        assert re[1]=="Sign in or create account","Logout Failed"