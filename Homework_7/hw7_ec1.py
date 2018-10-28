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

headline = []
headlines_links = []

raw_links = freep_soup.find_all('a', itemprop = 'url', limit = 10)
for raw_link in raw_links:
    try:
        headline.append(raw_link.find('span', class_ = 'hgpm-list-hed js-asset-headline placeholder-bg ').text)
    except:
        headlines.append(None)
    headlines_links.append(baseurl + raw_link['href'])

information = {}
author = []
published = []
    
for i in headlines_links:
    headline_text = requests.get(i).text
    headline_soup = BeautifulSoup(headline_text, 'html.parser')
    
    try:
        author.append(headline_soup.find('span', class_ = 'asset-metabar-author asset-metabar-item').text.split(',')[0])
    except:
        author.append(None)
        
    try:
        published.append(headline_soup.find('span', class_ = 'asset-metabar-time asset-metabar-item nobyline').text.split('|')[0].replace('\n', '')[22:]) # I know its a mess, ignore the chaining of functions; I'm lazy as fuuuucccck
    except:
        published.append(None)

for i,h,a,p in zip(headlines_links,headline, author, published):
    if i is not None and h is not None and a is not None and p is not None:
        information[i] = {'headline': h, 'author': a, 'published': p}

with open('freep.csv', mode = 'w') as csv_file:
    fieldnames = ['headline', 'author', 'published']
    writer = csv.DictWriter(csv_file, fieldnames = fieldnames)
    
    writer.writeheader()
    for i in information:
        writer.writerow(information[i])
        
print('The script took {0} seconds to run.'.format(time.time() - startTime))    