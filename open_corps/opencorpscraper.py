import requests
import json
import urllib
import pandas as pd

def corp_scraper(cpi_file, row_index, num_rows):
    ''' Takes the CPI data and scrapes the OpenCorps API. Use the parameters
    to configure the portion of the dataset we want to search, to manage
    API calls. '''

    df = pd.read_csv(cpi_file, encoding = "ISO-8859-1")
    for row in df.iterrows():
        # create a dictionary for each lawmaker
        leg_dict = {df.lawmaker:{"state":df.state,
        for interest in leg_dict["interest"]:
            open_corp_dict = get_interest_info(entity)
            leg_dict["interest"].append(open_corp_dict)
        leg_dict = corp_scrap(leg_dict)

def get_entity_info(leg_dict):
    ''' Takes a dictionary consisting of a legislator, their state, and their
    listed business / employer interests, and scrapes the OpenCorp API for
    entities matching their business / employer interests'''

        interest = interest.replace(" ", "+")
        search_url = "https://api.opencorporates.com/v0.4/companies/search?q="
        + interest
        # make the api call
        response = requests.get(search_url)
        if response.status_code == 200:
            result = json.loads(response.content)
        else:
            print("No Response") # test code if we're out of calls
        # collect all matching company numbers
        for entity in result["results"]["companies"]:
            e = entity["company"]["jurisdiction_code"] + "/"
            + entity["company"]["company_number"]
            entity_numbers.append(e)
            entity_list = []
        # collect information on company numbers
        # probably want to cap the number of entities we crawl
        for entity in entity_numbers:
            search_url = "https://api.opencorporates.com/v0.4/companies/" + entity
            response = requests.get(search_url)
            if response.status_code == 200:
                result = json.loads(response.content)
            else:
                print("no response")
            entity_list.append(result["results"]["company"])
        # process the entity list to remove entities that we don't want
        return entity_list
