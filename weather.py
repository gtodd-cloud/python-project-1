import requests

url = 'http://api.weatherapi.com/v1/current.json?key=df199811fb54490e9cd190347232911&q=California&aqi=no'
response = requests.get(url)
weather_json = response.json()

temp = weather_json.get('current').get('temp_f')
description = weather_json.get('current').get('condition').get('text')

print("Today's weather in California is", description, 'and', temp, 'degrees')