from django.contrib.auth.decorators import login_required
from venues.models import Venue
from customers.models import Customer

def venue_login_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url=None):
    """
    Decorator for views that checks that the user is logged in and
    whether said user is a venue. Redirects to a different page if necessary.
    """
    actual_decorator = user_passes_test(
        lambda u:
            u.is_authenticated and Venue.objects.get(user=user) is not None,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator

def customer_login_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url=None):
    """
    Decorator for views that checks that the user is logged in and
    whether said user is a customer. Redirects to a different page if necessary.
    """
    actual_decorator = user_passes_test(
        lambda u:
            u.is_authenticated and Customer.objects.get(user=user) is not None,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator
