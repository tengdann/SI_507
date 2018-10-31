## proj_nps.py
## Skeleton for Project 2, Fall 2018
## ~~~ modify this file, but don't rename it ~~~
import requests
import requests_cache
from bs4 import BeautifulSoup
from secrets import google_places_key

npsurl = 'https://www.nps.gov'
index_url =  npsurl + '/index.htm'
googleurl = 'https://maps.googleapis.com/maps/api/place/'
requests_cache.install_cache('nps_cache')

## you can, and should add to and modify this class any way you see fit
## you can add attributes and modify the __init__ parameters,
##   as long as tests still pass
##
## the starter code is here just to make the tests run (and fail)
class NationalSite():
    def __init__(self, type, name, desc, url=None):
        if type != '':
            self.type = type
        else:
            self.type = "No type found!"
        self.name = name
        self.description = desc
        self.url = url

        park_soup = BeautifulSoup(requests.get(url).text, 'html.parser')
        self.address_street = park_soup.find('span', itemprop = 'streetAddress').text.split('\n')[1]
        self.address_city = park_soup.find('span', itemprop = 'addressLocality').text
        self.address_state = park_soup.find('span', itemprop = 'addressRegion').text
        self.address_zip = park_soup.find('span', itemprop = 'postalCode').text[:-5]
        
    def __str__(self):
        string = '%s (%s): %s, %s, %s %s' % (self.name, self.type, self.address_street, self.address_city, self.address_state, self.address_zip)
        return string

## you can, and should add to and modify this class any way you see fit
## you can add attributes and modify the __init__ parameters,
##   as long as tests still pass
##
## the starter code is here just to make the tests run (and fail)
class NearbyPlace():
    def __init__(self, name):
        self.name = name

## Must return the list of NationalSites for the specified state
## param: the 2-letter state abbreviation, lowercase
##        (OK to make it work for uppercase too)
## returns: all of the NationalSites
##        (e.g., National Parks, National Heritage Sites, etc.) that are listed
##        for the state at nps.gov
def get_sites_for_state(state_abbr):
    list_sites = []
    state_url = npsurl + '/state/%s/index.htm' % (state_abbr.lower())
    page_soup = BeautifulSoup(requests.get(state_url).text, 'html.parser')
    
    list_parks = page_soup.find_all('li', class_ = 'clearfix')
    for park in list_parks[:-1]:
        name = park.find('a').text
        type = park.find('h2').text
        desc = park.find('p').text[1:-1]
        park_url = npsurl + park.find('a')['href'] + 'planyourvisit/basicinfo.htm'
        list_sites.append(NationalSite(type, name, desc, park_url))
    
    return list_sites


## Must return the list of NearbyPlaces for the specifite NationalSite
## param: a NationalSite object
## returns: a list of NearbyPlaces within 10km of the given site
##          if the site is not found by a Google Places search, this should
##          return an empty list
def get_nearby_places_for_site(national_site):
    search_query = national_site.name + national_site.type
    return []

## Must plot all of the NationalSites listed for the state on nps.gov
## Note that some NationalSites might actually be located outside the state.
## If any NationalSites are not found by the Google Places API they should
##  be ignored.
## param: the 2-letter state abbreviation
## returns: nothing
## side effects: launches a plotly page in the web browser
def plot_sites_for_state(state_abbr):
    pass

## Must plot up to 20 of the NearbyPlaces found using the Google Places API
## param: the NationalSite around which to search
## returns: nothing
## side effects: launches a plotly page in the web browser
def plot_nearby_for_site(site_object):
    pass