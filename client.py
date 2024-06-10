import requests
import json

# URL сервера, куда отправляем запрос
url = 'http://127.0.0.1:5000/delete_person'

# JSON данные для отправки
# data_to_send = {'id_house': 140042, 'adress': '640978, Новосибирск, ул. Ватутина 12а к67 кв 87',
#                 'cadastr_number': '123123123', 'id_client': 46831, 'is_actual': 0}

data_to_send = {}

# Отправляем POST запрос с JSON данными
response = requests.delete(url, json=data_to_send)

response_json = response.json()
print("Ответ от сервера:")
print(json.dumps(response_json, indent=4))
