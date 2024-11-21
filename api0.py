import requests

url = 'http://localhost:9696/predict'

person_data = {
    "N_Days":1012,
    "Drug":'D-penicillamine',
    "Age":70.0,
    "Sex":'M',
    "Ascites":'N',
    "Hepatomegaly":'N',
    "Spiders":'N',
    "Edema":'S',
    "Bilirubin":1.4,
    "Cholesterol":176.0,
    "Albumin":3.48,
    "Copper":210.0,
    "Alk_Phos":516.0,
    "SGOT":96.10,
    "Tryglicerides" :55.0,
    "Platelets":151.0,
    "Prothrombin":12.0,
    "Stage":4.0
    }

response = requests.post(url, json=person_data).json()
print(response)

#this data should result 0 = D (Death)
