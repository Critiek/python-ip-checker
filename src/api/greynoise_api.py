import requests
from os.path import exists

url = "https://api.greynoise.io/v3/community/"

def get(url, headers):
    response = requests.get(url, headers=headers)
    return response

def get_response_from_greynoise(ip):
    if exists('keys/greynoise_key.key'):
        with open('keys/greynoise_key.key', 'r') as file:
            key = file.read().strip()
        headers = {"key": key, "accept": "application/json"}

    response = get(url+ip, headers)

    print(response.text)

    with open("response.json", "w") as file:
        file.write(response.text)
