import requests


url = "https://api.openweathermap.org/data/2.5/weather"

params ={"q": "Seoul", "appid": "102364761d47591fac837b027b548d4f", "lang": "kr"}
json = requests.get(url, params)

# print(json.json())
# print(json.json())
for j in json.json():
    print(str(j) + " : " + str(json.json()[j]))
