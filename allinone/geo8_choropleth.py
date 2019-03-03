#1.0 Import Library
import json
import folium
import pandas as pd
from folium.plugins import MarkerCluster

#Load Data
geo_data = json.load(open("thailand.json"))
emp_data = pd.read_csv("us-unemployment.csv")

data = pd.read_csv("data/output-2015.csv")
lat = data['latitude']
lon = data['longitude']
elevation = data['input_string']


#Function to change colors
def color_change(elev):
    if(True):
        return('green')



#    elif(1000 <= elev <3000):
#        return('orange')
#    else:
#        return('black')



#Create base map
map = folium.Map(location=[13.73,100.59], zoom_start = 11)
#map = folium.Map(location=[37.296933,-121.9574983], zoom_start = 5)

marker_cluster = MarkerCluster().add_to(map)

#Plot Markers
for lat, lon,elevation in zip(lat, lon,elevation):
    folium.CircleMarker(location=[lat, lon], radius = 9, popup=str(elevation)+" m", fill_color=color_change(elevation), color="gray", fill_opacity = 0.9).add_to(marker_cluster)


#Method to create Choropleth map, All parameters are mandatory
folium.Choropleth(
    geo_data=geo_data, data=emp_data,
    name = 'Unemployment Rate',
    columns=['State', 'Unemployment'],
    key_on='feature.id',
    fill_color='YlGn', fill_opacity=0.2, line_opacity=0.2,
    legend_name='Unemployment Rate (%)'
).add_to(map)


#Save the map
map.save("map1.html")
