from django.contrib import admin
from .models import Lawmaker, FinancialInterest, OpenCorps 

admin.site.register(FinancialInterest)
admin.site.register(OpenCorps)
admin.site.register(Lawmaker)
