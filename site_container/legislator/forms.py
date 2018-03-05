from django import forms

class AddressForm(forms.Form):
    '''
    Very simple input form for just Address.
    The GoogleMaps API handles validation, however
    document that testing!
    '''
    address = forms.CharField(label='Enter an Address:')
    #input_type = 'text'
    template_name = 'django/forms/widgets/text.html'





'''
When we want to search by individual lawmaker - we could do this
#from models import Lawmaker
class LawmakerForm(forms.ModelForm):

    class Meta:
        Information that doesn't define the form belongs here.
        model = Lawmaker

'''
