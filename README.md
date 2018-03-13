DisclosUR
=========

Financial disclosure for legislators at the state level and its relation to corporate entities.

## Contributors

[Nick Tallant](https://github.com/ndtallant) | [Saptarshi Ghose](https://github.com/saptarshighose) |  [Sam Gallicchio](https://github.com/SRGallicchio)

## Installation
To install dependent packages by running:

```
pip3 install -r requirements.txt
```

from the top level directory - we recommend using a virtual environment.

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
Data-driven independent reporting since 1989. CPI  believes "in the democratic process and seek transparency, accountability and efficiency in our government."

### Open Corporates
The largest open database on companies in the world.  Their goal is to "make information on companies more usable and more widely available for the public benefit, particularly to tackle the use of companies for criminal or anti-social purposes, for example corruption, money laundering and organised crime"

## Data Visualization
Made connections to CPI data source and created dynamic data visualizations using Tableau.  Hosted dynamic data visualizations on Tableau's public server [here](https://public.tableau.com/profile/saptarshi.ghose#!/vizhome/CPIDataViz/Dashboard1) and [here](https://public.tableau.com/profile/saptarshi.ghose#!/vizhome/cs_map_final/Sheet1) and used HTML embedding to incorporate data visualizations into our website.  

## Usage

### Populating the database

### Using the website
Users can query our database through the home page in four separate ways: 1) Enter your home address 2) Enter your state 3) Enter your state and legislative district 4) Enter the name of your state legislator.  After entering location information into the web form in one of those ways and clicking submit, users will see information about the state legislators that represent their location.  They will also see links, if available, to the public financial disclosure forms filed by their state legislators.  If available, users will also see information about the corporations compensating those state legislators -- as revealed by the CPI data. 

A separate feature of the site is the "explore your data" link on the home page.  When users click this link, they are taken to a page with dynamic data visualizations of the major business industries compensating state legislors -- filterable by state, legislative district, and legislative body.  The top visualization is a bubble chart in which each bubble represents an industry and the size is a factor of count of industries compensating state legislators (dynamic to the filter).  The bottom visualization is a color differentiated map of the United States showing the biggest industries by state that are compensating state legislators.   In each of these visualizations, users can hover over a part of the chart/map and export the underlying fitlered data.  

Contribute
---------

- Issue Tracker: https://github.com/ndtallant/DisclosUR/issues
- Source Code: https://github.com/ndtallant/DisclosUR

## Project Responsibilities
Worked on Together: Django views/models, cleaning data, building database ADD

Nick:

Saptarshi: Django templates and static files for views, django tables, dynamic data visualizations, bootstrap, html and css.

Sam: OpenCorps web scraper,  ADD
