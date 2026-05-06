
from APIAutomation.APIHelpers.user_api_helpers import UserApiHelpers


class DeleteUserDetails(UserApiHelpers):
    def delete_user_details(self,data=None):
        resp=self.delete_api(self.DELETE_ACCOUNT,data=data)
        return resp

