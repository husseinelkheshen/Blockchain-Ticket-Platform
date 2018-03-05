from django.urls import path

from .views import (venue, list_ticket, validate_ticket, schedule_release)

urlpatterns = [
    path("<int:venue_id>/", venue, name="venue"),
    path("list/<int:event_id>/<int:ticket_num>/", list_ticket, name="list-ticket"),
    path(
        "validate/<int:event_id>/<int:ticket_num>/",
        validate_ticket,
        name="validate-ticket"),
    path(
        "schedule/<int:event_id>/",
        schedule_release,
        name="schedule-release"),
]
