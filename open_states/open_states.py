# Nick Tallant
# Working with the Open States API / JSON data
# Returns Legislators and Metadata from a latitiude and longitude

import pyopenstates
import requests 
import json

#api key stored locally for now - probably shouldn't be public.

os_key = ""
gmaps_key = ""

def get_location(address, gmaps_key=gmaps_key):
    '''
    Returns gps coordinates for a given address
    Input: address (string), api keys
		Output: lat, lon (floats)
    '''
    location_string = "+".join(address.split())
    myurl = "https://maps.googleapis.com/maps/api/geocode/json?address={}&key={}".format(location_string, gmaps_key)
    #example https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key=YOUR_API_KEY

    # Extract lat and lon from JSON here
    r = requests.get(myurl)
    google_data = r.json()
    loc_dict = google_data['results'][0]['geometry']['location']
    lat, lon = loc_dict['lat'], loc_dict['lng']
    return lat,lon

def get_legislator_data(address, gmaps_key=gmaps_key, os_key=os_key):
	'''
	Returns legislator metadata from an address.
		Calls get_location (google maps api).
		Input: address (string), api keys
		Output: Dictionary (JSON)
	'''
	pyopenstates.set_api_key(os_key)
	lat, lon = get_location(address, gmaps_key)
	return pyopenstates.locate_legislators(lat, lon)[0]['full_name']

