# 507 Homework 6 Part 1
import requests
import sys
from bs4 import BeautifulSoup

#### Part 1 ####
print('\n*********** PART 1 ***********')
print("-------Alt tags-------\n")

### Your Part 1 solution goes here ###
url = sys.argv[1] # url = http://newmantaylor.com/gallery.html

html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')

# print(soup.prettify())

alt_tags = soup.find_all('img')

for alt in alt_tags:
    try:
        print(alt['alt'])
    except:
        print("No alternate text provided!!")
