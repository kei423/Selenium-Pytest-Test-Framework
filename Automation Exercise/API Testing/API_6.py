import requests

url = "https://automationexercise.com/api/searchProduct"

payload = {}
response = requests.post(url)

try:
    search_product = response.json()
    print("Response code: " + str(search_product["responseCode"]))
    print(search_product["message"])
except:
    print("Invalid JSON in response")