import pytest
from pages.LoginWithValidInvalidDetails import LoginWithValidInvalidDetails
from Utils.logger import TestLogger

@pytest.mark.parametrize(
    "email,password",
    [
        ("7207962483", "Vijay@8500"),
        ("7207962483", "vijay8500")
    ]
)
@pytest.mark.login
class TestLoginValidInvalid:

    def test_login_valid_invalid(self, init_driver, email, password):
        logger = TestLogger(__name__).get_logger()

        logger.info("===== Test Started =====")
        logger.info(f"Test data -> Email: {email}, Password: {password}")

        login = LoginWithValidInvalidDetails(init_driver)

        logger.info("Opening URL")
        login.get_url()

        logger.info("Performing login action")
        login.login_check(email, password)

        logger.info("Fetching result text")
        a = login.assert_text()

        logger.info(f"Result text received: {a}")

        print("done")  # you can remove later

        logger.info("Validating login result")
        assert a == "Sign Out", "Login Failed"

        logger.info("Re-validating login result (second assertion)")
        assert login.assert_text() == "Sign Out", "Login Failed"

        logger.info("===== Test Completed Successfully =====")
        print("done")