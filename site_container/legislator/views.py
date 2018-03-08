'''
views file for legislator  app
'''
from django.shortcuts import render_to_response
from django.http import HttpResponse
from legislator.models import Lawmaker, FinancialInterest, OpenCorps
from legislator.forms import DataForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import loader, Context
from .dynamic_address_query import get_legislator_names
from .tables import LawmakerTable

def home(request):
    '''
    This is the main view of the website. Users input into one
    of the three input areas:

    Address: User inputs an address, and the view redirects
             to the appropriate results page.

    State/Distric: User inputs a State, and may input a District.
                   The page will redirect and show all legislators
                   in the State (and will filter by district if required).

    Lawmaker: User inputs a single lawmaker. Redirects to a
              detailed page, which will redirect to the relevant
              page depending on the financial interest meta data.
    '''
    if request.method == 'POST':
        form = DataForm(request.POST)
        print(form.data)
        if form.data['address']:
            return HttpResponseRedirect('/legislator/from/address/{}/'.format(form.data['address']))

        if form.data['legislator']:
            return HttpResponseRedirect('/legislator/{}/'.format(form.data['legislator'], form.data['legislator']))
        
        usr_dist = 'ALL' if not form.data['district'] else form.data['district']
        usr_state = form.data['state']
        return HttpResponseRedirect('/legislator/{}/{}/'.format(form.data['state'], usr_dist))
    
    else:
        form = DataForm()
   
    return render(request, 'home_page.html', {'form': form})

def state_dist(request, usr_state, usr_dist):
    '''
    This view displays the results for every legislator in
    the given State and District.

    This page is meant to only show the legislator and
    their disclosure forms.
    '''
    if usr_dist == 'ALL':
        q_set = Lawmaker.objects.filter(state=usr_state)
    else:
        q_set = Lawmaker.objects.filter(state=usr_state, district = usr_dist)
    return render(request, 'by_state.html', {"lm_table":q_set})

def by_lawmaker(request, lawmaker):
    form = request.GET
    lm_set = Lawmaker.objects.filter(name=lawmaker)
    if not lm_set:
        return HttpResponse('Lawmaker not found - sorry!')
    
    lm_names = [lm.name for lm in lm_set] 
    fi_set = FinancialInterest.objects.filter(lawmaker__name__in=lm_names)
    if not fi_set: #CPI has no known data on these legislators.
        return render(request, 'no_fi.html', {"lm_table":lm_set})

    fi_names = [fi.name for fi in fi_set]
    oc_set = OpenCorps.objects.filter(finterest__name__in=fi_names)
    if not oc_set:
       return render(request, 'no_oc.html', {"lm_table":lm_set, "fi_table":fi_set})
    
    return render(request, 'has_oc.html', {"lm_table":lm_set,
                                           "fi_table":fi_set,
                                           "oc_table":oc_set})

def from_address(request, address):
    '''
    This view takes in an address as a string, and returns a
    data structure containing law maker names....
    It will do other things too.
    '''
    legislators = get_legislator_names(address)
    lm_set = Lawmaker.objects.filter(name__in=legislators)
    
    fi_set = FinancialInterest.objects.filter(lawmaker__name__in=legislators)
    if not fi_set: #CPI has no known data on these legislators.
        return HttpResponseRedirect('/legislator/no/known/entities/{}/'.format(address), address)

    fi_names = [fi.name for fi in fi_set]
    oc_set = OpenCorps.objects.filter(finterest__name__in=fi_names)
    if not oc_set:
        return HttpResponseRedirect('/legislator/has/fi/but/no/oc/{}/'.format(address), address)
    return HttpResponseRedirect('/legislator/has/fi/and/oc/{}/'.format(address), address)

def no_known(request, address):
    '''
    This view is to show when the lawmakers returned
    have no known financial interests from CPI.

    It displays a message as to why this might be the case
    and shows a table of lawmaker information.
    '''
    legislators = get_legislator_names(address)
    lm_set = Lawmaker.objects.filter(name__in=legislators)
    return render(request, 'no_fi.html', {"lm_table":lm_set})

def no_oc(request, address):
    '''
    This view is to show lawmakers with CPI data, but
    no data from open_corporates.

    It displays a message as to why this might be the case
    and two tables: one of lawmaker data queried, and one of
    metadata to the respective financial interests.
    '''
    legislators = get_legislator_names(address)
    lm_set = Lawmaker.objects.filter(name__in=legislators)
    fi_set = FinancialInterest.objects.filter(lawmaker__name__in=legislators)
    return render(request, 'no_oc.html', {"lm_table":lm_set, "fi_table":fi_set})

def has_oc(request, address):
    '''
    This view is to show lawmakers with CPI and OC data,
    resulting from an address search.

    It displays a table for lawmakers, a table for their financial
    interests, and a table for their open corporates metadata.
    '''
    legislators = get_legislator_names(address)
    lm_set = Lawmaker.objects.filter(name__in=legislators)
    fi_set = FinancialInterest.objects.filter(lawmaker__name__in=legislators)
    oc_set = OpenCorps.objects.filter(finterest__name__in=fi_names)
    return render(request, 'has_oc.html', {"lm_table":lm_set,
                                           "fi_table":fi_set,
                                           "oc_table":oc_set})


