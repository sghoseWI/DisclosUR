'''
views file for legislator  app
'''
from django.shortcuts import render_to_response
from django.http import HttpResponse
from legislator.models import Lawmaker
from legislator.forms import DataForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import loader, Context

def state_dist(request, state, district):
    form = request.GET
    usr_state = state
    usr_dist = district
    q_set = Lawmaker.objects.filter(state=usr_state)
    #filter columns, bring in OC data from class
    return render(request, 'state_table.html', {"state_table":q_set})

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
        return HttpResponseRedirect('/legislator/{}/{}/'.format(form.data['state'], form.data['district']))
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
 # OPEN_STATES thing Nick Made goes here (import that thing too)
    return HttpResponse('Address is {}'.format(address))


def full_results(request, lm):
    #lm.name, rv.state, rv.district

    return render(request, 'full_info.html', context={})
