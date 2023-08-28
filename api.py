import requests
import json

ip = input("Enter the IP >")

url = "https://api.greynoise.io/v3/community/{}".format(ip)

headers = {"accept": "application/json"}

def get(url, headers):
    response = requests.get(url, headers=headers)
    return response

def get_response_from_greynoise():
    response = get(url, headers)

    print(response.text)

    file = open("response.json", "w")
    try:
        file.write(json.dumps(response.text))
    finally:
        file.close()

get_response_from_greynoise()