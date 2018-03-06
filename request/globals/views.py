from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.db import models
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import User
from customers.models import Customer
from venues.models import Venue
from .forms import RegisterForm
from globals import blockchain_api as bcAPI
from globals.decorators import customer_login_required

from datetime import datetime

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
            bc_created = False
            if password1 == password2:

                if user_type == "venue":
                    data = {
                        "venue_location": "Chicago, IL",
                        "venue_name": name
                    }
                    response = bcAPI.post('venue/create', data=data)
                    if response[1] == 200:
                        user = User.objects.create_user(email=email, password=password1)
                        Venue.objects.create(user=user, name=name, location="Chicago, IL")
                        bc_created = True
                    else:
                        messages.error(request, "Request to blockchain API failed.")
                        print(response[1])
                        return redirect("register")

                else:
                    data = {
                        "fname": name,
                        "lname": "smith",
                        "email_address": email
                    }
                    response = bcAPI.post('user/create', data=data)
                    if response[1] == 200:
                        bc_created = True
                        user = User.objects.create_user(email=email, password=password1)
                        Customer.objects.create(user=user, name=name)
                    else:
                        messages.error(request, "Request to blockchain API failed.")
                        return redirect("register")
            else:
                messages.error(request, "Passwords do not match.")
                return redirect("register")

            if bc_created:
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
    
@login_required
def explore(request):
    user = request.user

    # TODO: submit request to blockchain server to get events for explore
    data = {
        "user_email": user.email
    }
    response = bcAPI.post('user/explore', data=data)

    if response[1] == 200:
        events = response[0]

        context = {
            "events": events
        }

        return render(request, "explore.html", context)
    else:
        messages.error(request, "Can't contact blockchain server.")
        return redirect("/")

@customer_login_required
def search(request):
    query = request.GET.get("q")
    print('query',query)
    date = request.GET.get("date") or datetime.now()
    print('date',date)
    date_range = request.GET.get("date-range")
    print('date range',date_range)
    if date_range is None:
        date_range = "1"
    if len(date_range) == 0:
        date_range = "100"
    print('date range',date_range)
    results = None

    if query:
        try:
            date = models.DateField().to_python(date)
        except:
            raise Http404("Incorrectly formatted date.")

        if date is None:
            raise Http404("Incorrectly formatted date.")

        data = {
            "user_email": request.user.email,
            "search_info": {
                "search_text": query,
                "date_range": int(date_range),
                "date": {
                    "year": date.year,
                    "month": date.month,
                    "day": date.day
                }
            }
        }

        response = bcAPI.post('user/search', data=data)

        if response[1] == 200:
            results = response[0]
        else:
            messages.error(request, "Something went wrong while searching. Please try again.")

    context = {
        "results": results,
        "query": query
    }

    return render(request, "search.html", context)