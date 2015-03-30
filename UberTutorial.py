import requests
import settings

url = 'https://api.uber.com/v1/products'

parameters = {
    'server_token': settings.uber_token,
    'latitude': 37.775818,
    'longitude': -122.418028,
}

response = requests.get(url, params=parameters)

data = response.json()
print(data)