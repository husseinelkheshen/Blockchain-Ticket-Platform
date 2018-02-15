import requests

from django import settings

def get(path):
    """
    Send GET request to given path on blockchain server, and, if 
    succcessful, return a decoding of the response. Assumes that
    response is JSON.
    """
    r = request.get(
            settings.BLOCKCHAIN_API["host"] + "/" + path, 
            timeout=settings.API_TIMEOUT)
    
    # if request fails
    if r.status_code != 200:
        return None
    
    return r.json()

def post(path, data):
    """
    Send POST request with given data to given path on blockchain 
    server, and, if succcessful, return a decoding of the response. 
    Assumes that response is JSON.
    """
    r = request.get(
            settings.BLOCKCHAIN_API["host"] + "/" + path, 
            timeout=settings.API_TIMEOUT)
    
    # if request fails
    if r.status_code != 200:
        return None
    
    return r.json()
