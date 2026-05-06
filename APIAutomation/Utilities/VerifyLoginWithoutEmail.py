from APIAutomation import APIHelpers
from APIAutomation.APIHelpers.user_api_helpers import UserApiHelpers


class VerifyLoginWithoutEmail(UserApiHelpers):

    def login_without_email(self,data=None):
        resp=self.post_api(self.VERIFY_LOGIN,data=data)
        return resp