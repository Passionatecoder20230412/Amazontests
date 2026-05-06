from APIAutomation.TestData.user_test_data import UserData
from APIAutomation.Utilities.user_create_account import CreateAccount


class TestUserCreate:

    def test_user_created(self):
        create_acc = CreateAccount()
        resp=create_acc.create_account(payload=UserData.create_account)
        print(resp.text)
        print(resp.status_code)
        assert resp.status_code == 200,"not created successfully"
        assert resp.json()["responseCode"]==201, "Account Not created successfully"
        assert resp.json()["message"]=="User created!",f"Account not created successfully{resp.json()['message']}"








