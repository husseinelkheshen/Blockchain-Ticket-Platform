from django.urls import path

from . import views

urlpatterns = [
    path("list/<int:event_id>/<int:ticket_num>/", views.buy_ticket, name="list_ticket")
]