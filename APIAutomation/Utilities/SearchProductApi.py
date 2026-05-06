from APIAutomation.APIHelpers.user_api_helpers import UserApiHelpers


class SearchProductApi(UserApiHelpers):

    def search_product_by_text(self,data=None):
        resp=self.post_api(self.SEARCH_PRODUCT,data=data)
        return resp