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

opencorp_officer_query.py - Contains one function for searching the OpenCorporates Officer API by legislator name. 
	Intended to be incorporated into Django application, but ultimately was not due to 
	difficulties in rendering the output in a comprehensible way. Can be used independently of the web app in 
	IPython3 by passing the function a legislator name (does not need to be exact) and two-letter state code (e.g. "IL")) 

opencorpscraper.py - Calls the OpenCorporates API and collects information to be passed to populate_open_corps.

populate_open_corps.py - Programmatically populates db.sqlite3 with OpenCorp objects based on the financial interest objects
	present in the database.


