import requests

url = "https://automationexercise.com/api/verifyLogin"

payload = {"password" : "!23456A@"}
reponse = requests.post(url, payload)

try:
    verify_login = reponse.json()
    print("Response code: " + str(verify_login["responseCode"]))
    print(verify_login["message"])
except:
    print("Invalid JSON in response")