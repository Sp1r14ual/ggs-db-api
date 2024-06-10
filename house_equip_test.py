import requests
import json


def test_insert_in_house_equip():
    # URL сервера, куда отправляем запрос
    global ITEM_ID
    url = 'http://127.0.0.1:5000/add_house_equip'

    data_to_send = {'id_house': 140040, 'id_type_house_equip': 4,
                    'year_produce': 2077, 'remark': 'blablabla'}

    # Отправляем POST запрос с JSON данными
    response = requests.post(url, json=data_to_send)

    response_json = response.json()
    ITEM_ID = response_json["id_house_equip"]
    print("Ответ от сервера:")
    print(json.dumps(response_json, indent=4))

    assert response_json["id_house_equip"] != None
    assert response_json["status_code"] == 200


def test_update_in_house_equip():
    # URL сервера, куда отправляем запрос
    url = 'http://127.0.0.1:5000/edit_house_equip'

    data_to_send = {'id_house_equip': ITEM_ID, 'house_id': 140040, 'id_type_house_equip': 3,
                    'year_produce': 2069, 'remark': 'bimbimbimbambambam'}

    # Отправляем POST запрос с JSON данными
    response = requests.put(url, json=data_to_send)

    response_json = response.json()
    print("Ответ от сервера:")
    print(json.dumps(response_json, indent=4))

    assert response_json["status_code"] == 200


def test_delete_from_house_equip():
    # URL сервера, куда отправляем запрос
    url = 'http://127.0.0.1:5000/delete_house_equip'

    data_to_send = {'id_house_equip': ITEM_ID}

    # Отправляем POST запрос с JSON данными
    response = requests.delete(url, json=data_to_send)

    response_json = response.json()
    print("Ответ от сервера:")
    print(json.dumps(response_json, indent=4))

    assert response_json["status_code"] == 200
