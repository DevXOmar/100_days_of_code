import requests
from twilio.rest import Client
import os

account_sid = ""
# auth_token = ""
auth_token = os.environ.get("AUTH_TOKEN")
# print(auth_token)

LAT = 17.421377
LON = 78.472799

# api_key = ""
api_key = os.environ.get("OWM_API_KEY")
# print(api_key)

call = requests.get(url = f"https://api.openweathermap.org/data/2.5/forecast?lat={LAT}&lon={LON}&cnt=4&appid={api_key}")
data = call.json()


weather_daily = data["list"]
# print(weather_daily)
flag = 0

for x in weather_daily:
    print(x["weather"][0]["id"],":",x["weather"][0]["description"])
    print(x["main"]["humidity"])
    if x["main"]["humidity"] > 60 and x["weather"][0]["id"]<700 :
        flag = 1
    elif x["weather"][0]["id"]<700:
        flag = 2
    # Weather code < 700:: Rainy Atmosphere.
if flag == 1:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="\nIt might rain today."
             "\nPlease carry an umbrella☂️.",
        from_="+17697598403",
        to="+919391141054",
    )
elif flag == 2:
    client = Client(account_sid,auth_token)
    message = client.messages.create(
        body = "\nIt might rain today and the humidity is high.\n"
               "Please carry an umbrella☂️.",
        from_ = "+17697598403",
        to = "+919391141054",
    )
    print(message.sid)