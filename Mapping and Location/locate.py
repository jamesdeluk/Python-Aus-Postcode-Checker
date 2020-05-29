import json

postcode = 4101

file1 = 'Resources/au_postcodes.json'

with open(file1) as json_file1:
    data1 = json.load(json_file1)

for region in data1:
    if region['postcode'] == postcode:
        print(region['place_name'])

file2 = 'Resources/australian_postcodes.json'

with open(file2) as json_file2:
    data2 = json.load(json_file2)

for region in data2:
    if region['postcode'] == postcode:
        print(region['locality'])

# import requests

# gets = requests.get(f'http://v0.postcodeapi.com.au/suburbs/{postcode}.json').json()
# for got in gets:
#     print(got['name'])


# from geopy.geocoders import Nominatim
# glnom = Nominatim(user_agent="aswpc")

# location = glnom.geocode("brisbane", country_codes='au')
#viewbox=[(-44,112), (-10,153)], bounded=True
# print(location)
# print((location.latitude, location.longitude))
# print(location.raw)

# location = geolocator.reverse("52.509669, 13.376294")
# print(location.address)
# print((location.latitude, location.longitude))
# print(location.raw)

# from geopy.geocoders import GoogleV3
# geopygoogle = GoogleV3(api_key="")

# location = geopygoogle.geocode("Australia 3640")
# print(location)

# import googlemaps
# # from datetime import datetime

# gmaps = googlemaps.Client(key="")

# geocode_result = gmaps.geocode('3640 Australia')
# print(geocode_result)

# reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))
# print(reverse_geocode_result)

# now = datetime.now()
# directions_result = gmaps.directions("Sydney Town Hall",
#                                      "Parramatta, NSW",
#                                      mode="transit",
#                                      departure_time=now)
# print(directions_result)

# temp = googlemaps.geolocation.geolocate('Chrome')
# print(temp)
