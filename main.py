import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import random
from random import choice
import asyncio
import wikipedia
from config import *
import pyjokes
import requests
import time
import json
import sys
import webbrowser
import os

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
vvccee = f'voices[{voiceee}].id'
engine.setProperty('voice', vvccee)
now = datetime.datetime.now()
clear = lambda: os.system('cls')
rate = engine.getProperty('rate')
engine.setProperty('rate', 180)  

## Weather
URL = 'http://api.openweathermap.org/data/2.5/weather?q=Newmarket&appid=0c42f7f6b53b244c78a418f4f181282a&units=metric'
response = requests.get(URL)
data = response.json()
main = data['main']
tem = main['temp']
temp_feel_like = main['feels_like']
humidity = main['humidity']
pressure = main['pressure']
weather_report = data['weather']
wind_report = data['wind']
## Weather

## COVID-19
url = f"https://coronavirus-19-api.herokuapp.com/countries/{countryName}"
stats = requests.get(url)
json_stats = stats.json()
country = json_stats["country"]
totalCases = json_stats["cases"]
todayCases = json_stats["todayCases"]
totalDeaths = json_stats["deaths"]
todayDeaths = json_stats["todayDeaths"]
recovered = json_stats["recovered"]
active = json_stats["active"]
critical = json_stats["critical"]
casesPerOneMillion = json_stats["casesPerOneMillion"]
deathsPerOneMillion = json_stats["deathsPerOneMillion"]
totalTests = json_stats["totalTests"]
testsPerOneMillion = json_stats["testsPerOneMillion"]
## COVID-19

def talk(text):
    engine.say(text)
    engine.runAndWait()


r = sr.Recognizer() 
def record_audio(ask=False):
    with sr.Microphone() as source: 
        if ask:
            talk(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio) 
        except sr.UnknownValueError:
            clear()
        except sr.RequestError:
            clear()
        return voice_data.lower()

while True:
    commands = record_audio()
    if 'song' in commands:
        song = commands.replace('play', '')
        talk('playing the requested song')
        pywhatkit.playonyt(song)
    elif 'time' in commands:
        time = datetime.datetime.now().strftime('%H:%M ')
        timee = datetime.datetime.now().strftime('%H:%M %p')
        if hour12 == 'false':
            talk('The current time is ' + time)
        elif hour12 == 'true':
            talk('The current time is ' + timee)
    elif 'exit' in commands:
        talk('Exiting Tay AI')
        clear()
        sys.exit()
    elif 'weather' in commands:
        talk(f'The Temperature In {location} is {tem}, and the feel like is {temp_feel_like}')
    elif 'temperature' in commands:
        talk(f'The Temperature In {location} is {tem}, and the feel like is {temp_feel_like}')
    elif 'case' in commands:
        talk(f"Today There were {todayCases} new cases here in {countryName}, and {todayDeaths} deaths today here in {countryName}, the total cases of {countryName} are {totalCases}, and a total deaths of {totalDeaths}")
    elif 'date' in commands:
        talk(f'Today is ' + now.strftime("%Y-%m-%d"))
    else:
        clear()