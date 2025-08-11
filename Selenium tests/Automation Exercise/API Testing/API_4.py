import requests

url = "https://automationexercise.com/api/brandsList"

response = requests.put(url)

try:
    brands = response.json()
    assert int(brands["responseCode"]) == 405, "Expected 405 but got " + str(brands["responseCode"])
    print("Response code: " + str(brands["responseCode"]))
    print(brands["message"])
except:
    print("Invalid JSON in response")