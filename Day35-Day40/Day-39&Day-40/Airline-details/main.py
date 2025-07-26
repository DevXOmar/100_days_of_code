from notification_manager import NotificationManager

# Well each class is interlinked with the other class

#it starts with data_manager.py
## gets names of the target airlines from an online Excel sheet via Sheety

#then flight_data.py
##calls the aviationstack API and gets airline data. Also checks for data related to our Target Airlines

#next flight_search
##Organizes our acquired data into some useful info

#finally notification manager
##Our final content is sent to the client via mail

obj1 = NotificationManager()
obj1.details()
obj1.send_mail()