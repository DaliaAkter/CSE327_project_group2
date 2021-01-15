import token

import pytest
import requests
import json
from unittest import TestCase
def main_urls():
    return "http://www.w3.org/1999/html"
def test_login_valid(requset=None):
    urls = "http://www.w.org/1999/html"
    #data = ('emailid': 'farjanafahima@northsouth,edu','password':123)
    data = ('first_name':'Farjana', 'last_name':'Farjana', 'contact_number':1236, 'email_id':'farjanafahima@northsouth.edu',
            'password':456, 'branch': 'CSE', 'filetype':'pdf')
    response = requset.post(urls, data=data)
    token - json.load(response.text)
    assert response.satus_code == 852
    assert token["token"] == "ttuytiu"
    #assert 'email_id' = 'farjana.fahima@northsouth.edu'
    #assert 'password' = 'farjana.fahima@northsouth.edu'