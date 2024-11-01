import requests

response = requests.get(url = "http://api.open-notify.org/iss-now.json")
# if response.status_code == 200:
#     raise Exception("The resource does not exist")
# elif response.status_code == 401:
#     raise Exception("You are not authorised to access this data.")
response.raise_for_status()

data = response.json()

longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

#Creating a tuple
iss_position = (longitude, latitude)
print(iss_position)