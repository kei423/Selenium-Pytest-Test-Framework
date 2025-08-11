import requests

url = "https://automationexercise.com/api/updateAccount"

# updating company to E
payload = {
    "name" : "a",
    "email" : "testemail425@gmail.com",
    "password" : "123",
    "title" : "Mr",
    "birth_date" : "01",
    "birth_month" : "01",
    "birth_year" : "2000",
    "firstname" : "a",
    "lastname" : "b",
    "company" : "E",
    "address1" : "423 1st St",
    "address2" : "Apt D",
    "country" : "United States",
    "zipcode" : "12345",
    "state" : "CA",
    "city" : "abc",
    "mobile_number" : "1234567890"
}
response = requests.put(url, data = payload)

try:
    update_user = response.json()
    print("Reponse code: " + str(update_user["responseCode"]))
    print(update_user["message"])
except:
    print("Invalid JSON in response")