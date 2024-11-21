import requests

url = 'http://localhost:9696/predict'

person_data = {
    "N_Days":1295,
    "Drug":'Placebo',
    "Age":45.0,
    "Sex":'F',
    "Ascites":'N',
    "Hepatomegaly":'N',
    "Spiders":'N',
    "Edema":'N',
    "Bilirubin":1.0,
    "Cholesterol":393.0,
    "Albumin":3.57,
    "Copper":50.0,
    "Alk_Phos":1307.0,
    "SGOT":74.0,
    "Tryglicerides" :103.0,
    "Platelets":295.0,
    "Prothrombin":10.5,
    "Stage":4.0
    }

response = requests.post(url, json=person_data).json()
print(response)

#this data should result 1 = C (censored)