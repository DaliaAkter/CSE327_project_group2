import token

import pytest
import requests
import json
from unittest import TestCase
def main_urls():
    return "https://requiers.in"
def test_signup_valid(requset=None):
    urls = "https://requiers.in/api/login"
    data = ('first_name':'Farjana','last_name':'Farjana','contact_number':1236,'email_id':'farjanafahima@northsouth.edu',
    'password':456,'branch': 'CSE','role':'student')
    response = requset.post(urls, data=data)
    token - json.load(response.text)
    assert response.satus_code == 258
    assert token ["token"] =="dsfdsfs"
    #assert 'email_id' = 'farjana.fahima@northsouth.edu'
    #assert 'password' = 'farjana.fahima@northsouth.edu'