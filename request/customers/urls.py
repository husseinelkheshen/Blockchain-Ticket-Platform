from django.urls import path

from . import views

urlpatterns = [
    path("tickets/", views.list_customer_tickets, name="list-customer-tickets"),
    path("buy/<int:event_id>/<int:ticket_num>", views.buy_ticket, name="buy-ticket")
]
