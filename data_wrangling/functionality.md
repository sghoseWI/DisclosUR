# Functionality Map

## Populating the Database

### Overview:
**We will run several thousand queries in order to populate the back-
end Django database with all of the information pertaining to lawmakers and companies.
This will combine the speed of static data with the functionality of dynamic querying - particularly as data changes over time.**

### Output

**A fully populated Django back-end database**

### Process Flow & Steps Needed To Implement
*We may want to highlight dynamic and static functionality at each point - rather than selling this as two separate processes*


*Note: This process repeats for all lawmakers*

1. Developers query specific lawmaker
  * We will want to query this based on the name and district of the lawmaker in the CPI
dataset (rather than an address query like the user form will do)
  * The query will pass the name and address to an OpenStates script

2. The OpenStates script makes a call to an API and returns a packet of information about a lawmakers
  * This information is then stored in a Lawmaker model, as the model's attributes
  * A state model is created and associated with the lawmaker.
  * For the purposes of populating the database, we will not query states that we know do not have business interest information

3. The lawmaker information is passed to a script that queries the CPI database
  * Is the CPI database already loaded into Django? How do we do that?
  * If the CPI database is manually loaded into Django, is it queried through a separate back-end script / app, or in one of the main django container modules?
  * Do we pass the attributes of the specific instance of the lawmaker object we're querying, or in some other form?
  * If the CPI database is pre-loaded, do we need to create lawmaker, industry, state, and corp objects with each query, or can we precreate them based on everything that is in CPI, and just append attributes as we run through the query process?

4. The CPI script returns a packet of information about the lawmaker, their business / employment interests, and the industry of each business / employment interest
  * Business / employment interest objects are created ("corps") and associated with the lawmaker, industry objects are created or updated with associations to the lawmaker and the corps, the lawmaker is updated with new associations / a link to his disclosure URL

5. If at this stage the lawmaker object has certain values for Industry or Business (e.g. "Retired", "Military", "None", etc.) we know there is no information in OpenCorps and we skip the rest of the steps

6. The information packet about the lawmaker and his corps are passed to OpenCorps
  * This is also presumably a separate, back-end script
  * Again, question of passing information as object attributes or in some other form

7. The OpenCorps script returns a packet of information (formatted as JSON dicts, with one dict per result). *Depending on how strictly we filter, each "corp" object will have multiple OpenCorps dicts associated with it, representing all the entities that could probably match the corp listed in the CPI database*
  * The corps objects are updated. Should we have another model, for each OpenCorps results, that are associated with the corps objects and contain the more detailed OpenCorps information?

** End Of Process: Database is fully populated **

## User Queries the Database (static)

### Overview

**This is the main user functionality. The user inputs an address and receives a screen with information about his state lawmaker(s) and their business interets**

### Output

**A page displaying information based on the attributes of the lawmaker(s) queried. Possibly: A visualization. Information relating them to other lawmakers in the state (or country).**

*If the lawmaker is from a non-disclosure state, a page with an explanation and their OpenStates-derived attributes - requires separate template*

*If the lawmaker does not have OpenCorps info, their page will instead contain an explanation of the nature of their business / employment interest - requires separate template*

### Process Flow / Steps to Implement

1. The user enters an address into the form. If the user enters a district or lawmaker name, skip to step no 4.

2. The form sends the address information to a back-end script that queries the Google Maps API and returns usable location information

3. The back-end Google Maps script passes this location information to the back-end OpenStates script, and retrieves the name of the relevant lawmaker(s)

4. The lawmaker(s) name(s) are passed to the pre-populated Django db; all the relevant objects are identified, and their attributes are returned

5. The object attributes are passed to a template and shown to the user  
