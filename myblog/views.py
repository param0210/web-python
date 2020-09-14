from django.shortcuts import render,redirect
from django.http import HttpResponse
from aiohttp.client import request
from .models import * 
from django.contrib.auth.decorators import login_required
from.forms import *
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View

# Create your views here.

def about(request):
    #+return HttpResponse("about page")
    return render(request,'myblog/about.html')


def homepage(request):
      return render(request,'myblog/home.html')
  
def blog_list(request):
    
    blog=Blog.objects.all().order_by('-created_on')
    return render(request,'myblog/blog.html',{'all_blog':blog})

def blog_details(request,slug):
    blog=Blog.objects.get(slug=slug)
    return render(request,'myblog/blog_details.html',{'blogs':blog})
    
@login_required(login_url='/accounts/login/') #tell the django what is login url
@csrf_exempt
def blog_create(request):
    if request.method=='POST':
      form=CreateBlog(request.POST,request.FILES)
      if form.is_valid():
          instance=form.save(commit=False)
          instance.writen_by=request.user
          instance.save()
          return redirect('myblogs:myblogs')     
    else:
        form=CreateBlog()
        return render(request,'myblog/blog_create.html',{'form':form})


class BlogCreate(View):
    form_class=CreateBlog
    template='myblog/blog_create.html'

    def get(self,request):
        form=self.form_class()
        return render(request,self.template,{'form':form})

    def post(self,request):
        form=self.form_class(request.POST)
        if form.is_valid:
            instance=form.save(commit=False)
            instance.written_by=request.user
            instance.save()
            return redirect('myblogs:myblogs')
        else:
            return render(request,self.template,{'form':form})
    

    
def user_blogs(request):
    blogs=Blog.objects.filter(writen_by=request.user)
    return render(request,'myblog/user_blogs.html',{'blog':blogs})
