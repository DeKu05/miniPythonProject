import requests
import json
import os

city = input("Enter the name of the city\n")
url = f"https://api.weatherapi.com/v1/current.json?key=6440485e05ba43b2a8275622231308&q={city}"
r = requests.get(url)
#print(r.text)
weatherDict = json.loads(r.text)
w = weatherDict["current"]["temp_c"]
os.system(f'''PowerShell -Command "Add-Type -AssemblyName System.speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).speak('Weatehr in {city} is {w} degrees ');"''')
f = weatherDict["current"]["feelslike_c"]
os.system(f'''PowerShell -Command "Add-Type -AssemblyName System.speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).speak('Weatehr in {city} feels like {f} degrees ');"''')