import requests
from bs4 import BeautifulSoup

rURL = requests.get("https://en.wikipedia.org/wiki/Deccan_Plateau")
bs4Soup = BeautifulSoup(rURL.content, "html.parser")
sTitle = bs4Soup.find(class_="firstHeading").text

print(sTitle)