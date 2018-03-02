from django.urls import path

from . import views

urlpatterns = [
    path("<int:venue_id>/", views.venue, name="venue"),
    path("list/<int:event_id>/<int:ticket_num>/", views.list_ticket, name="list_ticket")
]
