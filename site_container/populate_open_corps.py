import django
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "disc_site.settings")
django.setup()
from legislator.models import Lawmaker, FinancialInterest, OpenCorps
import opencorpscraper as oc

'''
Populates the Django database with OpenCorps objects. Every OpenCorp object is
a collection of information, sourced from OpenCorporates, about an entity that
is likely to match an entity that a given legislator may have a financial
interest in (a 'finterest' object). t.

For each finterest object, calls the OpenCorps API scraper functions, and creates
an OpenCorps object from each entity in the OpenCorporates database that is
returned by the scraper. There may be more than one positive name
match in the OpenCorporates database for a given finterest. Updates the
finterest object to note that it has been passed to OpenCorps (this allows the
population process to be stopped and started, in case the number of daily API
calls we are allotted isn't sufficient to populate the database in one pass).
'''

all_finterest = FinancialInterest.objects.exclude(made_API_call=True)

for finterest in all_finterest:
    name = finterest.name
    state = finterest.state
    company_numbers = oc.get_company_numbers(name, state)
    open_corps_list = oc.get_open_corps(company_numbers)
    finterest.made_API_call = True
    finterest.save()
    for entry in open_corps_list:
        officer_list = ''
        for officer in entry['officers']:
            officer_name = officer['officer']['name']
            officer_position = officer['officer']['position']
            if officer_name is None or officer_position is None:
                pass
            else:
                officer_list += '* Officer: ' + officer_name + ' Position: ' + officer_position + ' *'
        open_corp = OpenCorps.objects.create(name = entry['name'],
            company_number = entry['company_number'],
            company_type = entry['company_type'],
            incorporation_date = entry['incorporation_date'],
            opencorporates_url = entry['opencorporates_url'],
            alternative_names = entry['alternative_names'],
            registered_address_in_full	= entry['registered_address_in_full'],
            registry_url = entry['registry_url'],
            ultimate_beneficial_owners = entry['ultimate_beneficial_owners'],
            inactive = entry['inactive'],
            officers = officer_list,
            status = entry['current_status'],
            finterest = finterest)
        print('Saving -->', entry['name'])
