Files in the CPI directory:

clean_cpi.py - Reads CPI data sets:
                    cpi_std_unclean.csv
                    cpi_nonstd_unclean.csv

               And creates:
                    cpi_cleaned.csv
                    cpi_nonstd_cleaned.csv

               The nonstandard csv files contain CPI records
               that met the criteria in 'standard_entities.txt'

standard_entities.txt - Describes criteria for excluding rows from the cpi_std datasets.
	In order to limit the number of unnecessary API calls and the time spent populating
	the Django database, lawmakers whose financial interests were definitely not represented
	in OpenCorporates were excluded (typically because they had none, their financial interests
	were not in entities likely to be in OpenCorps e.g. the military or municipal bodies, or
	they described their financial interests without using a searchable entity name, e.g.
	generically stating 'farmland' or 'rental income'). These lawmakers are still represented
	in the database, they just aren't fed to the OpenCorporates scraper.

cpi.db - Queried by all_cpi.py in an earlier implementation of our
         project. Kept here for future versions! 

all_cpi.py - An early attempt to mass populate the 
             django database using a sqlite3 database of 
             the CPI dataset. We ended up using csvs with
             the final implementation of our project.


