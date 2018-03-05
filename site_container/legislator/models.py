from django.db import models

class Lawmaker(models.Model):
    """
    Model representing a legislaTor.
    """
    name = models.CharField(max_length=50)
    party = models.CharField(max_length=50, null = True) # allows null for values added later by OpenStates
    state = models.CharField(max_length=2)
    body = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    disclosure_url = models.URLField(null = True)
    lawmaker_id = models.IntegerField(primary_key = True)
    cpi_2015 = models.BooleanField(default=False)
    non_standard_FI = models.TextField(default='')
    non_standard_IN = models.TextField(default='')

    def __str__(self):
        return self.name

class FinancialInterest(models.Model):
    """
    Model representing an employer or business interest.
    """
    name = models.TextField()
    industry = models.TextField()
    lawmaker = models.ForeignKey(Lawmaker, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class OpenCorps(models.Model):
    """
    Model representing an OpenCorporates entry for a given financial interest.
    """
    name = models.TextField()
    company_number = models.CharField(max_length = 25)
    company_type = models.CharField(max_length = 25, null=True)
    incorporation_date = models.CharField(max_length = 25, null = True)
    opencorporates_url = models.URLField(null = True)
    alternative_names = models.TextField(null = True)
    registered_address_in_full	= models.TextField(null=True)
    registry_url = models.URLField(null = True)
    ultimate_beneficial_owners = models.TextField(null = True)
    finterest = models.ForeignKey(FinancialInterest,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
