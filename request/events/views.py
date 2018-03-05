import requests

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import Http404

from globals.decorators import venue_login_required
from .models import Event
from venues.models import Venue
from .forms import (
    CreateEventForm, 
    CreateTicketsForm, 
    EditEventForm,
    EditTicketsForm
)
from globals import blockchain_api as bcAPI


# Create your views here.
@venue_login_required
def create_event(request):
    if request.method == "POST":
        form = CreateEventForm(request.POST)
        if form.is_valid():
            user = request.user
            venue = Venue.objects.get(user=user)
            name = form.cleaned_data.get("name")
            description = form.cleaned_data.get("description")
            when = form.cleaned_data.get("when")

            event = Event.objects.create(venue=venue, name=name, description=description)
            print("event id: ", event.id)

            # TODO: API call to blockchain server to create event
            data = {
                "venue": {
                    "venue_location": venue.location,
                    "venue_name": venue.name
                },
                "name": name,
                "description": description,
                "event_id": event.id,
                "time": {
                    "minute": when.minute,
                    "hour": when.hour,
                    "day": when.day,
                    "month": when.month,
                    "year": when.year
                }
            }

            response = bcAPI.post('venue/event/create', data=data)
            if response[0].get('event_id') == event.id:
                messages.success(request, "Event successfully created.")
            else:
                # messages.failure(request, "Event non ")
                messages.error(request, "Failed to create event.")
                event.delete()

            return redirect("home")
    else:
        form = CreateEventForm()

    return render(request, "create_event.html", {"form": form})

@venue_login_required
def create_tickets(request, event_id):
    try:
        event = Event.objects.get(pk=event_id)
    except Event.DoesNotExist:
        raise Http404("Event does not exist.")

    if request.method == "POST":
        form = CreateTicketsForm(request.POST)
        if form.is_valid():
            # getting data from form
            section = form.cleaned_data.get("section")
            min_row = form.cleaned_data.get("min_row")
            max_row = form.cleaned_data.get("max_row")
            min_seat = form.cleaned_data.get('min_seat')
            max_seat = form.cleaned_data.get('max_seat')
            face_value = form.cleaned_data.get('face_value')


            venue = Venue.objects.get(user=request.user)

            # check if venue has the permissions to create tickets for
            # an event.
            if event.venue == venue:
                # TODO: API call to blockchain server to create tickets
                data = {
                    "venue": {
                            "venue_location": venue.location,
                            "venue_name": venue.name
                    },
                    "event_id": event.id,
                    "tickets_info": {
                        "face_value": face_value,
                        "section": section,
                        "row_range": {
                            "begin": min_row,
                            "end": max_row
                        },
                        "seat_range": {
                            "begin": min_seat,
                            "end": max_seat
                        }
                    }
                }
                response = bcAPI.post('venue/event/tickets/create',data=data)
                messages.success(
                    request, "Tickets successfully created."
                )
                print(response[0])

                return redirect("create-tickets", event.pk)
            else:
                messages.error(
                    request,
                    "You are not authorized to create tickets for this event."
                )

                return redirect("home")
    else:
        form = CreateTicketsForm()

    context = {
        "form": form,
        "event": event
    }

    return render(request, "create_tickets.html", context)

@venue_login_required
def edit_event(request, event_id):
    """
    Allows a venue to edit an event's date, time, and description.
    """
    event = get_object_or_404(Event, pk=event_id)

    if request.method == "POST":
        form = EditEventForm(request.POST, instance=event)

        if form.is_valid():
            venue = Venue.objects.get(user=request.user)
            event = form.save(commit=False)

            data = {
                "venue": {
                    "venue_location": venue.location,
                    "venue_name": venue.name
                },
                "event_id": event.id,
                "update_info": {
                    "name": event.name,
                    "desc": event.description,
                    "time": {
                        "minute": event.when.minute,
                        "hour": event.when.hour,
                        "day": event.when.day,
                        "month": event.when.month,
                        "year": event.when.year
                    }
                }
            }

            response = bcAPI.post('venue/event/edit', data=data)
            print(response)
            if response[0].get('event_id') == event.id:
                messages.success(request, "Event successfully edited.")
                event.save()
            else:
                messages.error(request, "Failed to edit event.")

            return redirect("venue", venue.id)
    else:
        form = EditEventForm(instance=event)

    context = {
        "form": form,
        "event": event
    }

    return render(request, "edit_event.html", context)


@venue_login_required
def edit_tickets(request, event_id):
    """
    Edit the price of a ticket given ticket number, section, and seat.
    """
    event = get_object_or_404(Event, pk=event_id)
    venue = get_object_or_404(Venue, user=request.user)

    if request.method == "POST":
        form = EditTicketsForm(request.POST)

        if form.is_valid():
            new_price = form.cleaned_data.get("face_value")
            section = form.cleaned_data.get("section")
            row = form.cleaned_data.get("row")
            seat_num = form.cleaned_data.get("seat")

            data = {
                "venue": {
                    "venue_location": venue.location,
                    "venue_name": venue.name
                },
                "event_id": event_id,
                "update_info": {
                    "new_price": new_price,
                    "which_seats": {
                        "section": section,
                        "row": row,
                        "seat_num": seat_num
                    }
                }
            }

            response = bcAPI.post('venue/event/tickets/edit', data=data)
            print(response)
            if response[1] == 200:
                messages.success(request, "Tickets edited.")
            else:
                messages.error(request, "Failed to edit tickets.")

        else:
            messages.error(request, "Something went wrong.")
    else:
        form = EditTicketsForm()
    
    context = {
        "form": form,
        "event": event,
        "venue": venue
    }

    return render(request, "edit_tickets.html", context)
    

def event(request, event_id):
    """
    View for an event. A venue with the appropriate permissions can use
    this view to view tickets for an event.
    """
    try:
        event = Event.objects.get(pk=event_id)
    except Event.DoesNotExist:
        raise Http404("Event does not exist.")
    data =  {
                "venue": {
                    "venue_location": event.venue.location,
                    "venue_name": event.venue.name
                },
                "event_id": event_id
            }
    response = bcAPI.post('venue/view_event', data=data)
    e = response[0]
    tickets = []
    # TODO: get tickets by making API call to blockchain server
    # tickets = []
    try:
        user_venue = Venue.objects.get(user=request.user)
    except Venue.DoesNotExist as ex:
        user_venue = None

    # check if venue has the permissions to create tickets for
    # an event.
    print("user venue: "+ str(user_venue))
    print("event venue" + str(event.venue))
    print(event.venue == user_venue)
    if event.venue == user_venue:
        response = bcAPI.post('venue/event/view_tickets', data=data)
        tickets = response[0]


    print(response)
    context = {
        "event": event,
        "tickets": tickets
    }

    return render(request, "event.html", context)
