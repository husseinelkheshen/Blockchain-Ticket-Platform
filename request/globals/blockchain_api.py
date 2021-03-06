import requests
from requests.exceptions import ConnectionError

from django.conf import settings

def get(path):
    """
    Send GET request to given path on blockchain server and return
    a tuple with the decoding of the response as well as the status
    code.
    """
    r = requests.get(
            settings.BLOCKCHAIN_API["host"] + "/" + path, 
            timeout=settings.API_TIMEOUT)
    
    return (r.json(), r.status_code)

def post(path, data):
    """
    Send POST request with given data to given path on blockchain 
    server, and return a tuple with decoding of the response and
    the status code. 
    """
    r = requests.post(
            settings.BLOCKCHAIN_API["host"]+ ":"+ str(settings.BLOCKCHAIN_API['port']) + "/" + path, 
            timeout=settings.API_TIMEOUT, json=data)

    # print(data)   
    # print(r.text)
    return (r.json(), r.status_code)

def post_raw(path, data):
    """
    Send POST request with given data to given path on blockchain 
    server, and return a tuple with decoding of the response and
    the status code. 
    """
    r = requests.post(
            settings.BLOCKCHAIN_API["host"]+ ":"+ str(settings.BLOCKCHAIN_API['port']) + "/" + path, 
            timeout=settings.API_TIMEOUT, json=data)

    return (r.content, r.status_code)