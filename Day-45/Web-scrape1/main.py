from bs4 import BeautifulSoup
import requests

response = requests.get(url = "https://news.ycombinator.com/news")
website_html = response.text
# print(website_html)

soup = BeautifulSoup(website_html,"html.parser")

# Getting titles and links from the page
titles1 = soup.find_all(name = "span",class_ = "titleline")
just_titles = []
just_links = []
for tag in titles1:
    title = tag.find("a").text
    links = tag.find("a").get("href")
    just_titles.append(title)
    just_links.append(links)
print(just_titles)
print(just_links)

# Getting points data
just_points = []
scores1 = soup.find_all(name = "span", class_ = "score")
# print(scores1)
for tag in scores1:
    points = int(tag.text.split()[0]) # Getting it into integer terms
    just_points.append(points)
print(just_points)

# Zipping all the three details together. (Title, Links, Points)
all_tuples = []
max_points = 0
for x,y,z in zip(just_titles,just_links,just_points):
    tuple1 = (x,y,z)
    if max_points<z:
        max_points = z
    all_tuples.append(tuple1)
print(all_tuples)

# The Highest points data
for item in all_tuples:
    if max_points == item[2]:
        print(item)



# title = soup.find(name = "span",class_ = "titleline").find("a")
# print(title.text)