import requests

from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

def index(request):
    # do some base stuff
    return HttpResponse("You are at the API base. Ideally, this would have help information.")  

def buyTicket(request):
    # need to do some requesting to Blockchain flask api
    api_ip = settings.BLOCKCHAIN_API['address']
    api_port = settings.BLOCKCHAIN_API['port']
    r = requests.get('http://{}:{}/'.format(api_ip, api_port))
    return HttpResponse("do something")

def listTicket(request):
    # need to do some request to Blockchain flask api
    return HttpResponse("you are at api list endpoint")
