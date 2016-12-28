from bs4 import BeautifulSoup
import urllib
import csv, os
import re


class Gathering():

    def __init__(self):
        self.decklist = [["Name", "Type", "Mana", "Deck"]]

    def mainmethod(self):
        for x in xrange(0, 142):
            self.page = urllib.urlopen("http://gatherer.wizards.com/Pages/Search/Default.aspx?page={0}&color=|[W]|[U]|[B]|[R]|[G]".format(x))
            self.soup = BeautifulSoup(self.page)
            self.card_info()
            print("Completed page: {0}".format(x))
        self.csv_writer()

    def card_info(self):
        self.cardinfo = self.soup.find_all("div", attrs={"class": "cardInfo"})
        for card in self.cardinfo:
            self.card = card
            self.title_parse()
            self.type_parse()
            self.converted_mana_parse()
            self.mana_cost_parse()
            self.decklist.append([self.cardtitle, self.type, self.mana])

    def title_parse(self):
        self.cardtitle = self.card.findNext("span", {"class": "cardTitle"}).text.strip().encode('utf-8')

    def type_parse(self):
        self.type = self.card.findNext("span", {"class": "typeLine"}).text.strip().encode('utf-8')

    def converted_mana_parse(self):
        self.conv_mana = self.card.findNext("span", {"class": "convertedManaCost"}).text.strip().encode('utf-8')

    def mana_cost_parse(self):
        self.mana_cost = self.card.findNext("span", {"class": "manaCost"})
        for img in self.mana_cost.find_all("img"):
            try:
        self.mana = re.search(r'(\d)', re.search(r'alt="(\d)"', str(img)).group()).group().encode('utf-8')
            except:
                pass

    def csv_writer(self):
        with open("mtg.csv", "wb") as mtglist:
            mtglist = csv.writer(mtglist)
            for card in self.decklist:
                mtglist.writerow(card)

if __name__ == '__main__':
    Gathering().mainmethod()
~                                                                               
                              
