import requests
import datetime as dt
import smtplib

MY_LAT = 17.425308
MY_LONG = 78.474135

my_email = ""
password = ""

response1 = requests.get(url="http://api.open-notify.org/iss-now.json")
response1.raise_for_status()
data1 = response1.json()

iss_latitude = float(data1["iss_position"]["latitude"])
iss_longitude = float(data1["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.
print(iss_latitude,iss_longitude)
def pos_check():
    if (MY_LAT - 5 <= iss_latitude <= MY_LAT + 5) and (MY_LONG - 5 <= iss_longitude <= MY_LONG + 5):
             return True
def is_night():
    now = dt.datetime.now()
    time_h = now.hour
    if time_h>sunset or time_h<sunrise:
        return True
parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}
response2 = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response2.raise_for_status()
data2 = response2.json()
sunrise = int(data2["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data2["results"]["sunset"].split("T")[1].split(":")[0])

# If iss is overhead and its nighttime
if pos_check() and is_night():
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="god.s.m.o.97@gmail.com",
                            msg="subject: The ISS notifier\n\n Look up the ISS is nearby!")


