import requests

url = "https://automationexercise.com/api/productsList"

response = requests.get(url)

assert response.status_code == 200, "Expected 200, but got" + response.status_code

try:
    products = response.json()
    print(products)
except:
    print("Reponse was not valid JSON")