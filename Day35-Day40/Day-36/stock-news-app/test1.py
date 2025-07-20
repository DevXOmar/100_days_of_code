import datetime as dt

now = dt.datetime.now().date()
str1 = str(now)
print(type(str1))

day = now.day
print(day)

now = dt.datetime.now()
date_today = now.date()
print(date_today)

now = dt.datetime.now()
day = now.day
month = now.month
print(day)