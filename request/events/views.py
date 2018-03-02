from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from globals.decorators import venue_login_required
from .models import Event
from venues.models import Venue

# Create your views here.
@venue_login_required
def create_event(request):
    if request.method == "POST":
        form = CreateEventForm(request.POST)
        if form.is_valid():
            user = request.user
            venue = Venue.objects.get(user=user)

            Event.objects.create(venue=venue, name=name)

            # TODO: API call to blockchain server to create event

            return redirect("home")
    else:
        return render(request, "create_event.html", {"form": form})

@venue_login_required
def create_tickets(request):
    pass

@venue_login_required
def manage_event(request):
    pass

@venue_login_required
def manage_tickets(request):
    pass

@venue_login_required
def view_events(request):
    pass
