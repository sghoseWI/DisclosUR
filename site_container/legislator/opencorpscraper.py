import requests
import json
import urllib
from django.db import models
from dotenv import get_key, find_dotenv
from .models import Lawmaker, FinancialInterest, OpenCorps


open_corp_key = get_key(find_dotenv(), "OPEN_CORP_KEY")
API_call_counter = 0

def get_company_numbers(name, state):
    # for each business / employer interest listed by a legislator, call the
    # OpenCorp search API, filtering out results whose incorporation post-dates
    # the CPI dataset
    juris_code = "us_" + state.lower()
    company_numbers = []
    # print("Searching OpenCorp API for: ", corp_name)
    company_name = name.replace(" ", "+")
    incorp_filter = "&incorporation\date=:2016-01-01"
    search_url = "https://api.opencorporates.com/v0.4/companies/search?q=" + company_name + incorp_filter + "&" + open_corp_key
    print(search_url)
    response = requests.get(search_url)
    #API_call_counter += 1
    if response.status_code == 200:
        result = json.loads(response.content)
        for entity in result["results"]["companies"]:
            print("Considering ", entity["company"]["name"])
            # if there are a lot of results, filter on the state; might want to filter
            # on status too
            if len(result["results"]["companies"]) > 1 and entity["company"]["jurisdiction_code"] != juris_code:
                print("Passing on", entity["company"]["name"], "because its jurisdiction code is ", entity["company"]["jurisdiction_code"], "not ", juris_code)
                pass
            elif len(result["results"]["companies"]) > 1 and entity["company"]["inactive"]:
                print("Passing on", entity["company"]["name"], "because it is inactive")
            else:
                num = entity["company"]["jurisdiction_code"] + "/" + entity["company"]["company_number"]
                company_numbers.append(num)
    elif response.status_code == 401:
        print("Token incorrect")
    else:
        print("Status code error #: ", response.status_code) # test code if we're out of calls
    # collect all company numbers that may match the business / employer interest
        return company_numbers

def get_open_corps(company_numbers):
    company_list = []
    # for each company number, call the OpenCorp API and collect the info dict
    # that corresponds to that number
    if company_numbers is None:
        pass
    else:
        for number in company_numbers:
            print("Calling OpenCorp API on: ", number)
            search_url = "https://api.opencorporates.com/v0.4/companies/" + number + "?" + open_corp_key
            print(search_url)
            response = requests.get(search_url)
            #API_call_counter += 1
            if response.status_code == 200:
                result = json.loads(response.content)
                company_list.append(result["results"]["company"])
            else:
                print("no response!", response.status_code)
    return company_list
