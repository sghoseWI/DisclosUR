import django
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "disc_site.settings")
django.setup()
from legislator.models import Lawmaker, FinancialInterest, OpenCorps
import opencorpscraper as oc

all_finterest = FinancialInterest.objects.exclude(made_api_call=True)

for finterest in all_finterest:
    name = finterest.name
    state = finterest.state
    if oc.API_call_counter >= 9800:
        print("We're running out of API calls. Let's call it a day.")
        print("We stopped just before doing this company: ", name)
    company_numbers = oc.get_company_numbers(name, state)
    open_corps_list = oc.get_open_corps(company_numbers)
    finterest.made_api_call = True
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
