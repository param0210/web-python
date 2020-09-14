from django import forms
from django.contrib.auth.forms import UserCreationForm
from myblog.models import *
from django.forms.widgets import CheckboxSelectMultiple



GENDER=[
    ('male','MALE'),
    ('female','FEMALE'),
    ('transgender','TRANSGENDER')
    ]
# class SignUpForm(UserCreationForm):

#     class Meta:
#         model = MyUser
#         fields = ('first_name','last_name','email','username' )

GENDER=(
    ('male','Male'),
    ('female','Female'),
    ('transgender','transgender'),
)     
class SignUpForm(forms.Form):
    
    first_name=forms.CharField(help_text="enter your first name")
    middle_name=forms.CharField(help_text="enter your middle name",required=False)
    last_name=forms.CharField(help_text="enter your last name")
    gender=forms.ChoiceField(choices=GENDER)
    mobile_number=forms.CharField(help_text="enter the valid mobile number")
    date_of_birth=forms.DateField(widget=forms.SelectDateWidget())
    


        