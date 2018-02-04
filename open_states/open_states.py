# Nick Tallant
# Working with the Open States API / JSON data
# Returns Legislators and Metadata from a latitiude and longitude

import pyopenstates
import urllib3
import json

#api key stored locally for now - probably shouldn't be public.
#pyopenstates.set_api_key(ok_jey)

gmaps_key = ""

def get_google_data(gmaps_key, address):
	'''
	Returns location data in JSON
	'''
	location_string = "+".join(address.split())
	myurl = "https://maps.googleapis.com/maps/api/geocode/json?address={}&key={}".format(location_string, gmaps_key)
	#example https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key=YOUR_API_KEY

	# Extract lat and lon from JSON here
	pm = urllib3.PoolManager()

	google_data = pm.urlopen(url=myurl, method="GET")
	hm = google_data.read()
	
	#rv = json.loads(hm.decode())
	return type(hm)

#legislators = pyopenstates.locate_legislators(lat,lon)

