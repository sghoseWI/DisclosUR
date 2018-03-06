#!/usr/bin/env python3
'''
Nick Tallant

Downloads the bulk csv files from openstates.org

Note our project also dynamically queires their API
for the most updated information. This data is meant to complement 
the CPI dataset from 2015.
'''

import bs4
import re
import requests

html = open('https:_openstates.org_downloads_.html').read()
soup = bs4.BeautifulSoup(html)

def get_csv_links(soup):
    csv_links = []

    for link in soup.find_all('a'):
        link_text = link.get('href')
        if re.search('csv.z', link_text):
            csv_links.append(link_text)

    return csv_links

def download_zips(csv_links):
    for url in csv_links:
        file_name = url[-10:-8] + '.zip'
        r = requests.get(url)
        with open(file_name, "wb") as code:
            code.write(r.content)

if __name__ == "__main__":
    links = get_csv_links(soup)
    download_zips(links)

