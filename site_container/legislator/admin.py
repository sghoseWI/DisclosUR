from django.contrib import admin

from .models import Industry, Party, Corps, State, Lawmaker 

admin.site.register(Industry)
admin.site.register(Party)
admin.site.register(Corps)
admin.site.register(State)
admin.site.register(Lawmaker)
