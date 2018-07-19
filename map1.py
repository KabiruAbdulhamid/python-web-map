import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000<= elevation < 3000:
        return 'red'
    else:
        return 'blue'

map = folium.Map(location=[40.07, -103.5], zoom_start=5, tiles="Mapbox Bright")
fgv=folium.FeatureGroup(name="volcanoes")

for lt, ln, el, in zip(lat, lon, elev):
    fgv.add_child(folium.CircleMarker(location=[lt, ln], popup=str(el)+" M", radius=6, fill_color=color_producer(el), fill='true', color='none',  fill_opacity=0.7))

fgp=folium.FeatureGroup(name="population")

fgp.add_child(folium.GeoJson(data=open('world.json','r', encoding='utf-8-sig').read(),style_function = lambda x:{'fillColor':'yellow' if x['properties']['POP2005']<10000000
else 'green' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fgp)
map.add_child(fgv)

map.add_child(folium.LayerControl())
map.save("map1.html")
