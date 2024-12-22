import requests

APP_ID = "76a9006c"
API_KEY = ""
ENDPOINT = "https://api.syndigo.com/v2/natural/exercise"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

parameters = {
    "query": "swam for 1 hour"
}

response = requests.post(url=ENDPOINT, headers=headers, json=parameters)
print(response.text)
