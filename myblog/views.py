from django.shortcuts import render
from django.http import HttpResponse
from aiohttp.client import request
from .models import * 

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
    
