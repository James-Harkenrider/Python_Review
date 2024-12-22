import requests
from datetime import datetime

USERNAME = "harkej47"
TOKEN = ""
GRAPHID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

# graph_config = {
#     "id": "graph1",
#     "name": "Coding Graph",
#     "unit": "days",
#     "type": "int",
#     "color": "momiji"
# }
#
headers = {
    "X-USER-TOKEN": TOKEN
}
#
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)


today = datetime.now()
pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/{today.strftime("%Y%m%d")}"
pixel_config = {
    # "date": today.strftime("%Y%m%d"),
    "quantity": "3"
}

response = requests.put(url=pixel_endpoint, json=pixel_config, headers=headers)
print(response.text)
