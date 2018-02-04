# Returns Legislators and Metadata from a latitiude and longitude

import pyopenstates

pyopenstates.set_api_key('e84a8eb4-223e-4603-93ee-41d87f23fc56')

legislators = pyopenstates.locate_legislators(lat,lon)
