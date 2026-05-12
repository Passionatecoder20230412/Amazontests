from APIAutomation.APIHelpers.user_api_helpers import UserApiHelpers


class PatchUpdate(UserApiHelpers):
    def patch_update(self,json=None):
        resp=self.patch_api(self.PATCH_API_USER,json=json)
        return resp
