import requests
from twilio.rest import Client

with open("../../../weatherAPI_keys.txt", 'r') as key_file:
    key_data = key_file.readlines()

SID = key_data[0].split('=')[-1].strip()
AUTHTOKEN = key_data[1].split('=')[-1].strip()
APIKEY = key_data[2].split('=')[-1].strip()
LAT = "30.451468"
LON = "-91.187149"

arguments = {
    "lat": LAT,
    "lon": LON,
    "cnt": 4,
    "appid": APIKEY
}
api = f"https://api.openweathermap.org/data/2.5/forecast"

request = requests.get(api, arguments)
request.raise_for_status()
data = request.json()
weather_id = []
for forcast in data["list"]:
    forcast_3hr = forcast["dt_txt"]
    temp = int(forcast["main"]["temp"])
    temp_f = 9/5 * (temp - 273) + 32
    for weather in forcast["weather"]:
        if weather["id"] < 700:
            weather_id.append(weather["id"])
    print(f"Timestamp: {forcast_3hr}     Temperature: {temp_f}")

if len(weather_id) > 0:
    client = Client(SID, AUTHTOKEN)
    message = client.messages.create(
        body="Looks like rain today, best bring an umbrella!",
        from_="+18663526729",
        to="+16073779897"
    )
