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
### return 0 death

# person_data = {
#     "N_Days":1295,
#     "Drug":'Placebo',
#     "Age":45.0,
#     "Sex":'F',
#     "Ascites":'N',
#     "Hepatomegaly":'N',
#     "Spiders":'N',
#     "Edema":'N',
#     "Bilirubin":1.0,
#     "Cholesterol":393.0,
#     "Albumin":3.57,
#     "Copper":50.0,
#     "Alk_Phos":1307.0,
#     "SGOT":74.0,
#     "Tryglicerides" :103.0,
#     "Platelets":295.0,
#     "Prothrombin":10.5,
#     "Stage":4.0
#     }

### return 1

# person_data = {
#     "N_Days":1504,
#     "Drug":'Placebo',
#     "Age":38.0,
#     "Sex":'F',
#     "Ascites":'N',
#     "Hepatomegaly":'Y',
#     "Spiders":'Y',
#     "Edema":'N',
#     "Bilirubin":3.4,
#     "Cholesterol":279.0,
#     "Albumin":3.53,
#     "Copper":143.0,
#     "Alk_Phos":671.0,
#     "SGOT":113.15,
#     "Tryglicerides" :72.0,
#     "Platelets":136.0,
#     "Prothrombin":10.9,
#     "Stage":3.0
#     }

### return 2

response = requests.post(url, json=person_data).json()
print(response)
