import requests
import json
from get_auth_token import get_auth_token

URL = 'http://127.0.0.1:5000/person'
ITEM_ID = None
AUTH_TOKEN = get_auth_token()


def test_insert_in_person():
    global ITEM_ID

    data_to_send = {'family_name': 'Panasenko',
                    'name': 'Sergey', 'birthdate': '20.01.2001', 'phone_number': '89138946221'}

    response = requests.post(URL, json=data_to_send, headers={
                             'Authorization': f'Bearer {AUTH_TOKEN}'})

    response_json = response.json()
    ITEM_ID = response_json["id_client"]

    assert response_json["id_client"] is not None
    assert response.status_code == 201, response_json


def test_update_in_person():
    data_to_send = {'client_id': ITEM_ID, 'family_name': 'Drozdenko',
                    'name': 'Sergey', 'birthdate': '20.01.2003', 'phone_number': '89138946222'}

    response = requests.put(URL, json=data_to_send, headers={
        'Authorization': f'Bearer {AUTH_TOKEN}'})

    assert response.status_code == 200, response.json()


def test_delete_from_person():
    data_to_send = {'id_client': ITEM_ID}

    response = requests.delete(URL, json=data_to_send, headers={
        'Authorization': f'Bearer {AUTH_TOKEN}'})

    assert response.status_code == 200, response.json()
