#1.0 Import Library
import json
import folium
import pandas as pd
from folium.plugins import MarkerCluster
from folium import FeatureGroup, LayerControl, Map, Marker
from folium.plugins import HeatMap

for_map = pd.read_csv('geoprocessed1.csv')
df = for_map



hmap = folium.Map(location=[13.73,100.59], zoom_start=11)

x = df[df.classs != 'o']
onlyt = x[x.classs != 'a']
onlya = x[x.classs != 't']

y = df[df.classs != 't']
onlyo = y[y.classs != 'a']

accidents = HeatMap( list(zip(onlya.latitude.values, onlya.longitude.values)),
                     min_opacity=0.3,
                     radius=17, blur=50,
                     max_zoom=1, gradient={.4: 'red', .65: 'purple', 1: 'blue'} )


traffic = HeatMap( list(zip(onlyt.latitude.values, onlyt.longitude.values)),
                     min_opacity=0.3,
                     radius=17, blur=50,
                     max_zoom=1, gradient={.4: 'blue', .65: 'purple', 1: 'blue'} )

others = HeatMap( list(zip(onlyo.latitude.values, onlyo.longitude.values)),
                     min_opacity=0.3,
                     radius=17, blur=50,
                     max_zoom=1, gradient={.4: 'green', .65: 'purple', 1: 'blue'} )



# hmap.add_child(HeatMap(data, radius = 25, gradient={.4: 'blue', .65: 'lime', 1: 'red'}))

hmap.add_child(accidents)
hmap.add_child(traffic)
hmap.add_child(others)
hmap.save('heatmap.html')














#Load Data
geo_data = json.load(open("thailand.json"))
accident_data = pd.read_csv("Accident.csv")
traffic_data = pd.read_csv("Traffic.csv")



data = pd.read_csv("geoprocessed0.csv")
lat = data['latitude']
lon = data['longitude']
input = data['input_string']
intense = data['intensity']
clas= data['class']


# #Function to change colors
# def color_change(clas):
#     if(clas=='a'):
#         return('red')
#     elif(clas=='t'):
#        return('blue')
#     else:
#        return('green')


#Function to change colors
def color_change(clas,intense):
    if(clas=='a'):
        if(intense<3):
            return('#ffff66')
        elif(3.1<=intense<=7):
            return('#ff9933')
        elif(intense>7):
            return('red')
    elif(clas=='t'):
       if(intense<3):
           return('#ccccff')
       elif(3.1<=intense<=7):
           return('#66ccff')
       elif(intense>7):
           return('#0066cc')
    else:
       return('green')



#Create base map
map = folium.Map(location=[13.73,100.59], zoom_start = 11)
#map = folium.Map(location=[37.296933,-121.9574983], zoom_start = 5)

marker_cluster = MarkerCluster().add_to(map)

#Plot Markers
for lat, lon,input,clas,intense in zip(lat, lon,input,clas,intense):
    folium.CircleMarker(location=[lat, lon], radius = 9, popup=str(input)+" m", fill_color=color_change(clas,intense), color="gray", fill_opacity = 0.9).add_to(marker_cluster)
    #folium.Marker(location=[lat, lon], popup=str(input)+" m").add_to(marker_cluster)


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
