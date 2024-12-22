import requests
from datetime import datetime

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
#
# data = response.json()
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
#
# iss_position = (longitude, latitude)
# print(iss_position)

parameters = {
    "lat": 37.338207,
    "lng": -121.886330,
    "tzid": "America/Los_Angeles",
    "formatted": 0
}

response = requests.get("https://api.sunrise-sunset.org/json", parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[-1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[-1].split(":")[0]

time_now = datetime.now()
print(sunrise)

