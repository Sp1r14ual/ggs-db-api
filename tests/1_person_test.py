import requests
import json

ITEM_ID = None


def test_insert_in_person():
    # URL сервера, куда отправляем запрос
    global ITEM_ID
    url = 'http://127.0.0.1:5000/add_person'

    data_to_send = {'family_name': 'Drozdenko',
                    'name': 'Sergey', 'birthdate': '20.01.2001', 'phone_number': '89138946221'}

    # Отправляем POST запрос с JSON данными
    response = requests.post(url, json=data_to_send)

    response_json = response.json()
    ITEM_ID = response_json["id_client"]
    print("Ответ от сервера:")
    print(json.dumps(response_json, indent=4))

    assert response_json["id_client"] != None
    assert response_json["status_code"] == 200


def test_update_in_person():
    # URL сервера, куда отправляем запрос
    url = 'http://127.0.0.1:5000/edit_person'

    data_to_send = {'client_id': ITEM_ID, 'family_name': 'Drozdenko',
                    'name': 'Sergey', 'birthdate': '20.01.2003', 'phone_number': '89138946222'}

    # Отправляем POST запрос с JSON данными
    response = requests.put(url, json=data_to_send)

    response_json = response.json()
    print("Ответ от сервера:")
    print(json.dumps(response_json, indent=4))

    assert response_json["status_code"] == 200


def test_delete_from_person():
    # URL сервера, куда отправляем запрос
    url = 'http://127.0.0.1:5000/delete_person'

    data_to_send = {'id_client': ITEM_ID}

    # Отправляем POST запрос с JSON данными
    response = requests.delete(url, json=data_to_send)

    response_json = response.json()
    print("Ответ от сервера:")
    print(json.dumps(response_json, indent=4))

    assert response_json["status_code"] == 200
