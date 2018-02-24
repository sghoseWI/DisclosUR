'''
views file for legislator  app
'''
from django.shortcuts import render
from django.http import HttpResponse
from legislator.models import Lawmaker
from legislator.forms import AddressForm
from django.http import HttpResponseRedirect

def index(request):
    return HttpResponse("This is the legislator application index")
