from django.shortcuts import render
from django.http import HttpResponse
from aiohttp.client import request

# Create your views here.

def about(request):
    print("here is request",request)
    #+return HttpResponse("about page")
    return render(request,'myblog/about.html')


def homepage(request):
#     return HttpResponse("welcome to homepage")
      return render(request,'myblog/home.html')
