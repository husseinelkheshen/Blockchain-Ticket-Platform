from django.urls import path

from .views import (
    create_event,
    create_tickets,
    event
)

urlpatterns = [
    path("create", create_event, name="create-event"),
    path("<int:event_id>/", event),
    path("<int:event_id>/create-tickets/", create_tickets, name="create-tickets")
]
