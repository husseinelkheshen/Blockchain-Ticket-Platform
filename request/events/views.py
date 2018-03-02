import requests

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from globals.decorators import venue_login_required
from .models import Event
from venues.models import Venue
from .forms import CreateEventForm, CreateTicketsForm

# Create your views here.
@venue_login_required
def create_event(request):
    if request.method == "POST":
        form = CreateEventForm(request.POST)
        if form.is_valid():
            user = request.user
            venue = Venue.objects.get(user=user)
            name = form.cleaned_data.get("name")

            Event.objects.create(venue=venue, name=name)

            # TODO: API call to blockchain server to create event

            message.success(request, "Event successfully created.")

            return redirect("home")
    else:
        form = CreateEventForm()

    return render(request, "create_event.html", {"form": form})

@venue_login_required
def create_tickets(request, event_id):
    if request.method == "POST":
        form = CreateTicketsForm(request.POST)
        if form.is_valid():
            # getting data from form
            section = form.cleaned_data.get("section")
            min_row = form.cleaned_data.get("min_row")
            max_row = form.cleaned_data.get("max_row")
            event_id = form.cleaned_data.get("event_id")

            venue = Venue.objects.get(user=user)
            event = Event.objects.get(pk="event_id")

            if event.venue == venue:
                # TODO: API call to blockchain server to create tickets

            else:
                messages.error(
                    request,
                    "You are not authorized to create tickets for this event.")
    else:
        form = CreateTicketsForm()

    return render(request, "create_tickets.html", {"form": form})

@venue_login_required
def manage_event(request):
    pass

@venue_login_required
def manage_tickets(request):
    pass

@venue_login_required
def view_events(request):
    pass
