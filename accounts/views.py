from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from.forms import *
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login as auth_login,logout
from myblog.models import  MyUser
# Create your views here.
@csrf_exempt   
def signup(request):
    if request.method=="POST":
       form=SignUpForm(request.POST)
       if form.is_valid():
           gender=form.cleaned_data['gender']
           first_name=form.cleaned_data['first_name']
           last_name=form.cleaned_data['last_name']
           middle_name=form.cleaned_data['middle_name']
           mobile_number=form.cleaned_data['mobile_number']
           date_of_birth=form.cleaned_data['date_of_birth']
           user=MyUser.objects.create(first_name=first_name,last_name=last_name,mobile_number=mobile_number,gender=gender,date_of_birth=date_of_birth)
           
             
           #form.save()
           return redirect('accounts:login')
       else:
            return render(request,'accounts/signup.html')      
    else:
        form=SignUpForm()
        return render(request,'accounts/signup.html',{'form':form})
    
@csrf_exempt   
def login(request):
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)#parameter data is holds the value of post data we passed in the login form 
        if form.is_valid():
            user=form.get_user()# getting user from form
            print(user)
            auth_login(request,user)
            #if parameter 'next' exist in post request grab that next parameter and redirect to that particular 'next'parameter
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
