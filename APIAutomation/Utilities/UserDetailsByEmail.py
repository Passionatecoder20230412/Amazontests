from APIAutomation.APIHelpers import user_api_helpers
from APIAutomation.APIHelpers.user_api_helpers import UserApiHelpers
from APIAutomation.APIObjects import user_api_objects


class UserDetailsByEmail(UserApiHelpers):
    def get_user_details_email(self,params=None):
        return self.get_api(self.GET_USER_BY_EMAIL,params=params)


