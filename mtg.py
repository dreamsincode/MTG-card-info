from bs4 import BeautifulSoup
import csv
import urllib


page = urllib.urlopen("http://gatherer.wizards.com/Pages/Search/Default.aspx?color=|[W]|[U]|[B]|[R]|[G]")
soup = BeautifulSoup(page)

cardtitle  = soup.find_all("span", {"class": "cardTitle"})
type = soup.find_all("span", {"class": "typeLine"})
mana = soup.find_all("span", {"class": "convertedManaCost"})
deck = soup.find_all("img")
extra = soup.find_all("div", {"class": "rightCol" } )
soup.decompose(extra)

for span in cardtitle:
    links = span.findAll('a')
    for a in links:
        print a.text
    for span in type:
        print span.text
    for span in mana:
        print span.text
    for img in deck:
        color = img.get('alt', '')
        print color


