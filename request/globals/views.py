from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required

from .models import User
from customers.models import Customer
from venues.models import Venue
from .forms import RegisterForm
from globals import blockchain_api as bcAPI

# Create your views here.
def register(request):
    # if user is already logged in, redirect to home page
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data.get("email")
            password1 = form.cleaned_data.get("password1")
            password2 = form.cleaned_data.get("password2")
            user_type = form.cleaned_data.get("user_type")
            name = form.cleaned_data.get("name")

            if password1 == password2:
                user = User.objects.create_user(email=email, password=password1)

                if user_type == "venue":
                    Venue.objects.create(user=user, name=name, location="Chicago, IL")
                    data = {
                        "venue_location": "Chicago, IL",
                        "venue_name": name
                    }
                    response = bcAPI.post('venue/create', data=data).json()
                    return str(response)

                else:
                    Customer.objects.create(user=user, name=name)
                    data = {
                        "fname": name,
                        "lname": "smith",
                        "email_address": email
                    }
                    response = bcAPI.post('user/create', data=data).json
                    return str(response)


            else:
                messages.error(request, "Passwords do not match.")
                return redirect("register")

            user = authenticate(email=email, password=password1)
            auth_login(request, user)

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
    
def explore(request):
    user = request.user

    # TODO: submit request to blockchain server to get events for explore
    data = {
        "user_email": user.email
    }
    response = bcAPI.post('user/explore', data=data)

    if response.status == 200:
        events = []

        context = {
            "events": events
        }

        return render(request, "explore.html", context)
    else:
        messages.error(request, "Can't contact blockchain server.")
        return redirect("/")