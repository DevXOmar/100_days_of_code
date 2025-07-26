from data_manager import DataManager
import requests
class FlightData:
    def __init__(self):
        self.params = {
            "access_key": ""
        }
        self.call = requests.get(url = "https://api.aviationstack.com/v1/airlines",params=self.params)
        self.data = self.call.json()
        self.data1 = self.data["data"]
        self.details = []

    def target_airlines(self):
        obj1 = DataManager()
        self.target = obj1.getting_data() ## Has all the Target Airlines.
        ## Self.target is initialized and loaded now.

    def data_find(self):
        for item in self.target:
            for x in self.data1:
                # print(x)
                if item == x["airline_name"]:
                    self.details.append(x)
        # print(self.details)
        ##Self.details is loaded now.
        return self.details


# obj = FlightData()
# obj.target_airlines()
# obj.data_find()

