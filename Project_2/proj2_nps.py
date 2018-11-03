## proj_nps.py
## Skeleton for Project 2, Fall 2018
## ~~~ modify this file, but don't rename it ~~~
import requests
import requests_cache
from bs4 import BeautifulSoup
from secrets import google_places_key
import plotly.plotly as py

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
    def __init__(self, type, name, desc, state=None, url=None):
        if type != '':
            self.type = type
        else:
            self.type = ''
        self.name = name
        self.description = desc
        self.url = url
        
        if url is not None:
            park_text = requests.get(url).text
            park_soup = BeautifulSoup(park_text, 'html.parser')
            
            try:
                self.address_street = park_soup.find('span', itemprop = 'streetAddress').text.split('\n')[1]
            except:
                self.address_street = "No street address found!"
                
            try:
                self.address_city = park_soup.find('span', itemprop = 'addressLocality').text
            except:
                self.address_city = "No city found!"
                
            try:
                self.address_state = park_soup.find('span', itemprop = 'addressRegion').text
            except:
                self.address_state = state
                
            try:
                self.address_zip = park_soup.find('span', itemprop = 'postalCode').text[:-5]
            except:
                self.address_zip = "No zip code found!"
            
        
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
        
    def __str__(self):
        string = '%s' % (self.name)
        return string

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
        list_sites.append(NationalSite(type, name, desc, state_abbr.upper(), park_url))
    
    return list_sites


## Must return the list of NearbyPlaces for the specifite NationalSite
## param: a NationalSite object
## returns: a list of NearbyPlaces within 10km of the given site
##          if the site is not found by a Google Places search, this should
##          return an empty list
def get_nearby_places_for_site(national_site):
    search_query = national_site.name + ' ' + national_site.type
    search_url = googleurl + "findplacefromtext/json?input=%s&inputtype=textquery&fields=geometry,name&key=%s" % (search_query.replace(' ', '%20'), google_places_key)
    search_result = requests.get(search_url).json()
    
    if len(search_result['candidates']) != 0:
        lat = search_result['candidates'][0]['geometry']['location']['lat']
        lon = search_result['candidates'][0]['geometry']['location']['lng']
    
    nearby_url = googleurl + "nearbysearch/json?location=%s,%s&radius=10000&key=%s" % (lat, lon, google_places_key)
    nearby_results = requests.get(nearby_url).json()
    nearby_names = get_nearby_names(nearby_results)
    nearby_places = []
    
    for nearby_name in nearby_names:
        if national_site.name not in nearby_name:
            nearby_places.append(NearbyPlace(nearby_name))
    return nearby_places

## Must return the list of names of NearbyPlaces for the specifite NationalSite
## param: list of NearbyPlaces
## returns: a list names of NearbyPlaces within 10km of the given site
##          if the site is not found by a Google Places search, this should
##          return an empty list   
def get_nearby_names(results):
    names = []
    for result in results['results']:
        names.append(result['name'])
    return names

## Must plot all of the NationalSites listed for the state on nps.gov
## Note that some NationalSites might actually be located outside the state.
## If any NationalSites are not found by the Google Places API they should
##  be ignored.
## param: the 2-letter state abbreviation
## returns: nothing
## side effects: launches a plotly page in the web browser
def plot_sites_for_state(state_abbr):
    list_sites = get_sites_for_state(state_abbr)
    list_coords = []
    for national_site in list_sites:
        search_query = national_site.name + ' ' + national_site.type
        search_url = googleurl + "findplacefromtext/json?input=%s&inputtype=textquery&fields=geometry,name&key=%s" % (search_query.replace(' ', '%20'), google_places_key)
        search_result = requests.get(search_url).json()
        
        if len(search_result['candidates']) != 0:
            try:
                lat = search_result['candidates'][0]['geometry']['location']['lat']
                lon = search_result['candidates'][0]['geometry']['location']['lng']
                list_coords.append((lat,lon, national_site.name))
            except:
                pass
    
    lats = [coord[0] for coord in list_coords]
    lons = [coord[1] for coord in list_coords]
    
    min_lat = min(lats)
    max_lat = max(lats)
    min_lon = min(lons)
    max_lon = max(lons)

    lat_axis = [min_lat - 1, max_lat + 1]
    lon_axis = [min_lon - 1, max_lon + 1]

    center_lat = (min_lat + max_lat) / 2
    center_lon = (min_lon + max_lon) / 2
    
    data = [dict(
            type = 'scattergeo',
            locationmode = 'USA-states',
            lat = lats,
            lon = lons,
            text = [coord[2] for coord in list_coords],
            mode = 'markers',
            marker = dict(
                size = 10,
                symbol = 'star',
                color = 'purple'
                )
            )]
    
    layout = dict(
            title = 'Plots of National Sites in %s' % (state_abbr.upper()),
            colorbar = True,
            geo = dict (
                scope = 'usa',
                projection = dict(type = 'albers usa'),
                showland = True,
                showlakes = True,
                showocean = True,
                landcolor = '#ffffba',
                lakecolor = '#add8e6',
                oceancolor = '#add8e6',
                lataxis = {'range': lat_axis},
                lonaxis = {'range': lon_axis},
                center = {'lat': center_lat, 'lon': center_lon},
                countrywidth = 3,
                subunitwidth = 3
            )
        )
        
    fig = dict(data = data, layout = layout)
    py.plot(fig, validate = False, filename = '%s - National Sites' % (state_abbr.upper()))
            

## Must plot up to 20 of the NearbyPlaces found using the Google Places API
## param: the NationalSite around which to search
## returns: nothing
## side effects: launches a plotly page in the web browser
def plot_nearby_for_site(site_object):
    pass   