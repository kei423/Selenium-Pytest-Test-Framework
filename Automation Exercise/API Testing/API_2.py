import requests

url = "https://automationexercise.com/api/productsList"

response = requests.post(url)

try:
    products = response.json()
    assert int(products["responseCode"]) == 405, "Expected 405, but got" + str(products["responseCode"])
    print("Response code: " + str(products["responseCode"]))
    print(str(products["message"]))
except:
    print("Invalid JSON in response")