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

    class Meta:
        model = MyUser
        fields = ('first_name','last_name','email','username' )
        