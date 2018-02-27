from django.db import models

class Industry(models.Model):
    """
    Model representing an Industry.
    An Industry has multiple Corps.
    An Industy has multiple Lawmaker objects.
    An Industry has multiple States.
    An Industry has multiple Party objects.
    """
    name = models.CharField(max_length=25)

class Party(models.Model):
    """
    Model representing a political party.
    A Party has multiple Lawmaker objects (ForeignKey).
    A Party has multiple Industry objects.
    """
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Corps(models.Model):
    """
    Model representing a Corporation.
    Multiple Corps may be tied To multiple Lawmaker objects.
    """
    name = models.TextField()
    industry = models.ForeignKey(Industry, on_delete=models.CASCADE)
    lawmaker = models.ManyToManyField(Lawmaker, verbose_name =
        "lawmakers with an interest in this entity", on_delete=models.CASCADE)

    # corresponding to OpenCorporates attributes
    jurisdiction_code = models.SlugField()
    current_status = models.SlugField()
    company_type = models.CharField()
    incorporation_date = models.DateField()
    opencorporates_url = models.URLField()
    alternative_names = models.TextField() #OpenCorp returns an array
    registered_address_in_full = models.TextField()
    registry_url = models.URLField()
    company_number = models.CharField() # may not be strictly a number
    controlling_entity = models.TextField()
    ultimate_beneficial_owners = models.TextField()
    officers = models.TextField() # OpenCorps returns a list of dicts. Might be
        # better to implement this as a separate model

    def __str__(self):
        return self.name

class State(models.Model):
    """
    Model representing a State.
    A State has multiple Lawmaker objects, (ForeignKey).
    A State has multiple Corps (ManyToManyField).
    A State has multiple Industry objects (ManyToManyField).
    """
    name = models.CharField(max_length=15)
    abbr = models.CharField(max_length=2)
    industries = models.ManyToManyField(Industry)

    def __str__(self):
        return self.abbr

class Lawmaker(models.Model):
    """
    Model representing a legislaTor.
    """
    name = models.CharField(max_length=50)
    corps = models.ManyToManyField(Corps, verbose_name="list of corporations")
    state = models.ForeignKey(State,
                              verbose_name="the lawmaker's state",
                              on_delete=models.CASCADE)
    party = models.ForeignKey(Party, on_delete=models.CASCADE)

    def __str__(self):
        return "{},{},{}".format(self.name , self.state, self.party)
