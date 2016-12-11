from bs4 import BeautifulSoup
import csv
import urllib
import csv, os

page = urllib.urlopen("http://gatherer.wizards.com/Pages/Search/Default.aspx?color=|[W]|[U]|[B]|[R]|[G]")
soup = BeautifulSoup(page)

cardtitle  = soup.find_all("span", {"class": "cardTitle"})
t = soup.find_all("span", {"class": "typeLine"})
m = soup.find_all("span", {"class": "convertedManaCost"})

f = csv.writer(open("mtg.csv", "w"))
f.writerow(["Name", "Type", "Mana"])



for span in cardtitle:
    links = span.findAll('a')
    for a in links:
        title = a.text.encode('UTF-8')
for span in t:
    type = span.text.encode('UTF-8')
for span in m:
    mana = span.text.encode('UTF-8')

for rows in data:
    f.writerow([title, type, mana])











