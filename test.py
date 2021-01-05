import requests

#url = input("your url = ")

response = requests.get("https://protari.abs.gov.au/v1/about")

print (response.json())