import requests, json

url = "https://api.sofascore.com/api/v1/unique-tournament/15006/events/last/0"

payload={}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
