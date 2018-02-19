import requests
import json
import urllib
import pandas as pd

test_leg_one = {"lawmaker_id":23076, "lawmaker":"ROSA, DENNIS", "state":"MA",
"interests":["AMERICAN AUTO BODY AND REPAIR INC", "EAGLE REALTY TRUST"]}
test_leg_two = {"lawmaker_id":6681989, "lawmaker":"YORK, JILL", "state":"KY",
"interests":["PRINTWORKS UNLIMITED INC."]}
test_leg_three = {"lawmaker_id":121340, "lawmaker":"PIGMAN, EDWIN", "state":"FL",
"interests":["CALADIUM ER SVCS PARTNERSHIP LLC", "CARLTON ER SVCS PARTNERSHIP LLC",
"CITY CIRCLE ER SVCS PARTNERSHIP, LLC", "DOCTORS MEMORIAL HOSPITAL", "HARDEE CO.",
]}

def corp_scraper(cpi_file, row_index, num_rows):
    '''Takes the CPI csv file and scrapes the OpenCorps API. Builds a dictionary
    of each unique legislator, where the key-value pairs are the information from
    the CPI csv file. Use the parameters to configure the portion of
    the dataset we want to search, to manage number of API calls. '''

    df = pd.read_csv(cpi_file, encoding = "ISO-8859-1")
    for row in df.iterrows():
        # create a dictionary for each lawmaker
        #leg_dict = {df.lawmaker:{"state":df.state,
        leg_dict["open_corps"] = get_entity_info(leg_dict)

def get_entity_info(leg_dict):
    ''' Takes a dictionary consisting of a legislator, their state, and their
    listed business / employer interests, and scrapes the OpenCorp API for
    entities matching their business / employer interests'''
    leg_juris_code = "us_" + leg_dict["state"].lower()
    entity_numbers = []
    entity_list = []
    # for each business / employer interest listed by a legislator, call the
    # OpenCorp search API, filtering out results whose incorporation post-dates
    # the CPI dataset
    for interest in leg_dict["interests"]:
        print("Searching OpenCorp API for: ", interest)
        interest = interest.replace(" ", "+")
        incorp_filter = "&incorporation\date=:2016-01-01"
        search_url = "https://api.opencorporates.com/v0.4/companies/search?q=" + interest + incorp_filter
        print(search_url)
        response = requests.get(search_url)
        if response.status_code == 200:
            result = json.loads(response.content)
        else:
            print("No Response") # test code if we're out of calls
        # collect all company numbers that may match the business / employer interest
        for entity in result["results"]["companies"]:
            print("Considering ", entity["company"]["name"])
            # if there are a lot of results, filter on the state; might want to filter
            # on status too
            if len(result["results"]["companies"]) > 5 and entity["company"]["jurisdiction_code"] == leg_juris_code:
                print("Passing on", entity["company"]["name"], "because its jurisdiction code is ", entity["company"]["jurisdiction_code"], "not ", leg_juris_code)
                pass
            else:
                num = entity["company"]["jurisdiction_code"] + "/" + entity["company"]["company_number"]
                entity_numbers.append(num)
    # for each company number, call the OpenCorp API and collect the info dict
    # that corresponds to that number
    for entity in entity_numbers:
        print("Calling OpenCorp API on: ", entity)
        search_url = "https://api.opencorporates.com/v0.4/companies/" + entity
        response = requests.get(search_url)
        if response.status_code == 200:
            result = json.loads(response.content)
        else:
            print("no response")
        entity_list.append(result["results"]["company"])
    return entity_list
