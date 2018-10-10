# 507 Homework 6 Extra Credit 1
import requests
import sys
import codecs
from bs4 import BeautifulSoup
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

#### Extra Credit 2 ####
print('\n*********** EXTRA CREDIT 2 ***********')
print('Re-sort Atheletes by State\n')

### Your Extra Credit 2 solution goes here
url_mens = "https://www.athletic.net/CrossCountry/meet/135827/results/557666"

html_mens = requests.get(url_mens).text
print(html_mens)

soup_mens = BeautifulSoup(html_mens, 'html.parser')

table_mens = soup_mens.find('table', class_ = 'table DataTable table-responsive table-hover mb-0')
print(table_mens)
