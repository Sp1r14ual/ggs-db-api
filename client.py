import requests
import json

# URL сервера, куда отправляем запрос
url = 'http://127.0.0.1:5000/add_house'

# JSON данные для отправки
data_to_send = {'adress': '640978, Новосибирск, ул. Ватутина 12а к67 кв 87',
                'cadastr_number': '123123123', 'id_client': 46831, 'is_actual': 1}

# Отправляем POST запрос с JSON данными
response = requests.post(url, json=data_to_send)

response_json = response.json()
print("Ответ от сервера:")
print(json.dumps(response_json, indent=4))
