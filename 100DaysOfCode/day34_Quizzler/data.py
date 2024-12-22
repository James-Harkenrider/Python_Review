import requests

params = {
    "amount": 10,
    "type": "boolean"
}

request = requests.get("https://opentdb.com/api.php", params)
request.raise_for_status()
data = request.json()
question_data = data["results"]

