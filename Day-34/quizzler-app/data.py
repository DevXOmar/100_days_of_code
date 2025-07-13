import requests
parameters = {
    "amount": 10,
    "type": "boolean"
}
data = requests.get("https://opentdb.com/api.php",params = parameters)
data1 = data.json()

question_data = data1["results"]
# print(data1["results"])