import requests
import json

# URL сервера, куда отправляем запрос
url = 'http://127.0.0.1:5000/edit_house'

# JSON данные для отправки
# data_to_send = {'name': 'test52', 'is_coop': 1, 'is_pir': 1,
# 'is_smr_gvd_gnd': 0, 'is_smr_vdgo': 0, 'is_to_gvd_gnd': 0,
# 'from_1c': 0, 'to_rg': 0, 'to_ggs': 0, 'to_gss': 0, 'to_ggsi': 0,
# 'to_ggss': 0, 'to_rgs': 0, }

# data_to_send = {'town': 'Новосибирск', 'district': 'Заельцовский', 'street': 'Широкая',
#                 'house_number': '15b', 'corpus_number': 'k1', 'flat_number': '12',
#                 'cadastr_number': '123123123', 'is_actual': 1,
#                 'id_house': 104633}

data_to_send = {'id_house': 104633, 'is_actual': 1}

# Отправляем POST запрос с JSON данными
response = requests.post(url, json=data_to_send)

response_json = response.json()
print("Ответ от сервера:")
print(json.dumps(response_json, indent=4))
