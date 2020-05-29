import folium
import pandas

data = pandas.read_csv("Data/australian_postcodes.csv")
data=data.dropna(subset=['lat'])
data=data.dropna(subset=['long'])
postcodes = list(data["postcode"])
localities = list(data["locality"])
lats = list(data["lat"])
lons = list(data["long"])

# print(len(postcodes))
# print(len(localities))
# print(len(lats))
# print(len(lons))

# def marker_colours(elev):
#   if elev < 1000:
#     return "darkgreen"
#   elif 1000 <= elev < 3000:
#     return "green"
#   else:
#     return "lightgreen"
# 
# color=marker_colours(elev)

map = folium.Map(location=[-26.1772288,133.4170119], zoom_start=5)

fg_points = folium.FeatureGroup(name="Points")



for i in range(0, 15614):
  fg_points.add_child(folium.CircleMarker(location=[lats[i],lons[i]], popup=localities[i] + ": " + str(postcodes[i]), fill=True, fill_color="red", color="red", radius=3))

# for lat, lon in zip(lats, lons):
#   fg_points.add_child(folium.CircleMarker(location=[lats,lons], fill=True, fill_color="blue", radius=3))
#   print(lat, lon)


fg_areas = folium.FeatureGroup(name="Areas")

fg_areas.add_child(folium.GeoJson(data=open('Data/GeoJson-Data-master/australian-suburbs.geojson', 'r', encoding='utf-8-sig').read()
# , style_function=lambda x: {'fillColor':'green'}
))

map.add_child(fg_areas)
map.add_child(fg_points)
map.add_child(folium.LayerControl())

map.save("Map.html")

print("Done")

# print(str(postcode[0]) + " " + locality[0] + " " + str(lats[0]) + " " + str(lons[0]))