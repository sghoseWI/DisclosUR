DisclosUR
=========

Financial disclosures for US legislators at the state level and their relation to corporate entities.

## Contributors

[Nick Tallant](https://github.com/ndtallant) | [Saptarshi Ghose](https://github.com/saptarshighose) |  [Sam Gallicchio](https://github.com/SRGallicchio)

## Installation
Install dependent packages by running:

```
pip3 install -r requirements.txt
```

from the top level directory - we recommend using a virtual environment. To populate the database, please see 'Populating the database' under 'Usage'.

## Required Modules

* [pyopenstates](http://docs.openstates.org/projects/pyopenstates/en/latest/pyopenstates%20module.html)
* [requests](http://docs.python-requests.org/en/master/)
* [json](https://docs.python.org/3/library/json.html)
* [python-dotenv](https://github.com/theskumar/python-dotenv)
* [re](https://docs.python.org/3/library/re.html)
* [django](https://www.djangoproject.com/)
* [django-tables2](http://django-tables2.readthedocs.io/en/latest/)
* [sqlite3](https://docs.python.org/3/library/sqlite3.html)
* [pandas](https://pandas.pydata.org/)
* [tableau](https://onlinehelp.tableau.com/current/pro/desktop/en-us/embed.html)

## Data Sources & APIs

### Open States
An organization and suite of tools to collect data on bills, legislators, committees, and events. We interacted with this data using the python API listed above, and through using [their website](https://openstates.org/).

### Center for Public Integrity (CPI)
Data-driven independent reporting since 1989. CPI  believes "in the democratic process and seek transparency, accountability and efficiency in our government." Data for this project comes from their Conflicted Interests project:
https://github.com/PublicI/state-lawmakers-disclosures

### Open Corporates
The largest open database on companies in the world. Their goal is to "make information on companies more usable and more widely available for the public benefit, particularly to tackle the use of companies for criminal or anti-social purposes, for example corruption, money laundering and organised crime". Their information is sourced from publicly available official company registries.

Documentation for the API:
https://api.opencorporates.com/documentation/API-Reference

## Project / Data Limitations

## Data Visualization
Made connections to CPI data source and created dynamic data visualizations using Tableau.  Hosted dynamic data visualizations on Tableau's public server [here](https://public.tableau.com/profile/saptarshi.ghose#!/vizhome/CPIDataViz/Dashboard1) and [here](https://public.tableau.com/profile/saptarshi.ghose#!/vizhome/cs_map_final/Sheet1) and used HTML embedding to incorporate data visualizations into our website.  

## Usage

### Populating the database
If you have a demo of this project on a flashdrive, this is unnecessary.

Have a file `.env`, in the `site_container` directory with the google maps, open states, and open corporates API keys. (The local demo on a flash drive has this already).

In the `site_container` directory, run `repopulate`. This will reset the django database with lawmakers pandas financial interests. It should take about 2 minutes to run.

Run `populate_open_corps.py`. This may take some time depending on the internet connection.

### Using the website
Users can query our database through the home page in four separate ways:

1) Enter your home address

2) Enter your state

3) Enter your state and legislative district

4) Enter the name of your state legislator.  

After entering information into the web form and submitting, users will see information about the state legislators relevant to their query.  They will also see links, if available, to the financial disclosure forms filed by their state legislators.  If available, users will also see relevant information about the corporations compensating those state legislators.

A separate feature of the site is the "explore your data" link on the home page.  When users click this link, they are taken to a page with dynamic data visualizations of the major business industries compensating state legislors -- filterable by state, legislative district, and legislative body.  The top visualization is a bubble chart in which each bubble represents an industry and the size is a factor of count of industries compensating state legislators (dynamic to the filter).  The bottom visualization is a color differentiated map of the United States showing the biggest industries by state that are compensating state legislators.   In each of these visualizations, users can hover over a part of the chart/map and export the underlying filtered data.  

Contribute
---------

- Issue Tracker: https://github.com/ndtallant/DisclosUR/issues
- Source Code: https://github.com/ndtallant/DisclosUR

## Project Responsibilities
Worked on Together:
* Creating classes found in models.py, used in the main database.
* Cleaning the CPI dataset
* Integrating the separate components of the project.

Nick:
* Obtained Open States data through a script accessing their API, as well as obtaining/cleaning their bulk data.
* Implemented the original django framework, and maintained the versions of the back-end throughout the project (migrating model changes, etc).
* Connected views and urls to Saptarshi's work on the front end.
* Implemented the final version of CPI data.

Saptarshi: Django templates and static files for views, django tables, dynamic data visualizations, bootstrap, html and css.

Sam: OpenCorporates scrapers and database population script. OpenCorps officer query function (houesd in opencorp_officer_query.py; intended to be incorporated into Django application, but ultimately was not due to difficulties in rendering the output in a comprehensible way. Can be used independently of the web app in IPython3 by passing the function a legislator name (does not need to be exact) and two-letter state code (e.g. "IL")). All OpenCorp-related code is original work.
