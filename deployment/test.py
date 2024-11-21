import requests

url = 'http://localhost:9696/predict'

person_data = {
    "N_Days":1504,
    "Drug":'Placebo',
    "Age":38.0,
    "Sex":'F',
    "Ascites":'N',
    "Hepatomegaly":'Y',
    "Spiders":'Y',
    "Edema":'N',
    "Bilirubin":3.4,
    "Cholesterol":279.0,
    "Albumin":3.53,
    "Copper":143.0,
    "Alk_Phos":671.0,
    "SGOT":113.15,
    "Tryglicerides" :72.0,
    "Platelets":136.0,
    "Prothrombin":10.9,
    "Stage":3.0
    }

response = requests.post(url, json=person_data).json()
print(response)
#this return 2=CL (censored due to liver transplantation)

