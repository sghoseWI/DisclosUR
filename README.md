DisclosUR
=========

Financial disclosure at the state level and its relation to corporate entities.

## Contributors

[Nick Tallant](https://github.com/ndtallant) | [Saptarshi Ghose](https://github.com/saptarshighose) |  [Sam Gallicchio](https://github.com/SRGallicchio)

## Installation
To install dependent packages by running:

```
pip3 install -r requirements.txt
```

from the top level directory - we recommend using a virtual environment.

## Explanation of code
Generated from scratch:

Modified code: 
Incorporated Django Tables2 to build tables within our Django templates. 

## Required Modules

* [pyopenstates](http://docs.openstates.org/projects/pyopenstates/en/latest/pyopenstates%20module.html)
* [requests](http://docs.python-requests.org/en/master/)
* [json](https://docs.python.org/3/library/json.html)
* [python-dotenv](https://github.com/theskumar/python-dotenv)
* [re](https://docs.python.org/3/library/re.html)
* [django](https://www.djangoproject.com/)
* [django-tables2](put link here)
* [sqlite3](https://docs.python.org/3/library/sqlite3.html)
* [pandas](https://pandas.pydata.org/)
* [tableau] (https://onlinehelp.tableau.com/current/pro/desktop/en-us/embed.html)

## Data Sources & APIs

### Open States
An organization and suite of tools to collect data on bills, legislators, committees, and events. We interacted with this data using the python API listed above, and through using [their website](https://openstates.org/).

### Center for Public Integrity
Data-driven independent reporting since 1989. CPI  believes "in the democratic process and seek transparency, accountability and efficiency in our government."

## Data Visualization
Made connections to CPI data source and created dynamic data visualizations using Tableau.  Hosted dynamic data visualizations on Tableau's public server (see here: https://public.tableau.com/profile/saptarshi.ghose#!/vizhome/CPIDataViz/Dashboard1 and here: https://public.tableau.com/profile/saptarshi.ghose#!/vizhome/cs_map_final/Sheet1) and used HTML embedding to incorporate data visualizations into our website.  

## Project Responsibilities
Worked on Together: Django views/models, cleaning data, building database ADD

Nick:  ADD

Saptarshi: Dynamic data visualizations, bootstrap, html and css, Django templates and static files for views. ADD

Sam: OpenCorps web scraper,  ADD 

Contribute
---------

- Issue Tracker: https://github.com/ndtallant/DisclosUR/issues
- Source Code: https://github.com/ndtallant/DisclosUR
