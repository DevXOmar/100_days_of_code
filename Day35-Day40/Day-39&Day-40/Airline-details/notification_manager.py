from flight_search import FlightSearch
import smtplib
class NotificationManager:
    def details(self):
        obj = FlightSearch()
        obj.get_data()
        obj.clean()
        self.message = obj.messaging()

    def send_mail(self):
        my_email = "aren91173@gmail.com"
        my_password = ""

        with smtplib.SMTP("smtp.gmail.com",587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email, to_addrs="god.s.m.o.97@gmail.com",
                                msg=f"subject: Your requested Airline Survey is here.\n\n{self.message}")
