from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from globals import blockchain_api as bcAPI
from globals.decorators import customer_login_required
from .models import Customer
from events.models import Event

# Create your views here.
@customer_login_required
def buy_ticket(request, event_id, ticket_num):
    """
    Tell the blockchain server that the logged in customer intends 
    to purchase the ticket with the given ticket_num.
    """
    # get customer
    customer = get_object_or_404(Customer, user=request.user)
    event = get_object_or_404(Event, pk=event_id)
    venue = event.venue

    # build data
    data = {
        "user_email": customer.user.email,
        "event_id": event_id,
        "ticket_num": ticket_num,
        "venue": {
            "venue_location": venue.location,
            "venue_name": venue.name
        }
    }

    # send POST request to blockchain server with data.
    response = bcAPI.post("user/buy_ticket", data=data)

    # expect 200 response if successful.
    if response[1] != 200:
        print(response[0])
        messages.error(request, "Couldn't contact blockchain server.")
    else:
        messages.success(request, "Ticket successfully purchased.")

    return redirect("home")


@customer_login_required
def list_customer_tickets(request):
    """
    Return the list of tickets purchased by the currently logged
    in user.
    """

    # get customer
    customer = get_object_or_404(Customer, user=request.user)

    # use customer id to query blockchain server to 
    # get the list of the customer's tickets. 
    # Expect JSON response with list of tickets, each with the name
    # of the event, details of the seat, the ticket id (num), and the venue.
    # TODO
    response = bcAPI.post("user/view_tickets", data={"user_email": customer.user.email}) 

    if response[1] != 200: # request to blockchain server failed
        messages.error(
            request, 
            "Couldn't contact blockchain server.")
        return redirect("home")

    context = {"tickets": response[0]}

    return render(request, "customer_ticket_list.html", context)

@customer_login_required
def list_customer_ticket(request, event_id, ticket_num):
    """
    List a ticket that a customer owns.
    """
    # get venue
    event = get_object_or_404(Event, pk=event_id)

    # build data
    data = {
        "venue": {
            "venue_location": event.venue.location,
            "venue_name": event.venue.name
        },
        "event_id": event_id,
        "ticket_num": ticket_num,
        "user_email": request.user.email
    }

    # send POST request to blockchain server with data
    response = bcAPI.post("user/list_ticket", data=data)

    # expect 201 response if successful.
    if response[1] != 200:
        messages.error(request, "Couldn't contact blockchain server.")
    else:
        messages.success(request, "Ticket successfully listed.")

    return redirect("list-customer-tickets")
