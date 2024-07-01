import requests
import json

URL = 'http://127.0.0.1:5000/house'
ITEM_ID = None


def test_insert_in_house():
    global ITEM_ID

    data_to_send = {'adress': '640978, Новосибирск, ул. Ватутина 12а к67 кв 87',
                    'cadastr_number': '123123123', 'id_client': 46831, 'is_actual': 0}

    response = requests.post(URL, json=data_to_send)

    response_json = response.json()
    ITEM_ID = response_json["id_house"]
    print("Ответ от сервера:")
    print(json.dumps(response_json, indent=4))

    assert response_json["id_house"] != None
    assert response_json["status_code"] == 200


def test_update_in_house():
    data_to_send = {'id_house': ITEM_ID, 'adress': '640978, Новосибирск, ул. Ватутина 12б к69 кв 88',
                    'cadastr_number': '123223223', 'id_client': 46831, 'is_actual': 1}

    response = requests.put(URL, json=data_to_send)

    response_json = response.json()
    print("Ответ от сервера:")
    print(json.dumps(response_json, indent=4))

    assert response_json["status_code"] == 200


def test_delete_from_house():
    data_to_send = {'id_house': ITEM_ID}

    response = requests.delete(URL, json=data_to_send)

    response_json = response.json()
    print("Ответ от сервера:")
    print(json.dumps(response_json, indent=4))

    assert response_json["status_code"] == 200
