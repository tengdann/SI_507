import requests
import requests_cache
import json
import time
import csv
from bs4 import BeautifulSoup

startTime = time.time()

baseurl = 'https://www.freep.com'
news_url = baseurl + '/news/'
requests_cache.install_cache('freep_cache')

with requests_cache.disabled():
    freep_text = requests.get(news_url).text

freep_soup = BeautifulSoup(freep_text, 'html.parser')

headlines_links = []

raw_links = freep_soup.find_all('a', itemprop = 'url', limit = 10)
for raw_link in raw_links:
    headlines_links.append(baseurl + raw_link['href'])

information = {}
    
for i in headlines_links:
    headline_text = requests.get(i).text
    headline_soup = BeautifulSoup(headline_text, 'html.parser')
    
    headline = headline_soup.find('h1', class_ = 'asset-headline speakable-headline').text
    author = headline_soup.find('span', class_ = 'asset-metabar-author asset-metabar-item').text.split(',')[0]
    published = headline_soup.find('span', class_ = 'asset-metabar-time asset-metabar-item nobyline').text.split('|')[0].replace('\n', '')[22:] # I know its a mess, ignore the chaining of functions; I'm lazy as fuuuucccck
    information[i] = {'headline': headline, 'author': author, 'published': published}

with open('freep.csv', mode = 'w') as csv_file:
    fieldnames = ['headline', 'author', 'published']
    writer = csv.DictWriter(csv_file, fieldnames = fieldnames)
    
    writer.writeheader()
    for i in information:
        writer.writerow(information[i])
    
print('The script took {0} seconds to run.'.format(time.time() - startTime))    