Files in the CPI directory:

clean_cpi.py - Reads CPI data sets:
                    cpi_std_unclean.csv
                    cpi_nonstd_unclean.csv

               And creates:
                    cpi_cleaned.csv
                    cpi_nonstd_cleaned.csv

               The nonstandard csv files contain CPI records
               that met the criteria in 'standard_entities.txt'

standard_entities.txt - Sam if you could explain this that would be dope 

cpi.db - Queried by all_cpi.py in an earlier implementation of our
         project. Kept here for future versions! 

all_cpi.py - An early attempt to mass populate the 
             django database using a sqlite3 database of 
             the CPI dataset. We ended up using csvs with
             the final implementation of our project.


