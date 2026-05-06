from APIAutomation.APIHelpers.user_api_helpers import UserApiHelpers
from APIAutomation.APIObjects.user_api_objects import UserApiObjects


class CreateAccount(UserApiHelpers):

    def create_account(self,payload):
        resp=self.post_api(UserApiObjects.create_account,payload)
        return resp
