from django.shortcuts import render
from django.http import HttpResponse
from aiohttp.client import request
from .models import * 
from django.contrib.auth.decorators import login_required


# Create your views here.

def about(request):
    #+return HttpResponse("about page")
    return render(request,'myblog/about.html')


def homepage(request):
#     return HttpResponse("welcome to homepage")
      return render(request,'myblog/home.html')
  
def blog_list(request):
    blog=Blog.objects.all().order_by('-created_on')
    return render(request,'myblog/blog.html',{'all_blog':blog})

def blog_details(request,slug):
    print(slug)
    blog=Blog.objects.get(slug=slug)
    return render(request,'myblog/blog_details.html',{'blogs':blog})
    #return HttpResponse(slug)
    
@login_required(login_url='/accounts/login/') 
def blog_create(request):
    return render(request,'myblog/blog_create.html')
    
