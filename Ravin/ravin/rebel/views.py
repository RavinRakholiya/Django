# I have created this file
from django.shortcuts import render

def login(request):
    return render(request,'rebel/login.html')

def home(request):
    userid=request.POST.get("email",'default')
    password=request.POST.get("password",'default')
    print(f"my email is:{userid} and password is:{password}")
    params={'email':userid,'password':password}
    return render(request, 'rebel/home.html', params)


def registration(request):
    return render(request, 'rebel/registration.html')


def changepassword(request):
    return render(request, 'rebel/changepassword.html')
