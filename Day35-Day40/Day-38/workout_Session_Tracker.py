import requests
import datetime as dt

# Nutritionix API
API_ID = ""
API_KEY = ""

header = {
    'Content-Type': 'application/json',
    'x-app-id':API_ID,
    'x-app-key':API_KEY
}
json1 = {
  "query": input("Enter exercise session: ")
}
call_nutritionix_api = requests.post(url = "https://trackapi.nutritionix.com/v2/natural/exercise",headers=header,json=json1)

data = call_nutritionix_api.json()
EXERCISE = data["exercises"][0]["name"]
DURATION = data["exercises"][0]["duration_min"]
CALORIES = data["exercises"][0]["nf_calories"]


#Obtaining Date and Time
now = dt.datetime.now()
DATE = now.strftime("%d/%m/%Y")
TIME = now.strftime("%H:%M:%S")
# print(DATE)


# Sheety Api
header2 = {
     "Authorization": ""
}
json2 = {
    "workout":{
     "date":DATE, # there;s a catch all these headings (date etc...) must be in lower case only.
        "time":TIME,
        "exercise":EXERCISE,
        "duration":DURATION,
        "calories":CALORIES
}}
# Writing data to an excel sheet online.
call_sheety_api = requests.post(url = "https://api.sheety.co/9dec29ddd2b7cd02d9d6da11d7f0a1ca/myWorkoutsSessions/workouts",json = json2,headers=header2)
# print(call_sheety_api.text)