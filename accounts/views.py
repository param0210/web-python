from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from.forms import *
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login as auth_login,logout
# Create your views here.
@csrf_exempt   
def signup(request):
    if request.method=="POST":
       form=SignUpForm(request.POST)
       if form.is_valid():
           form.save()
           return redirect('accounts:login')
       else:
            return render(request,'accounts/signup.html')

           
    else:
        form=SignUpForm()
        return render(request,'accounts/signup.html',{'form':form})
    
@csrf_exempt   
def login(request):
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            print(user)
            auth_login(request,user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('myblogs:blog')
            
        else:
            return render(request,'accounts/login.html',{'form':form})

    else:
        form=AuthenticationForm()
        return render(request,'accounts/login.html',{'form':form})
    

@csrf_exempt     
def logout_view(request): 
    if request.method=='POST':
        logout(request)
        return redirect('accounts:login')       
