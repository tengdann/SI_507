import plotly.plotly as py
import csv

f = open('CA-airports.csv')
csv_data = csv.reader(f)

lat_vals = []
lon_vals = []
text_vals = []
for row in csv_data:
    if row[0] != 'iata':
        lat_vals.append(float(row[5]))
        lon_vals.append(float(row[6]))
        text_vals.append(row[0])
        
min_lat = min(lat_vals)
max_lat = max(lat_vals)
min_lon = min(lon_vals)
max_lon = max(lon_vals)

lat_axis = [min_lat - 1, max_lat + 1]
lon_axis = [min_lon - 1, max_lon + 1]

center_lat = (min_lat + max_lat) / 2
center_lon = (min_lon + max_lon) / 2

data = [dict(
        type = 'scattergeo',
        locationmode = 'USA-states',
        lon = lon_vals,
        lat = lat_vals,
        text = text_vals,
        mode = 'markers',
        marker = dict(
            size = 8,
            symbol = 'star',
        ))]


layout = dict(
        title = 'US airports<br>(Hover for airport names)',
        geo = dict(
            scope='usa',
            projection=dict( type='albers usa' ),
            showland = True,
            landcolor = "rgb(250, 250, 250)",
            subunitcolor = "rgb(100, 217, 217)",
            countrycolor = "rgb(217, 100, 217)",
            lataxis = {'range': lat_axis},
            lonaxis = {'range': lon_axis},
            center = {'lat': center_lat, 'lon': center_lon},
            countrywidth = 3,
            subunitwidth = 3
        ),
    )        

fig = dict(data=data, layout=layout )
py.plot( fig, validate=False, filename='usa - airports' )