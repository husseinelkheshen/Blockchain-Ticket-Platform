from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required

from .models import User
from .forms import RegisterForm

# Create your views here.
def register(request):
    # if user is already logged in, redirect to home page
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password1")

            user = authenticate(email=email, password=password)
            login(request, user)

            return redirect("home")
    else:
        form = RegisterForm()

    return render(request, "register.html", {"form": form})

def login(request):
    # if user is already logged in, redirect to home page
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        user = authenticate(
            email=request.POST["email"],
            password=request.POST["password"])

        if user and user.is_active:
            auth_login(request, user)
            messages.success(request, "Successfully logged in.")
            return redirect("home") # redirect to homepage
        else: # login failed
            messages.error(request, "Invalid login credentials.")
            return redirect("login")
    else: # display login page
        return render(request, "login.html")

@login_required
def logout(request):
    auth_logout(request)
    messages.success(request, "Successfully logged out.")
    return redirect("home")


def home(request):
    return render(request, "home.html")
