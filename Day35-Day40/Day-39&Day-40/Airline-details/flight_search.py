from flight_data import FlightData
class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.cleaned_data = []
    def get_data(self):
        obj = FlightData()
        obj.target_airlines()
        self.target_details = obj.data_find()

    def clean(self):
        for x in self.target_details:
            dict1 = {
                "airline_name" : x["airline_name"],
                "callsign" : x["callsign"],
                "date_founded" : x["date_founded"],
                "fleet_size" : x["fleet_size"],
                "status": x["status"]
            }
            self.cleaned_data.append(dict1)

    def messaging(self):
        # print(self.cleaned_data)
        Heading = "Details on your favourite Airlines:"
        txt = [(f"Airline Name : {x["airline_name"]}\nCall Sign : {x["callsign"]}\nDate-Founded : {x["date_founded"]}\n"
                f"Fleet-size : {x["fleet_size"]}\nStatus : {x["status"]} ")for x in self.cleaned_data]
        #txt is a List of strings
        body = "\n\n".join(txt)
        self.message = f"{Heading}\n\n\n{body}"
        return self.message


obj = FlightSearch()
obj.get_data()
obj.clean()
obj.messaging()