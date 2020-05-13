import requests, pandas
from bs4 import BeautifulSoup

info = ""
basic_url = "https://www.wikipedia.org/"
req = requests.get(basic_url)
content = req.content
soup = BeautifulSoup(content, "html.parser")
search = soup.findAll("div", {"class":"search-container"})
print(search)