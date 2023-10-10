import requests
import json

def geocode(address):
    base_url = "https://nominatim.openstreetmap.org/search"
    params = {
        'q': address,
        'format': 'json'
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

def reverse_geocode(lat, lon):
    base_url = "https://nominatim.openstreetmap.org/reverse"
    params = {
        'lat': lat,
        'lon': lon,
        'format': 'json'
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

address_to_search = "Masjid Istiqlal, Jakarta"
data = geocode(address_to_search)
if data:
    print(json.dumps(data, indent=4))

# Or for reverse geocoding
# lat, lon = 37.4220, -122.0841
# data = reverse_geocode(lat, lon)
# if data:
#     print(json.dumps(data, indent=4))