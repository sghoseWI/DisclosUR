#Disclousur$ Group Project
#Computer Science with Applications 2
#Join legislator retrieved from location search with CPI data

import pandas as pd
import csv
import sqlite3

# Create a SQL connection to our SQLite database
con = sqlite3.connect("data/portal_mammals.sqlite") #change to Nick's sqlite path

cur = con.cursor()

# Return all results of query
cur.execute('SELECT legislator FROM CPI_data left join  \
WHERE ')
cur.fetchall()

def join_leg_bus(csv):
    for legislator in CPI_data[]
