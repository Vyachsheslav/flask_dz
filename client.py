import requests

data = requests.post('http://localhost:5000/ads', json = {
    "title": "Продается дом",
    "description": "Красивый дом с садом и бассейном",    
    "owner": "Сидоров Сидор"
},)
print(data.status_code)
print(data.json())




# data = requests.get('http://localhost:5000/ads/1')
# print(data.status_code)
# print(data.json())


# data = requests.delete('http://127.0.0.1:5000/ads/1')
# print(data.status_code)
# print(data.json())
