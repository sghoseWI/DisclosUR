'''
urls file for legislator app
note legislator was set to default
redirect in disc_site.urls
'''

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),

]
