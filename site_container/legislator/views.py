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
    return HttpResponse('This is a test for {} {}'.format(state, district))

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
        if form.data['legislator']:
            return HttpResponseRedirect('/legislator/{}/'.format(form.data['legislator'], form.data['legislator']))
        return HttpResponseRedirect('/legislator/{}/{}/'.format(form.data['state'], form.data['district']))
    else:
        form = DataForm()
    return render(request, 'home_page.html', {'form': form})

def non_disc(request):
    return render(request, 'non_disc_states.html', context={})

def full_results(request, lm):
    #lm.name, rv.state, rv.district
 
    return render(request, 'full_info.html', context={})

