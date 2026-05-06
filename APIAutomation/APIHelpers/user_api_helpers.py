
import requests

from APIAutomation.APIObjects.user_api_objects import UserApiObjects


class UserApiHelpers(UserApiObjects):
    baseurl = UserApiObjects.baseurl + UserApiObjects.path_param
    def post_api(self,endpoint,data=None):
        # baseurl=UserApiObjects.baseurl+UserApiObjects.path_param
        url=self.baseurl+endpoint
        resp=requests.post(url=url,data=data)
        return resp
    def get_api(self,endpoint,params=None):
        url = self.baseurl+endpoint
        resp=requests.get(url=url,params=params)
        return resp
    def put_api(self,endpoint,data=None):
        url=self.baseurl+endpoint
        resp=requests.put(url=url,data=data)
        return resp
    def delete_api(self,endpoint,data=None):
        url=self.baseurl+endpoint
        resp=requests.delete(url=url,data=data)
        return resp
