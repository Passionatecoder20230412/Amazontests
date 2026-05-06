import pytest

from Utils.logger import TestLogger
from pages.RegisterWithExistingMail import RegisterWithExistingMail
@pytest.mark.existing
@pytest.mark.parametrize("email_num", ["7207962483","anegondi20004000@gmail.com"])
class TestUserExistingStatus:

    def test_user_existing_status(self,init_driver,email_num):
        logger = TestLogger(__name__).get_logger()
        user_status=RegisterWithExistingMail(init_driver)
        user_status.web_link()
        result=user_status.register_with_existing_mail(email_num)
        print(result)
        if result=="EXISTING USER":
            print("EXISTING USER------------***********")
        elif result=="NEW USER":
            print("NEW USER--------------------************")
        else:
            print("Bye")

        logger.info("Happy ending")


