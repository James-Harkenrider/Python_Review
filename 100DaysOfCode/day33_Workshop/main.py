import requests
from datetime import datetime
import smtplib
import time


def send_email(subject, message):
    my_gmail = "blank@gmail.com"

    with open("../../../day32_gmail_app_pass.txt") as pass_file:
        password = pass_file.readline()

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_gmail, password=password)
        connection.sendmail(
            from_addr=my_gmail,
            to_addrs="blank@outlook.com",
            msg=f"Subject:{subject}\n\n "
                f"{message}"
        )


# MY_LAT = 37.338207  # Your latitude
# MY_LONG = -121.886330  # Your longitude
MY_LAT = 0  # Your latitude
MY_LONG = -8  # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "tzid": "America/Los_Angeles",
    "formatted": 0
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now().hour

iss_within_range = False
print(f"LAT: {iss_latitude}/ LONG: {iss_longitude}")
print(f"TIME NOW: {time_now}/ SUNRISE: {sunrise}")
if abs(MY_LAT - iss_latitude) <= 5 and abs(MY_LONG - iss_longitude) <= 5:
    if (time_now > sunset) and (time_now < sunrise):
        send_email("ISS Space Station Alert", "Look up now!")

time.sleep(60)
