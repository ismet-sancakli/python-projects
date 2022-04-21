import requests
from datetime import datetime

USERNAME = "ismet5"
TOKEN = "asdfertgbcxzxxklypg"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

pixela_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=pixela_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Cycling graph",
    "unit": "Km",
    "type": "float",
    "color": "shibafu"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

# today = datetime(year=2022, month=4, day=20) # This type can use for the specific days or past days.

today = datetime.now()
# print(today.strftime("%Y%m%d"))

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many kilometers did you run today? "),

}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)

update_data_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

updated_pixel_data = {
    "quantity": "12.21"
}

# response = requests.put(url=update_data_endpoint, json=updated_pixel_data, headers=headers)
# print(response.text)

delete_data_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

# response = requests.delete(url=delete_data_endpoint, headers=headers)
# print(response.text)

