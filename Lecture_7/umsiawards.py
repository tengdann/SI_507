from bs4 import BeautifulSoup
import requests

baseurl = 'https://www.si.umich.edu'
catalog_url = baseurl + '/news-events/awards-and-honors'
header = {'User-Agent': 'SI_CLASS'}
page_text = requests.get(catalog_url, headers = header).text
page_soup = BeautifulSoup(page_text, 'html.parser')

field_items = page_soup.find(class_ = 'field-item even', property = 'content:encoded')
awards = field_items.find_all('h3')[:4]

# Right now, list of links to awards
# Need to extract list of winners from 2018, 2017, 2016, and 2015

class Award:
    def __init__(self, url, name):
        self.winners = {}
        self.name = name
        
        award_soup = BeautifulSoup(requests.get(url, headers = header).text, 'html.parser')
        award_items = award_soup.find(class_ = 'field-item even', property = 'content:encoded')
        list_winners = award_items.find_all('p')[-7:-4]
        for winner in list_winners:
            self.winners[winner.text[:4]] = winner.get_text(strip = True, separator = " ")[5:]
            
    def __call__(self, year):
        return self.winners[str(year)]
        
# award_list = []
# year_list = [2017, 2016, 2015]
# for award in awards:
    # award_list.append(Award(baseurl + award.find('a')['href'], award.find('a').text))
    
# for award in award_list:
    # print(award.winners)
    
# for year in year_list:
    # print(year)
    # for award in award_list:
        # print('\t' + award.name + ': ' + award(year))
    # print()
    