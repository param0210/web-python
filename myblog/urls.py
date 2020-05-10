from django.conf.urls import url
from.import views
from django.conf.urls.i18n import urlpatterns

app_name='myblogs'
 
urlpatterns=[
    url(r'^about-us$',views.about,name='aboutus'),
    url(r'^homepage$',views.homepage,name='homepage'),
    url(r'blog-list',views.blog_list,name='blog'),
    url(r'^create/$',views.blog_create,name='create'),
    url(r'^(?P<slug>[\w-]+)/$',views.blog_details,name='details'),

    
    
    ]