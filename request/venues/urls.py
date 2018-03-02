from django.urls import path

from . import views

urlpatterns = [
    path("<int:venue_id>/", views.venue, name="venue"),
    path("list/<int:event_id>/<int:ticket_num>/", views.list_ticket, name="list-ticket")
    path(
        "validate/<int:event_id>/<int:ticket_num>/",
        views.validate_ticket,
        name="validate-ticket"),
    path(
        "schedule/<int:event_id>/<section>/<int:num_tickets>/",
        views.schedule_release,
        name="schedule-release"),
]
