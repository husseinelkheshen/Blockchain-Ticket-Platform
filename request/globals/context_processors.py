from venues.models import Venue
from customers.models import Customer
from globals import blockchain_api as bcAPI

def user_type(request):
    context = {
        "userType": None,
        "userClass": None
    }

    if not request.user.is_authenticated:
        return context

    try:
        venue = Venue.objects.get(user=request.user)
        context["userType"] = "venue"
        context["userClass"] = venue
    except Venue.DoesNotExist:
        try: 
            customer = Customer.objects.get(user=request.user)
            context["userType"] = "customer"
            context["userClass"] = customer
        except Customer.DoesNotExist:
            pass
    
    return context

def wallet(request):
    context = {
        "balance": None
    }

    if not request.user.is_authenticated:
        return context

    try:
        venue = Venue.objects.get(user=request.user)
        
        data = {
            "venue": {
                "venue_location": venue.location,
                "venue_name": venue.name,
            }
        }

        response = bcAPI.post('venue/view_wallet', data=data)

        if response[1] == 200:
            context["balance"] = response[0]["wallet"]
        else:
            return context

    except Venue.DoesNotExist:
        try: 
            customer = Customer.objects.get(user=request.user)

            data = {
                "user_email": customer.user.email
            }

            response = bcAPI.post('user/view_wallet', data=data)

            if response[1] == 200:
                context["balance"] = response[0]["wallet"]
            else:
                return context

        except Customer.DoesNotExist:
            pass
    
    return context