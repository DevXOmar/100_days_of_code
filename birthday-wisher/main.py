import random
import smtplib
import datetime as dt
import csv

now = dt.datetime.now()
day_of_month = now.day
month_of_year = now.month
# print(day_of_month)

my_email = ""
password = ""

birth_data = []

with open("birthdays.csv", mode = "r") as file:
    data1 = csv.reader(file)
    next(data1)

    for x in data1:
     if len(x)==5: ## index out of bound error fix.
        birth_data1 =  {"Name":x[0],"Email":x[1],"Year":x[2],"Month":x[3],"Day":x[4]}
        birth_data.append(birth_data1)


choice = random.randint(1, 3)
letter_head = f"letter_templates/letter_{choice}.txt"


# Mechanism.

for x in birth_data:
    if day_of_month == int(x["Day"]) and month_of_year == int(x["Month"]):
        with open(letter_head, mode="r") as file:
            env = file.read()
            env = env.replace("[NAME]",x["Name"]) ##.

        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs="god.s.m.o.97@gmail.com",
                                msg=f"subject: Happy Birthday!\n\n "
                                    f"{env}")
            connection.close()







