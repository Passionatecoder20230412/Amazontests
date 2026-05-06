# APIAutomation/TestData/user_test_data.py
import time


class UserData:

    create_account= {
        "name": "madhu",
        "email":"msnpython@gmail.com",
        "password": "vijay@8500",
        "title": "Mr",
        "birth_date": "16",          # ✅ fixed key
        "birth_month": "6",
        "birth_year": "2024",
        "firstname": "python",       # ✅ fixed key
        "lastname": "testing",       # ✅ fixed key
        "company": "msn python automation testing",
        "address1": "Marathalli",
        "address2": "Dental college road",
        "country": "India",
        "state": "KA",
        "city": "Bangalore",
        "zipcode": "560036",
        "mobile_number": "9999999999"   # ✅ added (required)
    }