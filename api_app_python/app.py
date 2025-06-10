import requests
import json

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
response = requests.get(url)
print(response)

if response.status_code == 200:
    data_json = response.json()
    print(data_json)
    data_restaurant = {}
    for item in data_json:
        name_restaurant = item['Company']
        if name_restaurant not in data_restaurant:
            data_restaurant[name_restaurant] = []
        data_restaurant[name_restaurant].append({
            "item": item['Item'],
            "price": item['price'],
            "description": item['description']
        })
else:
    print(f'The error is {response.status_code}')

for name_restaurant, data in data_restaurant.items():
    archive_name = f'{name_restaurant}.json'
    with open(archive_name, 'w') as archive_restaurant:
        json.dump(data,archive_restaurant,indent=4)