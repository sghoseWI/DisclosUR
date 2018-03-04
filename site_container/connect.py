#!/usr/bin/env python3
import django
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "disc_site.settings")
django.setup()
from legislator.models import * #be specific later

import all_cpi

L = all_cpi.get_cpi_tuples()

for record in L:
    lawmaker, state, district, body, corp_name, industry = all_cpi.clean_record(record)

    indu_ob = Industry(name=industry)
    indu_ob.save()
    state_ob = State(name=state, abbr=state)
    state_ob.save()
    corp_ob, _ = Corps.objects.get_or_create(name=corp_name, industry=indu_ob, defaults=None)
    corp_ob.save()
    lm_ob, made_new_guy = Lawmaker.objects.get_or_create(name = lawmaker, district=district, body=body,
                    state=state_ob, cpi_15=True)
    lm_ob.save()
    lm_ob.corps.add(corp_ob)
    lm_ob.save()
    if made_new_guy:
        print('saving', lawmaker)

    #model.objects. get or create?
