Files in the legislator directory:

admin.py - Built in Django file where each class in models.py
           must be registered.

apps.py - Built in Django file that configures this application
          (legislator) at a high level.

forms.py - Contains the data form used for the home page.

migrations - Built in Django directory to handle high level
             operations of the models.

models.py - Contains the classes used to create objects in the 
            Django db.

tests.py - Built in Django file (not used currently).

urls.py - Contains the URL paths for returning pages connected
          to user searches.

views.py - Contains the functions/logic for using the website. 
           Takes in the data from a user request and redirects
           to an appropriate page (using urls.py).
