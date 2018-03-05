#!/usr/bin/env python3
'''
This reads in cpi_data_entities.csv
querys legislator_db by state table
makes and writes a new line to cleaned.csv
'''

import csv
import sqlite3
import pandas as pd

df = pd.read_csv('cpi_data_entities.csv')

SELECT = 'SELECT party FROM '
WHERE = ' WHERE full_name = ?'

def clean_name_state(name_as_list, state):
    name_as_list.reverse()
    name = ' '.join(name_as_list)
    name =  name.replace(',','')
    name = name.title()
    if state == 'in':
        state = 'ind'
    if state == 'or':
        state = 'org'
    return [name], state

def get_party(name, state):
    r = c.execute(SELECT+state+WHERE, name)
    party_list = r.fetchall()
    if not party_list:
        return 'Not in Open States'
    party_val = party_list.pop()[0]
    if party_val == '' or party_val == ' ':
        return 'Not in Open States'
    return party_val

def make_line():
    pass

def write_line():
    pass

if __name__ == "__main__":
    db = sqlite3.connect('legislator_db.sqlite3')
    c = db.cursor()
    for index, row in df.iterrows():
        name,state = clean_name_state(row.lawmaker.split(),row.state.lower())
        party_val = get_party(name, state)
        df.loc[index, 'party'] = party_val 
        print(name[0], '-->', party_val) 
    df.to_csv('test.csv')
