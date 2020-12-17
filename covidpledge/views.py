from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def home(request):
    return render(request,'index.html')

def loginPage(request):
    return render(request,'login.html')

def registerPage(request):
    return render(request,'register.html')

def contact(request):
    return render(request,'contactus.html')