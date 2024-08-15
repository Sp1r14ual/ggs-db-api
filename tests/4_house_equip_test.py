import requests
import json
from get_auth_token import get_auth_token

URL = 'http://127.0.0.1:5000/house_equip'
AUTH_TOKEN = get_auth_token()
ITEM_ID = None
ID_HOUSE = 140029
ID_PERSON = 623

def test_insert_in_house_equip():
    global ITEM_ID

    data_to_send = {'id_client': ID_PERSON, 'id_house': ID_HOUSE, 'id_type_house_equip': 4,
                    'year_produce': 2077, 'remark': 'blablabla'}

    response = requests.post(URL, json=data_to_send, headers={
                             'Authorization': f'Bearer {AUTH_TOKEN}'})

    response_json = response.json()
    ITEM_ID = response_json["id_house_equip"]
    print("Ответ от сервера:")
    print(json.dumps(response_json, indent=4))

    assert response_json["id_house_equip"] != None
    assert response_json["status_code"] == 200


def test_update_in_house_equip():
    data_to_send = {'id_house_equip': ITEM_ID, 'id_house': ID_HOUSE, 'id_type_house_equip': 3,
                    'year_produce': 2069, 'remark': 'bimbimbimbambambam'}

    response = requests.put(URL, json=data_to_send, headers={
        'Authorization': f'Bearer {AUTH_TOKEN}'})

    response_json = response.json()
    print("Ответ от сервера:")
    print(json.dumps(response_json, indent=4))

    assert response_json["status_code"] == 200


def test_delete_from_house_equip():
    data_to_send = {'id_house_equip': ITEM_ID, 'id_house': ID_HOUSE}

    response = requests.delete(URL, json=data_to_send, headers={
        'Authorization': f'Bearer {AUTH_TOKEN}'})

    response_json = response.json()
    print("Ответ от сервера:")
    print(json.dumps(response_json, indent=4))

    assert response_json["status_code"] == 200
