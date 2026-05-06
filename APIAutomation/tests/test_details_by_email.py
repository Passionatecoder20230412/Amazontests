import pytest

from APIAutomation.APIObjects.user_api_objects import UserApiObjects
from APIAutomation.Utilities.UserDetailsByEmail import UserDetailsByEmail


@pytest.mark.parametrize("email",["msnpython@gmail.com","msnpython123@gmail.com"])
class TestEmailDetails(UserDetailsByEmail):
    def test_email(self,email):
        print("lets start")
        params={"email":email}
        resp=self.get_user_details_email(params=params)
        print(resp)
        print(resp.json())
        print("lets end")