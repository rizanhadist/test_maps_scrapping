import requests
import json

def get_location_details(address=None, latlng=None, api_key='YOUR_API_KEY'):
    base_url = "https://maps.googleapis.com/maps/api/geocode/json?"

    if address:
        params = {
            'address': address,
            'key': api_key
        }
    elif latlng:
        params = {
            'latlng': latlng,
            'key': api_key
        }
    else:
        print("You must provide either an address or a latlng.")
        return None

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Error occurred:", response.status_code)
        return None

address = "1600 Amphitheatre Parkway, Mountain View, CA"
data = get_location_details(address=address)
print(json.dumps(data, indent=4))

# Or to get details based on latitude and longitude:
# latlng = "37.4220,-122.0841"
# data = get_location_details(latlng=latlng)
# print(json.dumps(data, indent=4))