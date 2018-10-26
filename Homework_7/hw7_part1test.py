# 507 Homework 7 Part 1
import requests
import requests_cache
import json
import time
from bs4 import BeautifulSoup

startTime = time.time()

baseurl = 'https://www.si.umich.edu'
directory_url = baseurl + '/directory?rid=All'
header = {'User-Agent': 'SI_CLASS'}
umsi_titles = {}

requests_cache.install_cache('test_cache') 
# Credit to Emma Brennan-Wydra for pointing out a more simplistic caching methd

DICT_FNAME = 'directory_dict.json'

#### Your Part 1 solution goes here ####
def get_umsi_data(page):
    page_text = requests.get(page, headers = header).text
    page_soup = BeautifulSoup(page_text, 'html.parser')
    contact_details = page_soup.find_all(class_ = 'field field-name-contact-details field-type-ds field-label-hidden')
    for contact in contact_details:
        contact_url = baseurl + contact.find('a')['href']
        contact_soup = BeautifulSoup(requests.get(contact_url, headers = header).text, 'html.parser')
        name = contact_soup.find(class_ = 'field-item even', property = 'dc:title').find('h2').text
        email = contact_soup.find(class_ = 'field field-name-field-person-email field-type-email field-label-inline clearfix').find('a')['href'].replace('mailto:', '')
        title = contact_soup.find(class_ = 'field field-name-field-person-titles field-type-text field-label-hidden').find(class_ = 'field-item even').text
        
        umsi_titles[email] = {'Name': name, 'Title': title}
    
    try:
        next_url = baseurl + page_soup.find('li', class_ = 'pager-next last').find('a')['href']
        get_umsi_data(next_url)
    except:
        pass
        

#### Execute funciton, get_umsi_data, here ####
get_umsi_data(directory_url)
print("Got %d in umsi_titles" % len(umsi_titles))

#### Write out file here #####
# TODO later: check if umsi_titles already exists in DICT_FNAME?
dumped_json_cache = json.dumps(umsi_titles)
fw = open(DICT_FNAME, 'w')
fw.write(dumped_json_cache)
fw.close()

print('The script took {0} seconds to run.'.format(time.time() - startTime))