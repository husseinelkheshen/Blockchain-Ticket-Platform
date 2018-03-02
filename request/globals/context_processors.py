from venues.models import Venue
from customers.models import Customer

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