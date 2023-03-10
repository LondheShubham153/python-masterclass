"""
Requests library
This library is used to make HTTP requests in Python.
"""
import requests

def api_check():
    url = "https://reqres.in/api/users"
    response = requests.get(url)
    if response.status_code == 200:
        return True
    else:
        return False

print(api_check())