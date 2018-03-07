'''
urls file for legislator app
note legislator was set to default
redirect in disc_site.urls
'''

from django.urls import path

from . import views

urlpatterns = [
        path('', views.home, name='home'),
        path('<usr_state>/<usr_dist>/', views.state_dist, name='test'),
        path('<lawmaker>/', views.by_lawmaker, name='by_law'),
        path('lawmaker_exists/', views.full_results, name='lm_exists'),
        path('from/address/<address>/', views.from_address, name='address'),
]
