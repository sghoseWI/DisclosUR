#!/usr/bin/env python3
'''
This reads in the original CPI csvs,
querys the legislator_db by state table, and
creates two csv files with cleaned data - ex:
names no longer UPPERCASE, null values, etc.
'''

import csv
import sqlite3
import pandas as pd

standard_df = pd.read_csv('cpi_std_unclean.csv',encoding='latin1')
nonstandard_df = pd.read_csv('cpi_nonstd_unclean.csv',encoding='latin1')
SELECT = 'SELECT party FROM '
WHERE = ' WHERE full_name = ?'

def clean_name_state(name_as_list, state):
    '''
    Prepares input for the get_party function.

    Input: name_as_list (list), state (string)
        Name of the legislator as a list from the
        original CPI data. State as a 2 character string.

    Output: [name] (list), state (string)
        Legislator name as ['First Last'] to be used in a query of
        the sqlite3 db of open states data. State as a string,
        correcting for 'in' and 'or', which can't be table names.
    '''
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
    '''
    Finds political party of legislator from open states.

    Input: name (list of a single string), state (string)

    Return: party_val (string)
    '''
    r = c.execute(SELECT+state+WHERE, name)
    party_list = r.fetchall()
    if not party_list:
        return 'Not in Open States'
    party_val = party_list.pop()[0]
    if party_val == '' or party_val == ' ':
        return 'Not in Open States'
    return party_val

def clean_df(df, c):
    '''

    '''
    for index, row in df.iterrows():
        name,state = clean_name_state(row.lawmaker.split(),row.state.lower())
        party_val = get_party(name, state)
        df.loc[index, 'party'] = party_val 
        df.loc[index, 'lawmaker'] = name[0]
        print(name[0], '-->', party_val) 
    
if __name__ == "__main__":
    db = sqlite3.connect('../open_states/legislator_db.sqlite3')
    c = db.cursor()
    clean_df(standard_df, c)
    clean_df(nonstandard_df, c)
    standard_df.to_csv('cpi_cleaned.csv')
    nonstandard_df.to_csv('cpi_nonstd_cleaned.csv')
