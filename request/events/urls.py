from django.urls import path

from .views import (
    create_event,
    create_tickets,
    event,
    edit_event,
    edit_tickets
)

urlpatterns = [
    path("create", create_event, name="create-event"),
    path("<int:event_id>/", event, name="event"),
    path("<int:event_id>/edit", edit_event, name="edit-event"),
    path("<int:event_id>/create-tickets/", create_tickets, name="create-tickets"),
    path("<int:event_id>/edit-tickets/", edit_tickets, name="edit-tickets")
]
