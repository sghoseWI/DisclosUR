import requests
import json
import urllib
from django.db import models
from dotenv import get_key, find_dotenv

def search_by_officer(name, state):
    # for each business / employer interest listed by a legislator, call the
    # OpenCorp search API, filtering out results whose incorporation post-dates
    # the CPI dataset
    juris_code = "&jurisdiction_code=us_" + state.lower()
    name = name.replace(" ", "+")
    search_url = "https://api.opencorporates.com/v0.4/officers/search?q=" + name + juris_code
    print(search_url)
    response = requests.get(search_url)
    officer_list = []
    if response.status_code == 200:
        result = json.loads(response.content)
        for officer in result["results"]["officers"]:
            print(officer)
            name = officer["officer"]["name"]
            position = officer["officer"]["position"]
            company_name = officer["officer"]["company"]["name"]
            open_corp_url = officer["officer"]["company"]["opencorporates_url"]
            sep = " "
            s = name, position, company_name, open_corp_url
            new_officer = sep.join(s)
            officer_list.append(new_officer)
    else:
        print("Status code error #: ", response.status_code) # for debugging
    return officer_list
