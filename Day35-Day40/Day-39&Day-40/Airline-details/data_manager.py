import requests
class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.header1 = {
            "Authorization": ""
        }
        self.target = requests.get(url = "https://api.sheety.co/9dec29ddd2b7cd02d9d6da11d7f0a1ca/flightDeals/prices",headers=self.header1)
        self.data = self.target.json()
        self.data1 = self.data["prices"]
        self.airlines = []
    def getting_data(self):
        for x in self.data1:
            self.airlines.append(x["airlines"])
            #  print(x)
        return self.airlines
# obj = DataManager()
# obj.getting_data()