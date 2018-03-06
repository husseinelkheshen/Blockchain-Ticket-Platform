from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

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
def upgrade_ticket(request, event_id, ticket_num):
    customer = get_object_or_404(Customer, user=request.user)
    event = get_object_or_404(Event, pk=event_id)
    venue = event.venue


    if request.method == "POST":

        user_email = customer.user.email
        old_ticket_num = request.POST.get("current-ticket")
        if old_ticket_num is None:
            print('none')
            return redirect('upgrade-ticket')
        # TODO: send request to blockchain server to Upgrade ticket
        data = {
            "event_id": event_id,
            "ticket_num": old_ticket_num,
            "user_email": user_email,
            "new_ticket_num": ticket_num,
            "venue": 
            {
                "venue_location": venue.location,
                "venue_name": venue.name
            }
        }
        response = bcAPI.post("user/upgrade_ticket", data=data)
        if response[1] == 200:
            result = True
        else:
            result = False

        if result:
            messages.success(request, "Ticket upgraded.")
        else:
            messages.error(request, "Ticket not valid.")

        return redirect("list-customer-tickets")
    else:
        response = bcAPI.post("user/view_tickets", data={"user_email": customer.user.email})
        if response[1] == 200:
            context = {"tickets": response[0]}
        else:
            return redirect('home')
        return render(request, "customer_upgrade_ticket.html", context)


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

<<<<<<< HEAD
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
=======

@customer_login_required
def ticket_code(request, event_id, ticket_num):
    """ 
    Get the qr ticket code png from the server
    """
    # get customer
    customer = get_object_or_404(Customer, user=request.user)
    event = get_object_or_404(Event, pk=event_id)
    venue = event.venue

    # build data
    data = {
        "venue": 
        {
            "venue_location": venue.location,
            "venue_name": venue.name
        },
        "user_email": customer.user.email,
        "event_id": event_id,
        "ticket_num": ticket_num
    }
    # send POST request to blockchain server with data.
    response = bcAPI.post_raw("user/generate_ticket_code", data=data)
    f = open("./image.gif", "w")
    f.write(str(response[0]))
    f.close()
    print(len(response[0]))
    # expect 200 response if successful.
    if response[1] != 200:
        return redirect("home")
    
    return HttpResponse((response[0]), content_type="image/gif")
>>>>>>> f08d672d00be7e3d515ff19032163c06ec021124
