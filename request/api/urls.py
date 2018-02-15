
from django.urls import path

from . import views

urlpatterns = [
        path('', views.index), 
        path('buy', views.buyTicket), 
        path('list', views.listTicket)
]

