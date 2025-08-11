import requests

url = "https://automationexercise.com/api/deleteAccount"

payload = {"email" : "testemail425@gmail.com", "password" : "123"}
response = requests.delete(url, data = payload)

try:
    delete_user = response.json()
    print("Reponse code: " + str(delete_user["responseCode"]))
    print(delete_user["message"])
except:
    print("Invalid JSON in response")