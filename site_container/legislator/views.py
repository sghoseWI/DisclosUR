'''
views file for legislator  app
'''
from django.shortcuts import render_to_response
from django.http import HttpResponse
from legislator.models import Lawmaker
from legislator.forms import AddressForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import loader, Context


def index(request):
    return HttpResponse("This is the legislator application index")

def home(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AddressForm(request.POST)
        # check whether it's valid:
        # if form.is_valid():
            # process the data in form.cleaned_data as required
            # redirect to a new URL:
        return HttpResponseRedirect('http://127.0.0.1:8000/full_results')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = AddressForm()
    return render(request, 'home_page.html', {'form': form})

def non_disc(request):
    return render(request, 'non_disc_states.html', context={})

def full_results(request):
    return render(request, 'full_info.html', context={})

    # render(request, 'home_page.html', {})
