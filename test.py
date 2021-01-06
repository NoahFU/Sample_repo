import requests

url = "text"

response = requests.get("https://protari.abs.gov.au/v1/about")

print (response.json())