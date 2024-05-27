import requests
import json

# URL сервера, куда отправляем запрос
url = 'http://127.0.0.1:5000/delete_house_equip'

# JSON данные для отправки
data_to_send = {'id_house_equip': 1432292}

# Отправляем POST запрос с JSON данными
response = requests.post(url, json=data_to_send)

response_json = response.json()
print("Ответ от сервера:")
print(json.dumps(response_json, indent=4))
