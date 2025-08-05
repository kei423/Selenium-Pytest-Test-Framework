import requests
import json

url = "https://automationexercise.com/api/productsList"

response = requests.get(url)

assert response.status_code == 200, "Expected 200, but got" + response.status_code

try:
    products = response.json()
    print("Response Code: " + str(products["responseCode"]))
    for product in products["products"]:
        print(json.dumps(product["name"]))
except:
    print("Invalid JSON in response")