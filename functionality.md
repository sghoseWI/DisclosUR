# Functionality Map

## Populating the Database

### Overview:
**We will run several thousand queries in order to populate the back-
end Django database with all of the information pertaining to lawmakers and companies.
After this step is completed, user queries based on the 2015 CPI data-set will not
be sent to APIs; instead, they will query the database locally**

### Output

**A fully populated Django back-end database**

### Process Flow & Steps Needed To Implement

*Note: This process repeats for all lawmakers*

1. Developers query specific lawmaker
..1. We will want to query this based on the name and district of the lawmaker in the CPI
dataset (rather than an address query like the user form will do)
..2. The query will pass the name and address to an OpenStates script

2. The OpenStates script makes a call to an API and returns a packet of information about a lawmakers
..1. This information is then stored in a Lawmaker model, as the model's attributes
..2. A state model is created and associated with the lawmaker (or is it easier to pre-create all the State models?)
..3. For the purposes of populating the database, we will not query states that we know do not have business interest information

3. The lawmaker information is passed to a script that queries the CPI database
..1. Is the CPI database already loaded into Django? How do we do that?
..2. If the CPI database is manually loaded into Django, is it queried through a separate back-end script / app, or in one of the main django container modules?
..3. Do we pass the attributes of the specific instance of the lawmaker object we're querying, or in some other form?
..4. If the CPI database is pre-loaded, do we need to create lawmaker, industry, state, and corp objects with each query, or can we precreate them based on everything that is in CPI, and just append attributes as we run through the query process?

4. The CPI script returns a packet of information about the lawmaker, their business / employment interests, and the industry of each business / employment interest
..1. Business / employment interest objects are created ("corps") and associated with the lawmaker, industry objects are created or updated with associations to the lawmaker and the corps, the lawmaker is updated with new associations / a link to his disclosure URL

5. If at this stage the lawmaker object has certain values for Industry or Business (e.g. "Retired", "Military", "None", etc.) we know there is no information in OpenCorps and we skip the rest of the steps

6. The information packet about the lawmaker and his corps are passed to OpenCorps

*Lawmaker & business data is passed to OpenCorps*

*OpenCorps returns a list of dictionaries for each business; Corps models are updated*

*Website shows user information from lawmaker, State, Industry, Business model*

## User Visualizes Industries by State

*User asks to look at all industries in a given state*

*Form queries state model, counts up industries, returns visualization*
