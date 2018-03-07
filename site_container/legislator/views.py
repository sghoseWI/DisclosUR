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

def state_dist(request, usr_state, usr_dist):
    if usr_dist == 'ALL':
        q_set = Lawmaker.objects.filter(state=usr_state)
    else:
        q_set = Lawmaker.objects.filter(state=usr_state, district = usr_dist)
    return render(request, 'by_state_temp.html', {"state_table":q_set})

def by_lawmaker(request, lawmaker):
    form = request.GET
    qset = Lawmaker.objects.filter(name=lawmaker)
    if qset:
        lm = qset[0]
        print(lm)
        return HttpResponse('{} {} {}'.format(lm.name, lm.state, lm.district))
        return HttpResponseRedirect('/legislator/lawmaker_exists/',lm)
    return HttpResponse('Lawmaker not found - sorry!')

def home(request):
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

def non_disc(request):
    return render(request, 'non_disc_states.html', context={})

def from_address(request, address):
    '''
    This view takes in an address as a string, and returns a
    data structure containing law maker names....
    It will do other things too.
    '''
    legislators = get_legislator_names(address)
    for dude in legislators:
        print(dude)
    lm_set = Lawmaker.objects.filter(name__in=legislators)
    fi_set = FinancialInterest.objects.filter(lawmaker__name__in=legislators)
    if not fi_set: #CPI has no known data on these legislators.
        print('YOOOO')
        return HttpResponseRedirect('/legislator/no/known/entities/{}/'.format(address), address)
    
    return render(request, 'state_table.html', {"state_table":lm_set})

def no_known(request, address):
    legislators = get_legislator_names(address)
    lm_set = Lawmaker.objects.filter(name__in=legislators)
    return render(request, 'state_table.html', {"state_table":lm_set})



def full_results(request, lm):
    #lm.name, rv.state, rv.district
    return render(request, 'full_info.html', context={})

def data_viz(request):
    return render(request, 'data_viz.html', context={})
