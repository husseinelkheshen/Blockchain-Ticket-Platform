from django.urls import path

from . import views

urlpatterns = [
    path("buy/<int:ticket_num>", views.buy_ticket, name="buy_ticket")
]
