#!/usr/bin/env python3
'''
Extracts the legislator csv from every zip file
in this directory.
'''

import zipfile
import os
import re

def get_legislator_csv(filename):
    print("unzipping", filename)
    zfile = zipfile.ZipFile(filename)
    for cfile in zfile.namelist():
        if re.search('legislators.csv',cfile):
            zfile.extract(cfile, './legislator_csvs')

if __name__ == "__main__":
    for f in os.listdir('./zips'):
         filename = os.fsdecode(f)
         if filename.endswith(".zip"):
            get_legislator_csv('./zips/'+ filename) 

