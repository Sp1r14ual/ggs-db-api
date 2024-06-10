import requests
import json


def test_insert_in_house():
    # URL сервера, куда отправляем запрос
    global ITEM_ID
    url = 'http://127.0.0.1:5000/add_house'

    data_to_send = {'adress': '640978, Новосибирск, ул. Ватутина 12а к67 кв 87',
                    'cadastr_number': '123123123', 'id_client': 46831, 'is_actual': 0}

    # Отправляем POST запрос с JSON данными
    response = requests.post(url, json=data_to_send)

    response_json = response.json()
    ITEM_ID = response_json["id_house"]
    print("Ответ от сервера:")
    print(json.dumps(response_json, indent=4))

    assert response_json["id_house"] != None
    assert response_json["status_code"] == 200


def test_update_in_house():
    # URL сервера, куда отправляем запрос
    url = 'http://127.0.0.1:5000/edit_house'

    data_to_send = {'id_house': ITEM_ID, 'adress': '640978, Новосибирск, ул. Ватутина 12б к69 кв 88',
                    'cadastr_number': '123223223', 'id_client': 46831, 'is_actual': 1}

    # Отправляем POST запрос с JSON данными
    response = requests.put(url, json=data_to_send)

    response_json = response.json()
    print("Ответ от сервера:")
    print(json.dumps(response_json, indent=4))

    assert response_json["status_code"] == 200


def test_delete_from_house():
    # URL сервера, куда отправляем запрос
    url = 'http://127.0.0.1:5000/delete_house'

    data_to_send = {'id_house': ITEM_ID}

    # Отправляем POST запрос с JSON данными
    response = requests.delete(url, json=data_to_send)

    response_json = response.json()
    print("Ответ от сервера:")
    print(json.dumps(response_json, indent=4))

    assert response_json["status_code"] == 200
