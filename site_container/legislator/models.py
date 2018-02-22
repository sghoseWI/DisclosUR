from django.db import models

class Legislator(models.Model):
    """
    Model representing a legislator.
    """
    name = models.CharField(max_length=50)
    corporations = models.ManytoMany(Corps)
    state = models.ForeignKey(State)
    party = models.ForeignKey(Party)

    def __str__(self):
        return self.name , self.state, self.party

class Corps(models.Model):
    """
    Model representing a Corporation.
    Multiple Corps may be tied to multiple Legislator objects.
    """
    name = models.TextField()
    industry = models.ForiegnKey(Industry)

    def __str__(self):
        return self.name

class State(models.Model):
    """
    Model representing a State.
    A State has multiple Legislator objects, (ForeignKey).
    A State has multiple Corps (ManytoMany).
    A State has multiple Industry objects (ManytoMany).
    """
    name = models.CharField(max_length=15)
    abbr = models.CharField(max_length=2)
    industries = models.ManytoMany(Industry)

    def __str__(self):
        return self.abbr

class Industry(models.Model):
    """
    Model representing an Industry.
    An Industry has multiple Corps.
    An Industy has multiple Legislator objects.
    An Industry has multiple States.
    An Industry has multiple Party objects.
    """

class Party(models.Model):
    """
    Model representing a political party.
    A Party has multiple Legislator objects (ForeignKey).
    A Party has multiple Industry objects.
    """
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name
