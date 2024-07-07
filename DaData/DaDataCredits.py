import json

with open('DaData/DaData.json') as f:
    d = json.load(f)
    DADATA_TOKEN = d["DADATA_TOKEN"]
    DADATA_SECRET = d["DADATA_SECRET"]
