import requests
import datetime as dt
import random

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "apalat12"
TOKEN = "Wsdtf215fgtf56369gdlka"

user_param = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# response = requests.post(url=pixela_endpoint, json=user_param)
# print(response.text)
headers = {
    "X-USER-TOKEN": TOKEN
}

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": "dailyrun",
    "name": "Running Graph",
    "unit": "miles",
    "type": "float",
    "color": "shibafu"
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

today = dt.datetime.today()
today1 = dt.datetime.now().strftime("%Y%m%d")
print(today1)
# today_format = "".join(str(today).split(" ")[0].split("-"))

my_random_run = str(round(random.uniform(1.1,4.9),2))
print(my_random_run)

posting_graph = f"{graph_endpoint}/dailyrun"
post_config = {
    "date": today1,
    "quantity": my_random_run,
}

response = requests.post(url=posting_graph, json=post_config, headers=headers)
print(response.text)

# update_pixel = f"{pixela_endpoint}/{USERNAME}/graphs/dailyrun/{today1}"
# update_pixel_config = {
#     "quantity": '20'
# }
#
# response = requests.put(url=update_pixel, json=update_pixel_config, headers=headers)
# print(response.text)
#
# delete_pixel = f"{pixela_endpoint}/{USERNAME}/graphs/dailyrun/{today1}"
#
# response = requests.delete(url=delete_pixel,headers=headers)
# print(response.text)
