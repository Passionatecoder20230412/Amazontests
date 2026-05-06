from APIAutomation.Utilities.VerifyLoginWithoutEmail import VerifyLoginWithoutEmail


class TestLoginWithoutEmail:
    # data={
    #     "email":"",
    #     "password":""
    # }
    def test_login_without_email(self,data=None):
        login=VerifyLoginWithoutEmail()
        resp=login.login_without_email(data=data)
        print(resp)
        print(resp.json())
        assert resp.status_code == 200,"status code should be 200"
        assert resp.json()["message"] == 'Bad request, email or password parameter is missing in POST request.'
