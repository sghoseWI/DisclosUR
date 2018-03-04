#!/usr/bin/env python3
import django
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "disc_site.settings")
django.setup()
from legislator.models import * #be specific later
import pandas as pd

cpi_file = 'cpi_data_entities.csv'
df = pd.read_csv(cpi_file, index_col = "lawmaker_id", encoding = "ISO-8859-1")

for index, row in df.iterrows():
#    check database to see if legislator id exists
    if not Lawmaker.objects.filter(pk=index).exists():
        # create the lawmaker
        lawmaker = Lawmaker.objects.create(name = row["lawmaker"],
            state = row["state"],
            body = row["body"],
            lawmaker_id = index,
            district = row["district"],
            disclosure_url = row["disclosure_report"],
            cpi_2015 = True)
        lawmaker.save()
        print('saving', lawmaker)
