from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

# Create your views here.
def login(request):
    if request.method == "POST":
        user = authenticate(
            username=request.POST["username"], 
            password=request.POST["password"])

        if user and user.is_active:
            login(request, user) 
            return redirect("home") # redirect to homepage
        else: # login failed
            messages.error(request, "Invalid login credentials.")
            return redirect("login")
    else: # display login page
        return render(request, "login.html")


def home(request):
    return render(request, "home.html")
