import requests
from bs4 import BeautifulSoup

response = requests.get(url = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
website_html = response.text

soup = BeautifulSoup(website_html,"html.parser")

# year = soup.select("p strong")
# print(year)

title = soup.find_all(name = "h3",class_ = "title")

#All the titles on the webpage.
list1 = []
for x in title:
    rank = x.getText()
    list1.append(rank)

# Reversing the list.
list2 = []
for x in range(len(list1)-1,-1,-1): # the right limit is exclusive
    list2.append(list1[x])
# print(list2)

with open("Best Movies.txt", mode = "w") as file:
    for line in list2:
        file.write(f"{line}\n")
