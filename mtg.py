from bs4 import BeautifulSoup
import csv
import urllib


page = urllib.urlopen("http://gatherer.wizards.com/Pages/Search/Default.aspx?color=|[W]|[U]|[B]|[R]|[G]")
soup = BeautifulSoup(page)

spans  = soup.find_all("span", {"class": "cardTitle"})

for span in spans:
    links = span.findAll('a')
    for a in links:
        print a.text

