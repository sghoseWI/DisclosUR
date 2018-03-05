'''
urls file for legislator app
note legislator was set to default
redirect in disc_site.urls
'''

from django.urls import path

from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('address', views.get_address, name='address'),
    path('', views.home, name='home'),
    path('non_disc', views.non_disc, name='non_disclosure'),
    path('full_results', views.full_results, name='results'),
]
