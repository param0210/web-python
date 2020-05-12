from django.conf.urls import url
from.import views
from.models import *
from django.conf.urls.i18n import urlpatterns

app_name='accounts'

urlpatterns=[
    url(r'^sign-up/$',views.signup,name='sign-up'),
    url(r'^login/',views.login,name='login'),
    url(r'logout/$',views.logout_view,name='logout')
    
    ]