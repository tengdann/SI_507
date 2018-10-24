# 507 Homework 7 Part 1
import requests
import json
from bs4 import BeautifulSoup

baseurl = 'https://www.si.umich.edu'
directory_url = baseurl + '/directory?rid=All'
header = {'User-Agent': 'SI_CLASS'}
umsi_titles = {}

CACHE_FNAME = 'cache.json'
try:
    cache_file = open(CACHE_FNAME, 'r')
    cache_contents = cache_file.read()
    CACHE_DICTION = json.loads(cache_contents)
    cache_file.close()

except:
    CACHE_DICTION = {}
    
def make_request_using_cache(url, header):
    unique_ident = url

    ## first, look in the cache to see if we already have this data
    if unique_ident in CACHE_DICTION:
        # print("Getting cached data...")
        return CACHE_DICTION[unique_ident]

    ## if not, fetch the data afresh, add it to the cache,
    ## then write the cache to file
    else:
        # print("Making a request for new data...")
        # Make the request and cache the new data
        resp = requests.get(url, headers=header)
        CACHE_DICTION[unique_ident] = resp.text
        return CACHE_DICTION[unique_ident]

#### Your Part 1 solution goes here ####
def get_umsi_data(page):
    page_text = make_request_using_cache(page, header)
    page_soup = BeautifulSoup(page_text, 'html.parser')
    contact_details = page_soup.find_all(class_ = 'field field-name-contact-details field-type-ds field-label-hidden')
    for contact in contact_details:
        contact_url = baseurl + contact.find('a')['href']
        contact_soup = BeautifulSoup(make_request_using_cache(contact_url, header), 'html.parser')
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
print(umsi_titles)

dumped_json_cache = json.dumps(CACHE_DICTION)
fw = open(CACHE_FNAME,"w")
fw.write(dumped_json_cache)
fw.close() # Close the open file

#### Write out file here #####