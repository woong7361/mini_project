import datetime as dt
from weather import getWeather, getAirCondition
import pandas as pd

d1 = getWeather("강남구")
print(d1)

d2 = getAirCondition("강남구")
print(d2)

d3 = dict(d1, **d2)

print(d3)
# print(response)
# print(response.url)
# print(response.content)




