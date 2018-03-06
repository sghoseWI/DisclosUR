#!/usr/bin/env python3
import django
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "disc_site.settings")
django.setup()
from legislator.models import Lawmaker, FinancialInterest 
import pandas as pd

cpi_path = '../data_wrangling/CPI/'
standard = 'cpi_cleaned.csv'
std_df = pd.read_csv(cpi_path+standard,
                      index_col="lawmaker_id",
                      encoding="latin1")

for index, row in std_df.iterrows():
#    check database to see if legislator id exists
    if not Lawmaker.objects.filter(pk=index).exists():
        # create the lawmaker
        lawmaker = Lawmaker.objects.create(name = row["lawmaker"],
            state = row["state"],
            body = row["body"],
            lawmaker_id = index,
            district = row["district"],
            disclosure_url = row["disclosure_report"],
            party = row["party"],
            cpi_2015 = True)
        lawmaker.save()
        print('saving', lawmaker)

    lawmaker = Lawmaker.objects.get(pk=index)
    
    # create FI object  and associate it to the lawmaker
    fi_entity = FinancialInterest.objects.create(name = row["employer_business_interest"],
            industry = row["industry"],
            lawmaker = lawmaker)
    fi_entity.save()
