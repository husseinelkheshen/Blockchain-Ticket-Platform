from django import messages
from django.shortcuts import render, get_object_or_404
from django.decorators import login_required

from globals import blockchain_api as bcAPI
from .models import Customer

# Create your views here.
@login_required
def list_customer_tickets(request):
    """
    Return the list of tickets purchased by the currently logged
    in user.
    """

    # get customer
    customer = get_object_or_404(Customer, user=request.user)

    # prevent customers from seeing the tickets of other customers
    
    # use customer_id to query blockchain server to 
    # get the list of the customer's tickets. 
    # Expect JSON response with list of tickets, each with the name
    # of the event, details of the seat, the ticket id (num), and the venue.
    response = bcAPI.get("tickets/" + str(customer.id)) 

    if not response: # request to blockchain server failed
        messages.error(request, "Couldn't contact blockchain server.")
        return redirect("home")

    context = {"tickets": response}

    return render(request, "customer_ticket_list.html", context)
