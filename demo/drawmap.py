#1.0 Import Library
import json
import folium
import pandas as pd
from folium.plugins import MarkerCluster

#Load Data
geo_data = json.load(open("thailand.json"))
accident_data = pd.read_csv("Accident.csv")
traffic_data = pd.read_csv("Traffic.csv")


data = pd.read_csv("geoprocessed.csv")
lat = data['latitude']
lon = data['longitude']
elevation = data['input_string']


#Function to change colors
def color_change(elev):
    if(len(elevation)%2==0):
        return('red')
    else:
       return('cadetblue1')



#Create base map
map = folium.Map(location=[13.73,100.59], zoom_start = 11)
#map = folium.Map(location=[37.296933,-121.9574983], zoom_start = 5)

marker_cluster = MarkerCluster().add_to(map)

#Plot Markers
for lat, lon,elevation in zip(lat, lon,elevation):
    folium.CircleMarker(location=[lat, lon], radius = 9, popup=str(elevation)+" m", fill_color=color_change(elevation), color="gray", fill_opacity = 0.9).add_to(marker_cluster)


#Method to create Choropleth map, All parameters are mandatory
folium.Choropleth(
    geo_data=geo_data, data=accident_data,
    name = 'Accidents',
    columns=['Type', 'Rate'],
    key_on='feature.id',
    fill_color='YlOrRd', fill_opacity=0.2, line_opacity=0.2,
    legend_name='Accidents'
).add_to(map)

folium.Choropleth(
    geo_data=geo_data, data=traffic_data,
    name = 'Traffic',
    columns=['Type', 'Rate'],
    key_on='feature.id',
    fill_color='Blues', fill_opacity=0.2, line_opacity=0.2,
    legend_name='Traffic'
).add_to(map)


#Save the map
map.save("map1.html")
