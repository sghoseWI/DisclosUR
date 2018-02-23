from django.db import models

class CpiRecord(models.Model):
    """
    Model representing the CPI data set .
    """
    cpi_id = models.CharField(max_length=10, ) 
    lawmaker_id = models.CharField(max_length=10) 
    lawmaker = models.CharField(max_length=50)
    corps = models.ManyToManyField('Corps', verbose_name="list of corporations")
    state = models.ForeignKey(State, verbose_name="the lawmaker's state")
    party = models.ForeignKey(Party)

    def __str__(self):
        return self.name , self.state, self.party

