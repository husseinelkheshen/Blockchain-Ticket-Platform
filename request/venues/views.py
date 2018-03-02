from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from .models import Venue
from globals import blockchain_api as bcAPI

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
        "event": event_id,
        "ticket_num": ticket_num
    }

    # send POST request to blockchain server with data
    response = bcAPI.post("tickets/list/", data=data)

    # expect 201 response if successful.
    if response[1] != 201:
        messages.error(request, "Couldn't contact blockchain server.")
    else:
        messages.success(request, "Ticket successfully listed.")

    return redirect("home")

def validate_ticket(request):
    pass

def schedule_release(request):
    """
    Schedule the release of the tickets for an event.
    """
    pass
