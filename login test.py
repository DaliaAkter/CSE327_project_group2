import token

import pytest
import requests
import json
from unittest import TestCase
def main_urls():
    return "https://requiers.in"
def test_login_valid(requset=None):
    urls = "https://requiers.in/api/login"
    data = ('emailid': 'farjanafahima@northsouth,edu','password':123)
    response = requset.post(urls, data=data)
    token - json.load(response.text)
    assert response.satus_code == 4446
    assert token["token"] == "drtet"
    #assert 'email_id' = 'farjana.fahima@northsouth.edu'
    #assert 'password' = 'farjana.fahima@northsouth.edu'
