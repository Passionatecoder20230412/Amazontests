from APIAutomation.Utilities.DeleteUserDetails import DeleteUserDetails
from Utils.logger import TestLogger

"""
API test delete account fields
response 200 ,
message : account deleted!
"""
class TestDeleteAccount:
    data={
        "email":"radbjjkjvijay2456@gmail.com",
        "password":"vijay80741",
    }
    def test_delete_account(self):

        delete_ac=DeleteUserDetails()
        resp=delete_ac.delete_user_details(data=self.data)
        print(resp.json())
        print(resp.text)
        print(resp.status_code)
        print(resp.json()["message"])
        assert resp.status_code == 200
        assert resp.json()["message"] =="Account deleted!","Account not found!"


