# Nick Tallant
# Working with the Open States API / JSON data
# Returns Legislators and Metadata from a latitiude and longitude

import pyopenstates
import requests 
import json

#api key stored locally for now - probably shouldn't be public.
#pyopenstates.set_api_key(os_key)

gmaps_key = ""

def get_location(gmaps_key, address):
    '''
    Returns location data in JSON
    '''
    location_string = "+".join(address.split())
    myurl = "https://maps.googleapis.com/maps/api/geocode/json?address={}&key={}".format(location_string, gmaps_key)
    #example https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key=YOUR_API_KEY

    # Extract lat and lon from JSON here

    r = requests.get(myurl)
    google_data = r.json()
    loc_dict = google_data['results'][0]['geometry']['location']
    lat, lon = loc_dict['lat'], loc_dict['lon']
    return lat, lon


#legislators = pyopenstates.locate_legislators(lat,lon)

