import datetime as dt

import requests

USERNAME = ""
TOKEN = ""

##creating our account and username on pixela
json1 = {
    "token" : TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}
response = requests.post(url = "https://pixe.la/v1/users",json = json1)
print(response.text)

#Creating a graph
json2 = {
    "id": "graph1",
    "name":"sport name",
    "unit":"Ar",
    "type":"float",
    "color":"shibafu"

}
header = {
"X-USER-TOKEN":"ABC123efgh97"
}
response = requests.post(url = "https://pixe.la/v1/users/omar97/graphs",json = json2,headers=header)
print(response.text)


# now = dt.datetime.now()
now = dt.datetime(year = 2025,month = 7 , day = 9)
DATE = now.strftime("%Y%m%d") ## Formatting date

#Posting a pixel.
json3 = {
    "date":DATE,
    "quantity": "10",
}
response = requests.post(url = "https://pixe.la/v1/users/omar97/graphs/graph1",headers=header,json = json3)
print(response.text)


#updating a pixel
json4 = {
    "quantity":"50"
}
response = requests.put(url = f"https://pixe.la/v1/users/omar97/graphs/graph1/{DATE}",headers=header,json = json4)
print(response.text)

#deleting a pixel
response = requests.delete(url = f"https://pixe.la/v1/users/omar97/graphs/graph1/{DATE}",headers=header)
print(response.text)