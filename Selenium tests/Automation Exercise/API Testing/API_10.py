import requests

url = "https://automationexercise.com/api/verifyLogin"

# incorrect password
payload = {"email": "testemail423@gmail.com", "password": "!23456A"}
response = requests.post(url, data = payload)

try:
    verify_login = response.json()
    print("Reponse code: " + str(verify_login["responseCode"]))
    print(verify_login["message"])
except:
    print("Invalid JSON in response")