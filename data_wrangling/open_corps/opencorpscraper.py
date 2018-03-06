import requests
import json
import urllib
import pandas as pd
from dotenv import get_key

#open_corp_key = get_key.find_dotenv(), "OPEN_CORP_KEY")

def corp_scraper(cpi_file):
    leg_dicts = get_leg_dicts(cpi_file, row_index_start, row_index_stop, False)
    for key in leg_dicts:
        leg = leg_dicts[key]
        for entry in leg["employer_business_interest"]:
            for interest, open_corps in entry.items():
                    open_corps.extend(get_entity_info(leg))

def get_leg_dicts(cpi_file, row_index_start, row_index_stop, partial=False):
    '''Takes the CPI csv file and scrapes the OpenCorps API. Builds a dictionary
    of each unique legislator, where the key-value pairs are the information from
    the CPI csv file. The employer / business interest field becomes a list of
    dictionaries, with each dictionary key corresponding to an employer or
    business interest; the dictionary's values will ultimately be a list of
    OpenCorps dictionaries corresponding to companies potentially matching that
    employer / business interest.

    Use the parameters to configure the portion of
    the dataset we want to search, to manage number of API calls. '''

    df = pd.read_csv(cpi_file, index_col = "lawmaker_id", encoding = "ISO-8859-1")
    if partial:
        df = df.iloc[row_index_start:row_index_stop]
    df2 = df.to_dict("index")
    for key in df2:
        df2[key]["employer_business_interest"] = []
        #df2[key]["employer_business_interest"] = [{df2[key]["employer_business_interest"]:[]}]
        df2[key]["industry"] = [df2[key]["industry"]]
    for index, row in df.iterrows():
        if {row["employer_business_interest"]} not in df2[index]["employer_business_interest"]:
            df2[index]["employer_business_interest"].append({row["employer_business_interest"]:[]})
        if row["industry"] not in df2[index]["industry"]:
            df2[index]["industry"].append(row["industry"])
    return df2

def get_entity_info(leg_dict):
    ''' Takes a dictionary consisting of a legislator, their state, and their
    listed business / employer interests, and scrapes the OpenCorp API for
    entities matching their business / employer interests. Returns a list of
    OpenCorp results dictionaries for entities that may match the employer / business interest. '''
    leg_juris_code = "us_" + leg_dict["state"].lower()
    entity_numbers = []
    entity_list = []
    # for each business / employer interest listed by a legislator, call the
    # OpenCorp search API, filtering out results whose incorporation post-dates
    # the CPI dataset
    for i in leg_dict["employer_business_interest"]:
        for entry in i:
            print("Searching OpenCorp API for: ", entry)
            entry = entry.replace(" ", "+")
            incorp_filter = "&incorporation\date=:2016-01-01"
            search_url = "https://api.opencorporates.com/v0.4/companies/search?q=" + entry + incorp_filter
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
                if len(result["results"]["companies"]) > 5 and entity["company"]["jurisdiction_code"] != leg_juris_code:
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
