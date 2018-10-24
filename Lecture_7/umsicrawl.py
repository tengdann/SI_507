from bs4 import BeautifulSoup
import requests
import json

baseurl = 'https://www.si.umich.edu'
catalog_url = baseurl + '/programs/courses/catalog'
header = {'User-Agent': 'SI_CLASS'}

CACHE_FNAME = 'cache.json'
try:
    cache_file = open(CACHE_FNAME, 'r')
    cache_contents = cache_file.read()
    CACHE_DICTION = json.loads(cache_contents)
    cache_file.close()

# if there was no file, no worries. There will be soon!
except:
    CACHE_DICTION = {}

class CourseListing:
    header = {'User-Agent': 'SI_CLASS'}
    def __init__(self, course_num, course_name):
        self.num = course_num
        self.name = course_name

    def __str__(self):
        course_str = self.num + ' ' + self.name + '\n\n\t' + self.description + '\n\n' + self.prereq
        return course_str
        
    def init_from_details_url(self, details_url):
        # page_text = requests.get(details_url, headers = self.header).text
        page_text = make_request_using_cache(details_url, header)
        page_soup = BeautifulSoup(page_text, 'html.parser')
        self.description = page_soup.find(class_ = 'course2desc').text[:-14]
        self.prereq = page_soup.find(class_ = 'course2prer').text
        
def get_unique_key(url):
    return url

def make_request_using_cache(url, header):
    unique_ident = get_unique_key(url)

    ## first, look in the cache to see if we already have this data
    if unique_ident in CACHE_DICTION:
        print("Getting cached data...")
        return CACHE_DICTION[unique_ident]

    ## if not, fetch the data afresh, add it to the cache,
    ## then write the cache to file
    else:
        # print("Making a request for new data...")
        # Make the request and cache the new data
        resp = requests.get(url, headers=header)
        CACHE_DICTION[unique_ident] = resp.text
        dumped_json_cache = json.dumps(CACHE_DICTION)
        fw = open(CACHE_FNAME,"w")
        fw.write(dumped_json_cache)
        fw.close() # Close the open file
        return CACHE_DICTION[unique_ident]
    
# user_input = input("Enter in the class you would like to search for: ")
# search_url = catalog_url + '?search=' + user_input
# page_text = requests.get(catalog_url, headers = header).text
page_text = make_request_using_cache(catalog_url, header)
page_soup = BeautifulSoup(page_text, 'html.parser')

content_div = page_soup.find(class_ = 'view-content')

# while content_div is None:
    # print("Sorry, that class doesn't exist!", end = ' ')
    # user_input = input("Enter in the class you would like to search for: ")
    # search_url = catalog_url + '?search=' + user_input
    # page_text = requests.get(search_url, headers = header).text
    # page_soup = BeautifulSoup(page_text, 'html.parser')

    # content_div = page_soup.find(class_ = 'view-content')

table_rows = content_div.find_all('tr')
course_listings = []

for i in range(25):
# for tr in table_rows:
    table_cells = table_rows[i].find_all('td')
    if len(table_cells) == 2:
        # extract course number and course name
        course_number = table_cells[0].text.strip()
        course_name = table_cells[1].text.strip()
        
        
        # crawl over to the details page
        details_url_end = table_cells[0].find('a')['href']
        details_url = baseurl + details_url_end
        course_listing = CourseListing(course_number, course_name)
        course_listing.init_from_details_url(details_url)
        course_listings.append(course_listing)

# table_cells = table_rows[1].find_all('td')
# if len(table_cells) == 2:
    # extract course number and course name
    # course_number = table_cells[0].text.strip()
    # course_name = table_cells[1].text.strip()
    
    
    # crawl over to the details page
    # details_url_end = table_cells[0].find('a')['href']
    # details_url = baseurl + details_url_end
    # course_listing = CourseListing(course_number, course_name)
    # course_listing.init_from_details_url(details_url)
    # course_listings.append(course_listing)
    
for cl in course_listings:
    print(cl)
    print('--' * 40)