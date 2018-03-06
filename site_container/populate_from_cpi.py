#!/usr/bin/env python3
import django
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "disc_site.settings")
django.setup()
from legislator.models import Lawmaker, FinancialInterest 
import pandas as pd

cpi_path = '../data_wrangling/CPI/'
standard = 'cpi_cleaned.csv'
std_df = pd.read_csv(cpi_path + standard,
                      index_col="lawmaker_id",
                      encoding="latin1")
non_std = 'cpi_nonstd_cleaned.csv'
non_std_df = pd.read_csv(cpi_path + non_std,
                      index_col="lawmaker_id",
                      encoding="latin1")

def create_fi(row, lawmaker): 
    '''
    Create FI object and associate it to the lawmaker
    '''
    fi_ob = FinancialInterest(name=row.employer_business_interest,
                              industry=row.industry,
                              lawmaker=lawmaker)
    fi_ob.save()
 

def create_lm(index, row, non_standard):
    '''
    Checks to see if LM already exists, creates one if it does not.
    Has 'non_standard' attributes if nonstandard = True.
    Creates FI object tied to LM either way.
    '''
    if not Lawmaker.objects.filter(pk=index).exists():
        lawmaker = Lawmaker(name=row.lawmaker,
                            state=row.state,
                            body=row.body,
                            lawmaker_id=index,
                            district=row.district,
                            disclosure_url=row.disclosure_report,
                            party=row.party,
                            cpi_2015=True)
        if non_standard:
            lawmaker.non_standard_FI = row.employer_business_interest
            lawmaker.non_standard_IF = row.industry
        lawmaker.save()
        print('saving', lawmaker)

    lawmaker = Lawmaker.objects.get(pk=index)
    create_fi(row, lawmaker)
def pop_from_df(df, non_standard):
    '''
    Takes in a dataframe, creates appropriate objects.
    '''
    for index, row in df.iterrows():
       create_lm(index, row, non_standard)

if __name__ == "__main__":
    pop_from_df(std_df, False)
    pop_from_df(non_std_df, True)



