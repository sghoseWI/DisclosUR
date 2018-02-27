# Functionality Map

## Single lawmaker Query

*User queries form with address*

*Form passes address to OpenStates API*

*OpenStates API returns lawmaker data; lawmaker model is created/updated, state model is created/updated*

*Lawmaker data is passed to CPI database*

*CPI database returns lawmaker & business data; lawmaker model is updated, Corps model is created/updated, Industry model is updated*

*If CPI returns certain values for Industry / business, OpenCorps is not queried and an explanation screen is shown to the user*

*Lawmaker & business data is passed to OpenCorps*

*OpenCorps returns a list of dictionaries for each business; Corps models are updated*

*Website shows user information from lawmaker, State, Industry, Business model*

## User Visualizes Industries by State

*User asks to look at all industries in a given state*

*Form queries state model, counts up industries, returns visualization*