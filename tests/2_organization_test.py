import requests
import json
from get_auth_token import get_auth_token

URL = 'http://127.0.0.1:5000/organization'
ITEM_ID = None
AUTH_TOKEN = get_auth_token()


def test_insert_in_organization():
    global ITEM_ID

    data_to_send = {'name': 'ООО Рога и Копыта',
                    'adress_jur': '640098, Новосибирская область, г Новосибирск, Октябрьская ул, д. 42, этаж цоколь',
                    'adress_fact': '640098, Новосибирская область, г Новосибирск, Октябрьская ул, д. 42, этаж цоколь',
                    'remark': 'blabla', 'inn': '4564564564', 'kpp': '345345333', 'from_1c': 0}

    response = requests.post(URL, json=data_to_send, headers={
                             'Authorization': f'Bearer {AUTH_TOKEN}'})

    response_json = response.json()
    ITEM_ID = response_json["id_organization"]

    assert response_json["id_organization"] is not None
    assert response.status_code == 201


def test_update_in_organization():
    data_to_send = {'organization_id': ITEM_ID, 'name': 'ООО Копыта и Рога',
                    'adress_jur': '640098, Новосибирская область, г Новосибирск, Октябрьская ул, д. 42, этаж цоколь',
                    'adress_fact': '640098, Новосибирская область, г Новосибирск, Октябрьская ул, д. 42, этаж цоколь',
                    'remark': 'blabla123321', 'inn': '33333', 'kpp': '44444', 'from_1c': 0}

    response = requests.put(URL, json=data_to_send, headers={
        'Authorization': f'Bearer {AUTH_TOKEN}'})

    assert response.status_code == 200, response.json()


def test_delete_from_organization():
    data_to_send = {'id_organization': ITEM_ID}

    response = requests.delete(URL, json=data_to_send, headers={
        'Authorization': f'Bearer {AUTH_TOKEN}'})

    assert response.status_code == 200, response.json()
