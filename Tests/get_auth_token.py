import requests
import json

URL = 'http://127.0.0.1:5000/login'
LOGIN = "test_avrunev"
SEND_DATA = {"login": LOGIN}


def get_auth_token():
    return requests.post(URL, json=SEND_DATA).json()["access_token"]
