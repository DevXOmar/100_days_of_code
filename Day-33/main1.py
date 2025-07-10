import requests
import datetime as dt

parameters = {
    "lat":17.385044,
    "lng":78.486671,
    "formatted":0
}

response = requests.get(url = "https://api.sunrise-sunset.org/json",params=parameters)
data = response.json()
print(data)
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

sunrise_hour = sunrise.split("T")[1].split(":")[0]
sunset_hour = sunset.split("T")[1].split(":")[0]
print(sunrise_hour)
print(sunset_hour)


now = dt.datetime.now() ##
current_time = now.time()
print(current_time)