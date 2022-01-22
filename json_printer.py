import requests, json

url = "https://api.sofascore.com/api/v1/unique-tournament/15006/events/last/0"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
