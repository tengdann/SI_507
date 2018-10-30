import plotly.plotly as py
from secret import *
import csv

f = open('2011_february_us_airport_traffic.csv')
csv_data = csv.reader(f)

big_lat_vals = []
big_lon_vals = []
big_text_vals = []
small_lat_vals = []
small_lon_vals = []
small_text_vals = []
for row in csv_data:   
    if row[0] != 'iata':
        traffic = int(row[7])
        lat = row[5]
        lon = row[6]
        text = row[0]
        if traffic > 1000:
            big_lat_vals.append(float(row[5]))
            big_lon_vals.append(float(row[6]))
            big_text_vals.append(row[0])
        else:
            small_lat_vals.append(float(row[5]))
            small_lon_vals.append(float(row[6]))
            small_text_vals.append(row[0])

trace1 = dict(
        type = 'scattermapbox',
        locationmode = 'USA-states',
        lon = big_lon_vals,
        lat = big_lat_vals,
        text = big_text_vals,
        mode = 'markers',
        marker = dict(
            size = 15,
            symbol = 'star',
            color = 'red'
        ))
trace2 = dict(
        type = 'scattermapbox',
        locationmode = 'USA-states',
        lon = small_lon_vals,
        lat = small_lat_vals,
        text = small_text_vals,
        mode = 'markers',
        marker = dict(
            size = 8,
            symbol = 'circle',
            color = 'blue'
        ))

data = [trace1, trace2]

layout = dict(
        title = 'US airports<br>(Hover for airport names)',
        autosize=True,
        showlegend = False,
        mapbox=dict(
            accesstoken=MAPBOX_TOKEN,
            bearing=0,
            center=dict(
                lat=38,
                lon=-94
            ),
            pitch=0,
            zoom=3,
        ),
    )        

fig = dict(data=data, layout=layout )
py.plot( fig, validate=False, filename='usa - airports' )