from django import messages
from django.shortcuts import render, get_object_or_404
from django.decorators import login_required

from globals import blockchain_api as bcAPI
from .models import Customer

# Create your views here.
@login_required
def buy_ticket(request, ticket_num):
    """
    Tell the blockchain server that the logged in customer intends 
    to purchase the ticket with the given ticket_num.
    """
    # get customer
    customer = get_object_or_404(Customer, user=request.user)

    # build data
    data = {
        "user": customer_id,         
        "ticket_num": ticket_num,
    }

    # send POST request to blockchain server with data.
    response = bcAPI.post("tickets/buy/", data=data)

    # expect 201 response if successful.
    if response[1] != 201:
        messages.error(request, "Couldn't contact blockchain server.")
    else:
        messages.success(request, "Ticket successfully purchased.")

    return redirect("home")


@login_required
def list_customer_tickets(request):
    """
    Return the list of tickets purchased by the currently logged
    in user.
    """

    # get customer
    customer = get_object_or_404(Customer, user=request.user)

    # use customer_id to query blockchain server to 
    # get the list of the customer's tickets. 
    # Expect JSON response with list of tickets, each with the name
    # of the event, details of the seat, the ticket id (num), and the venue.
    response = bcAPI.get("tickets/" + str(customer.id)) 

    if response[1] != 200: # request to blockchain server failed
        messages.error(request, "Couldn't contact blockchain server.")
        return redirect("home")

    context = {"tickets": response[0]}

    return render(request, "customer_ticket_list.html", context)
