# Returns Legislators and Metadata from a latitiude and longitude

import pyopenstates

#api key stored locally for now - probably shouldn't be public.
pyopenstates.set_api_key(api_jey)

legislators = pyopenstates.locate_legislators(lat,lon)
