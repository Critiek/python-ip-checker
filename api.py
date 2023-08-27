import requests
import json

ip = input("Enter the IP >")

url = "https://api.greynoise.io/v3/community/{}".format(ip)

headers = {"accept": "application/json"}

def get(url, headers):
    response = requests.get(url, headers=headers)
    return response

response = get(url, headers)

print(response.text)

response_json = json.dumps(response.text)

file = open("response.json", "w")
try:
    file.write(response_json)
finally:
    file.close()