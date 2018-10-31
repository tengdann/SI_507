import codecs
import requests
import requests_cache
import json
import secret
import sys
import plotly
import plotly.plotly as py
import plotly.graph_objs as go

sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

# Don't change this part
FLICKR_KEY = secret.FLICKR_KEY
MAPBOX_TOKEN = secret.MAPBOX_TOKEN
PLOTLY_USERNAME = secret.PLOTLY_USERNAME
PLOTLY_API_KEY = secret.PLOTLY_API_KEY

plotly.tools.set_credentials_file(username=PLOTLY_USERNAME, api_key=PLOTLY_API_KEY)

base_url = "https://api.flickr.com/services/rest"
requests_cache.install_cache('flickr_api')

city = ''
for i in sys.argv[1:]:
    city = city + i + ' '
city_query = {'query': city[:-1]}

'''
 Compose the url for requests to use.
 Parameters:
    method: string. The API method you want to use. e.g. "flickr.galleries.getInfo"
    parameter: dictionary. The parameters for the API query. e.g. {"gallery_id": "72157617483228192"}
 Returns: string. A composed url for requests to use. 
'''
def compose_url(method, parameter):
    temp_list = []
    for i in parameter:
        temp_list.append(str(i) + "=" + str(parameter[i]).replace(" ", "+"))
    parameter_string = "&".join(temp_list)
    return base_url+"/?method={}&api_key={}&{}&format=json&nojsoncallback=1".format(method, FLICKR_KEY, parameter_string)

# -----------------------------------------------------------------------------

# ----------------------------------------------
# Part 1: Get photo information using Flickr API
# ----------------------------------------------
print("----------------Part1--------------------")
print()
loc_find_method = 'flickr.places.find'
loc_photo_method = 'flickr.photos.search'
photo_info_method = 'flickr.photos.getInfo'

place = requests.get(compose_url(loc_find_method, city_query)).json()
place_id = place['places']['place'][0]['place_id']

photo_params = {'place_id': place_id, 'per_page': 250}
photos = requests.get(compose_url(loc_photo_method, photo_params)).json()
list_ids = []
list_owners = []
for photo in photos['photos']['photo']:
    if photo['owner'] not in list_owners:
        list_owners.append(photo['owner'])
        list_ids.append(photo['id'])

photo_info = []
for id in list_ids:
    query = {'photo_id': id}
    info = requests.get(compose_url(photo_info_method, query)).json()
    print("Photo id: ", id)
    print("Title: ", info['photo']['title']['_content'])
    print("Description: ", info['photo']['description']['_content'])
    print()
    
    photo_info.append({'Lat': info['photo']['location']['latitude'], 'Lon': info['photo']['location']['longitude'], 'Title': info['photo']['title']['_content'], 'Link': info['photo']['urls']['url'][0]['_content']})

# ----------------------------------------------
# Part 2: Map data onto Plotly
# ----------------------------------------------
lon_vals = []
lat_vals = []
text_vals = []

for photo in photo_info:
    lon_vals.append(photo['Lon'])
    lat_vals.append(photo['Lat'])
    text_vals.append("%s<br>%s" % (photo['Title'], photo['Link']))    

data = [
        go.Scattermapbox(
            lat = lat_vals,
            lon = lon_vals,
            mode = 'markers',
            marker = dict(
                size = 12,
                symbol = 'circle',
                color = 'blue'
            ),
            text = text_vals
        )
    ]
        
layout = dict(
        title = 'Ann Arbor Photos<br>(Hover for more info)',
        autosize=True,
        showlegend = False,
        mapbox=dict(
            accesstoken=MAPBOX_TOKEN,
            bearing=0,
            center=dict(
                lat=42.2808,
                lon=-83.7430
            ),
            pitch=0,
            zoom=11,
        ),
    )        

fig = dict(data=data, layout=layout)
py.plot(fig, filename='aa - photos')