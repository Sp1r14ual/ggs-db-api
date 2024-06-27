import requests
import json

ITEM_ID = None


def test_insert_in_organization():
    # URL сервера, куда отправляем запрос
    global ITEM_ID
    url = 'http://127.0.0.1:5000/add_organization'

    data_to_send = {'name': 'ООО Рога и Копыта',
                    'adress_jur': '640098, Новосибирская область, г Новосибирск, Октябрьская ул, д. 42, этаж цоколь',
                    'adress_fact': '640098, Новосибирская область, г Новосибирск, Октябрьская ул, д. 42, этаж цоколь',
                    'remark': 'blabla', 'inn': '4564564564', 'kpp': '345345333', 'from_1c': 0}

    # Отправляем POST запрос с JSON данными
    response = requests.post(url, json=data_to_send)

    response_json = response.json()
    ITEM_ID = response_json["id_organization"]
    print("Ответ от сервера:")
    print(json.dumps(response_json, indent=4))

    assert response_json["id_organization"] != None
    assert response_json["status_code"] == 200


def test_update_in_organization():
    # URL сервера, куда отправляем запрос
    url = 'http://127.0.0.1:5000/edit_organization'

    data_to_send = {'organization_id': ITEM_ID, 'name': 'ООО Копыта и Рога',
                    'adress_jur': '640098, Новосибирская область, г Новосибирск, Октябрьская ул, д. 42, этаж цоколь',
                    'adress_fact': '640098, Новосибирская область, г Новосибирск, Октябрьская ул, д. 42, этаж цоколь',
                    'remark': 'blabla123321', 'inn': '33333', 'kpp': '44444', 'from_1c': 0}

    # Отправляем POST запрос с JSON данными
    response = requests.put(url, json=data_to_send)

    response_json = response.json()
    print("Ответ от сервера:")
    print(json.dumps(response_json, indent=4))

    assert response_json["status_code"] == 200


def test_delete_from_organization():
    # URL сервера, куда отправляем запрос
    url = 'http://127.0.0.1:5000/delete_organization'

    data_to_send = {'id_organization': ITEM_ID}

    # Отправляем POST запрос с JSON данными
    response = requests.delete(url, json=data_to_send)

    response_json = response.json()
    print("Ответ от сервера:")
    print(json.dumps(response_json, indent=4))

    assert response_json["status_code"] == 200
