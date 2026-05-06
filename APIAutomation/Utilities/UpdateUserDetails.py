from APIAutomation.APIHelpers.user_api_helpers import UserApiHelpers


class UpdateUserDetail(UserApiHelpers):
    def update_user_details(self,data=None):
        resp=self.put_api(self.UPDATE_USER_DETAIL,data=data)
        return resp
