import requests
import json

url = "https://automationexercise.com/api/brandsList"

response = requests.get(url)

assert response.status_code == 200, "Expected 200 but got " + response.status_code

try:
    brands = response.json()
    print("Response Code: " + str(brands["responseCode"]))
    for brand in brands["brands"]:
        print(json.dumps(brand["brand"]))
except:
    print("Invalid JSON in response")