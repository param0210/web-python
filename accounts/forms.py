from django import forms
from django.contrib.auth.forms import UserCreationForm
from myblog.models import *
from django.forms.widgets import CheckboxSelectMultiple


GENDER=[
    ('male','MALE'),
    ('female','FEMALE'),
    ('transgender','TRANSGENDER')
    ]
class SignUpForm(UserCreationForm):
#     date_of_birth=forms.DateField(widget=forms.SelectDateWidget())
#     gender=forms.ChoiceField(choices=GENDER)


    class Meta:
        model = MyUser
        fields = ('first_name','last_name','email','username' )
        
#         
#     def clean_my_field(self):
#         if len(self.cleaned_data['date_of_birth']) > 2:
#            raise forms.ValidationError('Select no more than 3.')
#         return self.cleaned_data['date_of_birth']
