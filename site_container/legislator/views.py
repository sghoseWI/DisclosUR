'''
views file for legislator  app
'''
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("This is the legislator application index")
