import phonenumbers
import folium
from myphone import number
from phonenumbers import geocoder
from phonenumbers import carrier
from opencage.geocoder import OpenCageGeocode


pepnumber = phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumber, "en")
print(location)

service_pro = phonenumbers.parse(number)
print(carrier.name_for_number(service_pro, "en"))

key = "851313194061482b9740ac6c8a1ac609"

geocoder = OpenCageGeocode(key)
query = str(location)
result = geocoder.geocode(query)
print(result)
lat = result[0]['geometry']['lat']
lng = result[0]['geometry']['lng']
print(lat, lng)

mymap = folium.Map(location=[lat, lng], zoom_start=9)

folium.Marker([lat, lng], popup=location).add_to(mymap)
mymap.save("mylocatiom2.html")
