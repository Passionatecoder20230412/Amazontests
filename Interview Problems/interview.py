"""
Problem 1:
    # UI Login Automation (Robot Framework)
    # Design a Robot Framework test case to:
    # Open a browser and navigate to a URL
    # Enter username and password
    # Click the login button
    # Verify login is successful (any validation)
    # Close the browser
def login(username,password):
    driver=webdriver.Chrome()
    driver.get(url)
    driver.maximize_window()
    driver.find_element(By.ID,"username").send_keys(username)
    driver.find_element(By.ID,"password").send_keys(password)
    driver.find_element(By.ID,"password")
    driver.find_element(By.ID,"login").click()
    text=driver.find_element(By.ID,"login_success_text").text
    assert text="login successful","login failed"
    driver.quit()

"""
import pytest
from selenium.webdriver.common.by import By

"""
Problem 4: API Login Automation

    # Write a test case using API automation to:
    # Create a session
    # Send login request using POST
    # Pass username and password in request body
    # Validate response status code
    # Validate response contains success message
    def login(url,username,password):
        payload={"username":username,"password":password}
        resp=requests.post(url=url,json=payload)
        assert resp.status_code == 200
        assert resp.json()["message"]="login successful","login failed"
        return resp
"""
"""Problem 5: Python Multiple Inheritance
    # Given three classes:
    # Class A
    # Class B
    # Class C inherits from A and B
class A:
    def bell(self):
        return "bell of class A"
class B:
    def bell(self):
        return "bell of class B"
class C(A,B):
    def bell2(self):
        return "bell of class C"

obj=C()
print(obj.bell())
print(mro)
"""
"""
Problem 7: List Operations
    Given two lists:
    a = [1, 2]
    b = [2, 3]
    👉 Write a problem to:
    Combine both lists
    Remove duplicates
    Maintain sorted order
l1=[1,2,3,10,8,25,63,7]
l2=[8,45,14,23,6,86,45]
l1.extend(l2)
l=set(l1)
l=list(l)
print(sorted(l))
"""
"""
List Comprehension
Given a list:
l = [1, 2, 3, 4, 5, 6]
👉 Write problems to:
Extract even numbers
Extract odd numbers
Create a list of squares
Create a dictionary mapping number → square

l= [1, 2, 3, 4, 5, 6]
l1=[i for i in l if i%2==0]
l2=[i for i in l if i%2!=0]
d={i:i*i for i in l}
print(l1,l2,d,sep="\n")
"""
"""
Problem 9: Debugging Selenium Issue
Scenario:Login button is not clickable
===>wrong locator,handling waits
"""
"""
Problem 10: Hybrid Automation Framework
    Design a problem statement to:
    Combine UI automation + API automation
    Use common test data
    Implement logging
    Structure project using best practices

import requests
@pytest.mark.parametrize("username,password",[("radbjjkjvijay2456@gmail.com","vijay80741"),("radbjjkjvijay2456@gmail.com","vijay80742")])
def test_login_automation_api(init_driver,username,password):
    driver=init_driver
    driver.find_element(By.CSS_SELECTOR,'[href="/login"]').click()
    driver.find_element(By.CSS_SELECTOR,'[data-qa="login-email"]').send_keys(username)
    driver.find_element(By.CSS_SELECTOR,'[data-qa="login-password"]').send_keys(password)
    driver.find_element(By.CSS_SELECTOR,'[data-qa="login-button"]').click()
    driver.quit()
    #api
    url="https://automationexercise.com/api/verifyLogin"
    data={"email":username,"password":password}

    resp=requests.post(url=url,data=data)
    assert resp.status_code == 200
    print(resp.json()["message"])#"User exists!"
"""
"""
    text = "qawsedfrweqaswdrtg"
    substrings = [text[i:j] for i in range(len(text)) for j in range(i+1, len(text)+1)]
    b=[]
    for i in substrings:
        if len(i)==len(set(i)):
            b.append(i)
            
    d={len(i):i for i in b}
    print(d)
    max=max(d.keys())
    print(max,d[9])
"""
