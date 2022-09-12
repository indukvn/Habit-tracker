import requests
from datetime import datetime

USERNAME = "your name"
TOKEN = "any random token say it is like a password "
GRAPHID = "graph123"

pixela_end_pt = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# to create user
# response = requests.post(url=pixela_end_pt, json=user_params)
# print(response.text)

graph_end_pt = f"{pixela_end_pt}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPHID,
    "name": "Cycling Graph",
    "unit": "Calories",
    "type": "float",
    "color": "momiji"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# to create graph
# response = requests.post(url=graph_end_pt, json=graph_config, headers=headers)
# print(response.text)

record_end_pt = f"{graph_end_pt}/{GRAPHID}"

today = datetime.now()

record_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many Calories did you burn today? ")
}

# to record the response of user
response = requests.post(url=record_end_pt, json=record_config, headers=headers)
print(response.text)

update_record_end_pt = f"{record_end_pt}/20220910"

update_config = {
    "quantity": "83.3"
}
# for update operation
# response = requests.put(url=update_record_end_pt, json=update_config, headers=headers)
# print(response.text)

# for delete operation
# response = requests.delete(url=update_record_end_pt, headers=headers)
# print(response.text)
