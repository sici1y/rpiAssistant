# IMPORTS
import requests
from gtts import gTTS
import os

# CITY
city = "Siloam Springs"

# API
url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=d0021f6e2458575c6ca6f4949a1b6e5c&units=imperial'.format(city)

# REQUEST
res = requests.get(url)
data = res.json()

# WEATHER DATA
humidity = data['main']['humidity']
pressure = data['main']['pressure']
wind = data['wind']['speed']
description = data['weather'][0]['description']
temp = data['main']['temp']

# gTTS DATA
language = 'en'
weatherTTS = 'This is a test'

# PRINT DATA AND TTS
print('Temperature:',temp,'°F')
print('Wind:',wind, 'mph')
print('Pressure: ',pressure)
print('Humidity: ',humidity, '%')
print('Description:',description)

myobj = gTTS(text=weatherTTS, lang=language, slow=False)
# SAVE MP3
myobj.save("weather.mp3")
# PLAY MP3
os.system("mpg321 weather.mp3")