import pytest

from Utils.excel_utils import get_excel_data
from pages.CreateAccountPage import CreateAccount
# test_data=get_excel_data(file_path)
@pytest.mark.parametrize("name,email,password,day,month,year,first_name,last_name,company,address,address2,country,state,city,zipcode,mobile_number",[("vijay","radbjjkjvijay@gmail.com","vjk80741","12","April","2001","VIJAY","ANEGONDI","FAKE COMPANY","KURAGANI PALLI","NARPALA","India","AP","ANANTAPUR",515425,8074174770),("vijay2","radbjjkjvijay2@gmail.com","vijay80741","27","February","2000","VIJAY2","ANEGONDI2","FAKE COMPANY2","KURAGANI PALLI2","NARPALA2","India","AP2","ANANTAPUR2",5154252,80741747702)])
# @pytest.mark.parametrize("name,email,password,day,month,year",test_data)
class TestCreateAccount:

    def test_create_account(self,init_driver,name,email,password,day,month,year,first_name,last_name,company,address,address2,country,state,city,zipcode,mobile_number):
        create_account = CreateAccount(init_driver)
        text=create_account.home_text()
        assert text == "Automation Exercise","Wrong Home text"
        create_account.click_signup()
        text=create_account.new_account_text()
        assert text=="New User Signup!","failed"
        create_account.new_use_visible()
        create_account.user_details(name,email,password,day,month,year,first_name,last_name,company,address,address2,country,state,city,zipcode,mobile_number)



