Files in the site_container directory:

db.sqlite3 - The database for Django's backend.

manage.py - Built in program to perform high level operations on a
            website in Django's framework.

disc_site (directory) - Django directory containing settings and URL
                        paths for the main website.

legislator (directory) - Django application - has its own README

populate_from_cpi.py - Programmatically populates db.sqlite3 with
                       lawmaker and financial interest objects. 

repopulate - Flushes db.sqlite3, migrates the models from legislator,
             and runs populate_from_cpi.py

front_end - sap

static - sap

templates - sap

opencorp_officer_query.py - sam

opencorpscraper.py - sam


