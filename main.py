from datetime import datetime

import requests

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "samuel2010"
TOKEN = ""

user_params = {
    "token": "",
    "username": "samuel2010",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Coding Graph",
    "unit": "min",
    "type": "float",
    "color": "shibafu",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

graph_id = "graph1"

today = datetime.now().strftime("%Y%m%d")

pix_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_id}/{today}"

pix_config = {
    "quantity": "120"
}

response = requests.put(url=pix_endpoint, json=pix_config, headers=headers)
print(response.text)
