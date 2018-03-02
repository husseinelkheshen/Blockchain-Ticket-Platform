from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.index, name='index'),
    path('event/', views.event, name='event'),
    path('login_register/', views.login_register, name='login_register'),
    path('event/login_register/', views.event_login_register, name='event_login_register'),
    path('detail_event/', views.detail_event, name='detail_event'),
    #path('account/', views.account, name='account'),
    #path('event/account/', views.event_account, name='event_account'),
    path('search/', views.search, name='search'),
    path('explore/', views.explore, name='explore'),
    path('purchase/', views.purchase, name='purchase'),
    path('base/', views.base, name='base'),
    path('event_base/', views.event_base, name='event_base'),
]
