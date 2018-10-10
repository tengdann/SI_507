# 507 Homework 6 Part 2
import requests
from bs4 import BeautifulSoup


#### Part 2 ####
print('\n*********** PART 2 ***********')
print('Michigan Daily -- MOST READ\n')

### Your Part 2 solution goes here

url = "https://www.michigandaily.com/"
html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')

main_find = soup.find('div', class_ = 'panel-pane pane-mostread')
most_read_list = main_find.find_all('li')
for title in most_read_list:
    print(title.text)
