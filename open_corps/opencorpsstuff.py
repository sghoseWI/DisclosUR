import requests
import json
import urllib
import os

# test code
#legislator_dict = {"lawmaker": state, "businesses": ["biz a", "biz b"],
#"industry": "industry", "disclosure_url": "webpage"}

def open_corporates(legislator_dict):
    company_numbers = corporation_search(legislator_dict)
    if not company_numbers:
        return "No matching results"
    else:
        company_info = get_company_info(company_numbers, legislator_dict)
        return company_info

def corporation_search(legislator_dict):
    '''
    Receives a dict from the legislator database, in which legislator is the key
    and their associated corporate information is the value. Makes a
    GET companies/search call to OpenCorps with the company names and returns
    the IDs of the corresponding companies, if available

    Possibly filters on jurisdiction if too many results (need jurisdiction tag
    in legislator dict)
    '''
    company_numbers = [] # what we eventually feed into get_company_info

    for business in legislator_dict["businesses"]:
        # if business is not "N/A": should actually never happen
            # build the search query
            business = business.replace(" ", "+")
            print(business) # test
            search_url = "https://api.opencorporates.com/v0.4/companies/search?q=" + business
            print(search_url) # test
            # payload = {"?q":business} introduces an extraneous %3F for unknown reasons

            # make the api call
            response = requests.get(search_url) # params=payload
            print(response.url) # test
            if response.status_code == 200:
                result = json.loads(response.content)
            else:
                print("no response")
            # collect all matching company numbers, to be fed into the info search
            # might want to do some additional processing to make sure its a good match
            for company in result["results"]["companies"]:
                print(company["company"]["name"])
                c = company["company"]["jurisdiction_code"] + "/" + company["company"]["company_number"]
                company_numbers.append(c)

    # need to check for empty results, might do some of that above
    return company_numbers

def get_company_info(company_numbers):
    company_list = []
    for company in company_numbers:
        print(company)
        search_url = "https://api.opencorporates.com/v0.4/companies/" + company
        response = requests.get(search_url)
        if response.status_code == 200:
            result = json.loads(response.content)
        else:
            print("no response")
    # figure out this stupid dict organization
        company_list.append(result["results"]["company"])

    #while len(company_list) > 5:
    return company_list

# have a dict of filters and then iterate through each of the filters until
# company list is trimmed to a reasonable length
# maybe a better idea to pump the dynamic query directly to sql, filter there?
# or feed into a dataframe and filter with pandas?
def trim_corps(company_list, filter):
        if len(company_list) > 5:
        trim_corps(company_list)
    else:
        return company_list
