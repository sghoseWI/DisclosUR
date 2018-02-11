#Disclousur$ Group Project
#Computer Science with Applications 2
#Inserting CPI data into SQLite database

import csv, sqlite3

connection = sqlite3.connect(":memory:")
cur = connection.cursor()
cur.execute("CREATE TABLE t (cpi_id, lawmaker_id, lawmaker, state, \
body, district,	employer_business_interest,	industry, disclosure_report);")
#column names to be inserted ^

with open('CPI_data.csv','rb') as fin:
    # csv.DictReader uses first line in file for column headings by default
    dr = csv.DictReader(fin) # comma as delimiter
    to_db = [(i['cpi_id'], i['lawmaker_id'],i['lawmaker'], i['state'], \
    i['body'], i['district'],i['employer_business_interest'], i['industry'], \
    i['disclosure_report'])
    for i in dr]

cur.executemany("INSERT INTO t (cpi_id, lawmaker_id, lawmaker, state, \
body, district,	employer_business_interest,	industry, disclosure_report) \
VALUES (?, ?);", to_db)
connection.commit()
connection.close()
