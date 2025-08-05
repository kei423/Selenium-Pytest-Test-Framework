import requests

url = "https://automationexercise.com/api/verifyLogin"

payload = {"email": "testemail423@gmail.com", "password": "!23456A@"}
response = requests.post(url, data = payload)

try:
    verify_login = response.json()
    print(verify_login["responseCode"])
    print(verify_login["message"])
except:
    print("Invalid JSON in response")