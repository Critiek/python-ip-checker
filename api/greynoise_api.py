import requests
import json

with open('api/greynoise_key.txt', 'r') as file:
    key = file.read()

ip = input("Enter the IP \n> ")

url = "https://api.greynoise.io/v3/community/{}".format(ip)

headers = {"key": key, "accept": "application/json"}

def get(url, headers):
    response = requests.get(url, headers=headers)
    return response

def get_response_from_greynoise():
    response = get(url, headers)

    print(response.text)

    file = open("response.json", "w")
    try:
        file.write(response.text)
    finally:
        file.close()
