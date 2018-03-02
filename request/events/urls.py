from django.urls import path

from .views import (
    create_event,
    create_tickets
)

urlpatterns = [
    path("create", create_event, name="create-event"),
    # path("<int:event_id>/", view_event)
    path("<int:event_id>/create-tickets/", create_tickets, name="create-tickets")
]
