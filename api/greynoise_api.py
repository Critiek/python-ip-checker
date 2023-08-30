import requests
import json

with open('api/greynoise_key.txt', 'r') as file:
    key = file.read()

headers = {"key": key, "accept": "application/json"}

url = "https://api.greynoise.io/v3/community/"

def get(url, headers):
    response = requests.get(url, headers=headers)
    return response

def get_response_from_greynoise(ip):
    response = get(url+ip, headers)

    print(response.text)

    file = open("response.json", "w")
    try:
        file.write(response.text)
    finally:
        file.close()

