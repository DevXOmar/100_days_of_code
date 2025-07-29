from bs4 import BeautifulSoup

with open ("website.html", mode = "r") as file:
    content = file.read()
    # print(content)

soup = BeautifulSoup(content,"html.parser")
tag1 = soup.find_all(name = "a")
print(tag1)