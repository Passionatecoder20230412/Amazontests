import requests


def test_new_dummy_api():
    resp=requests.get("https://aws.amazon.com/")
    if "html" in resp.text:
        print("it is web page resp{}")
