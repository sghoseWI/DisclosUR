import requests
import json
import urllib


def search_by_officer(name, state):
    '''Takes the name of a legislator and their two-letter state code as strings;
    calls the OpenCorporates API to do an officer name search within
    that state. Returns a list of officers who are a positive name-match,
    their companies, and their positions at those companies.
    '''

    juris_code = "&jurisdiction_code=us_" + state.lower()
    name = name.replace(" ", "+")
    search_url = "https://api.opencorporates.com/v0.4/officers/search?q=" + name + juris_code
    response = requests.get(search_url)
    officer_list = []
    if response.status_code == 200:
        result = json.loads(response.content)
        for officer in result["results"]["officers"]:
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
