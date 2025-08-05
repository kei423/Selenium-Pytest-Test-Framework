import requests

url = "https://automationexercise.com/api/verifyLogin"

response = requests.delete(url)

try:
    verify_login = response.json()
    print("Response code: " + str(verify_login["responseCode"]))
    print(verify_login["message"])
except:
    print("Invalid JSON in response")