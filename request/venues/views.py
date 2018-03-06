import requests

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import Http404

from globals.decorators import venue_login_required
from .models import Venue
from events.models import Event
from globals import blockchain_api as bcAPI
from .forms import ValidateTicketForm, ScheduleReleaseForm

# Create your views here.
def list_ticket(request, event_id, ticket_num):
    """
    Tell the blockchain server that a venue wants to list a
    particular ticket with a given number of an event with
    the given id.
    """
    # get venue
    venue = get_object_or_404(Venue, user=request.user)

    # build data
    data = {
        "venue": {
            "venue_location": venue.location,
            "venue_name": venue.name
        },
        "event_id": event_id,
        "ticket_num": ticket_num
    }

    # send POST request to blockchain server with data
    response = bcAPI.post("venue/event/tickets/list", data=data)

    # expect 201 response if successful.
    if response[1] != 200:
        messages.error(request, "Couldn't contact blockchain server.")
    else:
        messages.success(request, "Ticket successfully listed.")

    return redirect("home")

@venue_login_required
def validate_ticket(request, event_id):
    venue = Venue.objects.get_object_or_404(user=request.user)
    event = Event.objects.get_object_or_404(pk=event_id, venue=venue)

    if request.method == "POST":
        form = ValidateTicketForm(request.POST)
        if form.is_valid():
            ticket_num = form.cleaned_data.get("ticket_num")
            h = form.cleaned_data.get("hsh")
            user_email = form.cleaned_data.get("user_email")

            # TODO: send request to blockchain server to validate ticket
            data = {
                "event_id": event_id,
                "ticket_num": ticket_num,
                "user_email": user_email,
                "hash": h,
                "venue": 
                {
                    "venue_location": venue.location,
                    "venue_name": venue.name
                }
            }
            response = bcAPI.post("venue/event/tickets/validate", data=data)
            if response[1] == 200:
                result = True
            else:
                result = False

            if result:
                messages.success(request, "Ticket validated.")
            else:
                messages.error(request, "Ticket not valid.")

            return redirect("validate_ticket", event_id)
    else:
        form = ValidateTicketForm()

    context = {
        "venue": venue,
        "event": event,
        "form": form
    }

    return render(request, "validate_ticket.html", context)

@venue_login_required
def schedule_release(request, event_id):
    """
    Schedule the release of the tickets for an event.
    """

    venue = get_object_or_404(Venue, user=request.user)
    event = get_object_or_404(Event, pk=event_id, venue=venue)

    if request.method == "POST":
        form = ScheduleReleaseForm(request.POST)

        if form.is_valid():
            date = form.cleaned_data.get("date")
            section = form.cleaned_data.get('section')

        # TODO: send request to blockchain server indicating that
        # venue wants to schedule all the tickets.

        data = {
            "venue": {
                "venue_location": venue.location,
                "venue_name": venue.name
            },
            "event_id": event_id,
            "release_info": {
                "section": section,
                "release_date": {
                    "month": date.month,
                    "day": date.day,
                    "year": date.year
                }
            }
        }
        response = bcAPI.post("venue/schedule_release", data=data)

        if response[1] == "200":
            messages.success(
                request,
                "The tickets have been successfully scheduled."
            )
        else:
            messages.error(request, "Ticket scheduling failed.")
    else:
        form = ScheduleReleaseForm()

    context = {
        "form": form,
        "event": event
    }

    return render(request, template_name="schedule_release.html", context=context)

@venue_login_required
def venue(request, venue_id):
    """
    View the events of a venue.
    """
    try:
        venue = Venue.objects.get(pk=venue_id)
    except Venue.DoesNotExist:
        raise Http404("Venue does not exist.")

    # TODO: get events from API call to blockchain server
    data = {"venue": {"venue_location": venue.location, "venue_name": venue.name}}
    response = bcAPI.post("venue/view_events", data=data)
    events = response[0]


    context = {
        "events": events,
        "venue": venue
    }

    return render(request, "venue.html", context)
