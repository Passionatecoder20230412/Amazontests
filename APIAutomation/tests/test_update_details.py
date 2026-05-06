from APIAutomation.TestData.user_test_data import UserData
from APIAutomation.Utilities.UpdateUserDetails import UpdateUserDetail


class TestUpdateDetails:
    payload={

      "name": "vijay",
      "email": "radbjjkjvijay@gmail.com",
      "password": "vjk80741",
      "title": "Mr",
      "birth_date": "12",
      "birth_month": "April",
      "birth_year": "2001",
      "firstname": "VIJAY",
      "lastname": "ANEGONDI",
      "company": "FAKE COMPANY",
      "address1": "KURAGANI PALLI123456",
      "address2": "NARPALA8500 v ",
      "country": "India",
      "zipcode": "515425",
      "state": "AP",
      "city": "ANANTAPUR",
      "mobile_number": "8074174770"}

    def test_update_user_details(self):
        update=UpdateUserDetail()
        resp=update.update_user_details(data=self.payload)
        print(resp.status_code,"0")
        print(resp,"1")
        print(resp.json(),"2")
        print(resp.text,"3")
        print("**************")
