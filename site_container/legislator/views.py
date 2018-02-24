'''
views file for legislator  app
'''
from django.shortcuts import render
from django.http import HttpResponse
from models import Lawmaker
from forms import LawmakerForm
from django.http import HttpResponseRedirect

def index(request):
    return HttpResponse("This is the legislator application index")
