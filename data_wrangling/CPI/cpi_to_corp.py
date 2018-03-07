'''
This file connects the dots between CPI and Open Corporates,
and returns a tuple of metadata to be saved in Lawmaker objects 
from models.py
'''

import all_cpi
import opencorpscraper

cpi_data = all_cpi.get_cpi_tuples()

def get_lawmaker_attr(record):
    '''
    As we loop through cpi data, call this function,
    it will return attr to save in a Lawmaker model through
    django API.
    '''
    lawmaker, state, district, body, corp, industry = all_cpi.clean_record(record)

    open_corp_data = oc_helper(lawmaker, state, corp)

    #parse data to what we need or do that in helper?

    return open_corp_data

def oc_helper(lawmaker, state, corp):
    num = opencorpscraper.get_company_numbers(lawmaker, state, corp)
    return opencorpscraper.get_open_corps(num)

