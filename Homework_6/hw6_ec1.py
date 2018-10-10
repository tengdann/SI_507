# 507 Homework 6 Extra Credit 1
import requests
import sys
import codecs
from bs4 import BeautifulSoup
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

#### Extra Credit 1 ####
print('\n*********** EXTRA CREDIT 1 ***********')
print('Top Headlines\n')

### Your Extra Credit 1 solution goes here
url = "https://www.michigandaily.com/"

html= requests.get(url).text

soup = BeautifulSoup(html, 'html.parser')

# News
print('Top 5 Headlines: news')
main_news = soup.find('div', {'id': 'section-news'})
news_headlines = main_news.find_all('div', class_ = 'field-content')
for news in news_headlines[1:]:
    try:
        print(news.find('a').text)
    except:
        pass
    
# Sports
print('\nTop 5 Headlines: sports')
main_sports = soup.find('div', {'id': 'section-sports'})
sports_headlines = main_sports.find_all('div', class_ = 'field-content')
for sports in sports_headlines[1:]:
    try:
        print(sports.find('a').text)
    except:
        pass
        
# Arts
# Sports
print('\nTop 5 Headlines: arts')
main_arts = soup.find('div', {'id': 'section-arts'})
arts_headlines = main_arts.find_all('div', class_ = 'field-content')
for arts in arts_headlines[1:]:
    try:
        print(arts.find('a').text)
    except:
        pass