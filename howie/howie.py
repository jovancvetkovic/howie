# import libraries
import urllib.request
from bs4 import BeautifulSoup

quote_page = 'https://www.catsa-acsta.gc.ca/en/airport/toronto-pearson-international-airport'

page = urllib.request.urlopen(quote_page)

soup = BeautifulSoup(page, "html.parser")

print(soup.find("table", attrs={"class": "views-table"}).find("th").text)

