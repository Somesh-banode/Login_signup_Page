from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout 
from django.http import HttpResponse
from .forms import LoginForm
# Create your views here.



def welcome(request):
    return render(request, 'myapp/welcome.html')

def error(request):
    return render(request, 'myapp/error.html')

# def login_action(request):
#     global email, password
#     if request.method =="POST":
#         d = request.POST  #it stores in dictionary in phython[dictionary in py is like key value pair as in hashmap in java]
#         for key, value in d.items():
#             if key =="email":
#                 email =value
#             if key =="password":
#                 password =value
#             if key =="username":
#                 username =value
#         form =LoginForm(request.POST)
#         if form.is_valid():
#             #form.save()
#             email = form.cleaned_data['email']
#             password = form.cleaned_data['password']
#             user = authenticate(request, email=email, password=password)
#             if user:
#                 login(request, user)
#                 return redirect('welcome')
#             else:
#                 return redirect('error')
#             return HttpResponse("Your data got saved")
#         else:
#             return HttpResponse("Your data got saved")
#     else:
#         form =LoginForm()
#     return render(request, 'myapp/login.html',{'form':form})

def login_action(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            #form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('welcome')
            else:
                return redirect('error')
        else:
            return HttpResponse("Failed to save data.")
    else: #method == "GET"
        form = LoginForm()
    return render(request, 'myapp/login.html', {'form':form})




def logout_action(request):
    logout(request)
    return redirect('login')

    
