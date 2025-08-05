import requests
import json

url = "https://automationexercise.com/api/searchProduct"

payload = {"search_product": "jean"}
response = requests.post(url, data = payload)

assert response.status_code == 200, "Expected 200, but got " + response.status_code

try:
    search_product = response.json()
    for product in search_product["products"]:
        print(product)
except:
    print("Invalid JSON in response")