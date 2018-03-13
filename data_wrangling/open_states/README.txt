Files in the open_states directory:

legislator_db.sqlite3 - Database of all legislators in open states'
                        2017 dataset. The data came from zip files
                        scraped from their website using the files
                        in the collection directory.

collection (directory)-
    db_maker - bash script that creates the file 'import.sql'
               should be run from the legislator_csvs directory

    scraper.py - saves all of the bulk data from open states 
                 using bs4

    extractor.py- extracts the csv file of interest from each of the
                  50 zip files corresponding to a different state

    https:_openstates.org_downloads_.html - Page with download links

legislator_csvs (directory) - Contains csv files for each state 
                              created by extractor.py

zips (directory) - Contains zip files collected by scraper.py

