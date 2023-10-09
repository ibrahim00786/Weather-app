import win32com.client as wincom
import requests
import json


city = input("Enter the name of the city\n")

url = f"https://api.weatherapi.com/v1/current.json?key=f4defccec1b8410c8f3145052231705&q={city}"
r = requests.get(url)

# print(r.text)

# By this json method we can convert this string into dictionary

weather = json.loads(r.text)

# print(type(weather))

# Here we are using dictionaries key value pair to get our work done

w = weather["current"]["temp_c"]
#
speak = wincom.Dispatch("SAPI.SpVoice")
text = f"The Current Weather in {city} is {w} Degrees"
speak.Speak(text)