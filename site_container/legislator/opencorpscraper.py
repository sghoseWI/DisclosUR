import requests
import json
import urllib
from django.db import models
from dotenv import get_key, find_dotenv
from legislator.models import Lawmaker, FinancialInterest, OpenCorps

open_corp_key = get_key(find_dotenv(), "OPEN_CORP_KEY")
open_corp_key = "api_token=" + open_corp_key

def get_company_numbers(name, state):
    '''
    for each business / employer interest listed by a legislator, call the
    OpenCorp search API, filtering out results whose incorporation post-dates
    the CPI dataset
    '''
    juris_code = "us_" + state.lower()
    company_numbers = []
    company_name = name.replace(" ", "+")
    incorp_filter = "&incorporation\date=:2016-01-01"
    s = company_name + incorp_filter + "&" + open_corp_key
    search_url = "https://api.opencorporates.com/v0.4/companies/search?q=" + s
    response = requests.get(search_url)
    # collect company numbers that may match the business / employer interest
    if response.status_code == 200:
        result = json.loads(response.content)
        for entity in result["results"]["companies"]:
            # if there are multiple name matches, filter on state / status
            if len(result["results"]["companies"]) > 1 and entity["company"]["jurisdiction_code"] != juris_code:
                pass
            elif len(result["results"]["companies"]) > 1 and entity["company"]["inactive"]:
                pass
            else:
                num = entity["company"]["jurisdiction_code"] + "/" + entity["company"]["company_number"]
                company_numbers.append(num)
    elif response.status_code == 401:
        print("Token Incorrect")
    else:
        print("Status code error #: ", response.status_code) # for debugging
    return company_numbers

def get_open_corps(company_numbers):
    '''
    Calls OpenCorp API for each call number and collects
    the metadata that corresponds to that number.
    '''
    company_list = []
    if company_numbers is None:
        pass
    else:
        for number in company_numbers:
            s = number + "?" + open_corp_key
            search_url = "https://api.opencorporates.com/v0.4/companies/" + s
            response = requests.get(search_url)
            if response.status_code == 200:
                result = json.loads(response.content)
                company_list.append(result["results"]["company"])
            else:
                print("Status code error", response.status_code)
    return company_list
