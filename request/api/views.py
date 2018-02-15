from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("you are at api index")

def buyTicket(request):
    # need to do some requesting to Blockchain flask api
    return HttpResponse("you are at api buy endpoint")

def listTicket(request):
    # need to do some request to Blockchain flask api
    return HttpResponse("you are at api list endpoint")
