from django import forms
STATES = {
         'Alaska'                   : 'AK',
         'Alabama'                  : 'AL',
         'Arkansas'                 : 'AR',
         'American Samoa'           : 'AS',
         'Arizona'                  : 'AZ',
         'California'               : 'CA',
         'Colorado'                 : 'CO',
         'Connecticut'              : 'CT',
         'District of Columbia'     : 'DC',
         'Delaware'                 : 'DE',
         'Florida'                  : 'FL',
         'Georgia'                  : 'GA',
         'Guam'                     : 'GU',
         'Hawaii'                   : 'HI',
         'Iowa'                     : 'IA',
         'Idaho'                    : 'ID',
         'Illinois'                 : 'IL',
         'Indiana'                  : 'IN',
         'Kansas'                   : 'KS',
         'Kentucky'                 : 'KY',
         'Louisiana'                : 'LA',
         'Massachusetts'            : 'MA',
         'Maryland'                 : 'MD',
         'Maine'                    : 'ME',
         'Michigan'                 : 'MI',
         'Minnesota'                : 'MN',
         'Missouri'                 : 'MO',
         'Northern Mariana Islands' : 'MP',
         'Mississippi'              : 'MS',
         'Montana'                  : 'MT',
         'National'                 : 'NA',
         'North Carolina'           : 'NC',
         'North Dakota'             : 'ND',
         'Nebraska'                 : 'NE',
         'New Hampshire'            : 'NH',
         'New Jersey'               : 'NJ',
         'New Mexico'               : 'NM',
         'Nevada'                   : 'NV',
         'New York'                 : 'NY',
         'Ohio'                     : 'OH',
         'Oklahoma'                 : 'OK',
         'Oregon'                   : 'OR',
         'Pennsylvania'             : 'PA',
         'Puerto Rico'              : 'PR',
         'Rhode Island'             : 'RI',
         'South Carolina'           : 'SC',
         'South Dakota'             : 'SD',
         'Tennessee'                : 'TN',
         'Texas'                    : 'TX',
         'Utah'                     : 'UT',
         'Virginia'                 : 'VA',
         'Virgin Islands'           : 'VI',
         'Vermont'                  : 'VT',
         'Washington'               : 'WA',
         'Wisconsin'                : 'WI',
         'West Virginia'            : 'WV',
         'Wyoming'                  : 'WY'}
         #http://code.activestate.com/recipes/577305-python-dictionary-of-us-states-and-territories/

class DataForm(forms.Form):
    '''
    Let's hope this works.
    '''
    address =  forms.CharField(label='Your home address', required=False)
    state = forms.ChoiceField(label='state', required=False, choices=STATES)
    district = forms.CharField(label='state', required=False)
    lawmaker = forms.CharField(label='lawmaker', required=False)

