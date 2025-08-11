import requests

url = "https://automationexercise.com/api/getUserDetailByEmail"

email = {"email" : "testemail425@gmail.com"}
response = requests.get(url, params = email)

try:
    user_info = response.json()
    print("Reponse code: " + str(user_info["responseCode"]))
    print(user_info["user"])
except:
    print("Invalid JSON in response")