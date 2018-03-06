from django.urls import path

from . import views

urlpatterns = [
    path("tickets/", views.list_customer_tickets, name="list-customer-tickets"),
    path("buy/<int:event_id>/<int:ticket_num>", views.buy_ticket, name="buy-ticket"),
    path("list/<int:event_id>/<int:ticket_num>", views.list_customer_ticket, name="list-customer-ticket"),
    path("ticket_code/<int:event_id>/<int:ticket_num>", views.ticket_code, name="ticket-code"),
    path("upgrade_ticket/<int:event_id>/<int:ticket_num>", views.upgrade_ticket, name="upgrade-ticket")
]
