from ../../back_end/Admit01_Blockchain.py import *

venue1 = Venue("Apollo Theater", "Chicago, IL") # success
venue2 = Venue("Apollo Theater", "Chicago, IL") # failure
venue3 = Venue("", "Miami, FL") # failure
venue4 = Venue("Civic Opera House", "") # failure

def test_allvalid:
    assert venue1.id != None and
           venue1.name == "Apollo Theater" and
           venue1.location == "Chicago, IL"

def test_dupvenue:
    assert venue2.id == None and
           venue2.name == None and
           venue2.location == None

def test_badname:
    assert venue3.id == None and
           venue3.name == None and
           venue3.location == None

def test_badloc:
    assert venue4.id == None and
           venue4.name == None and
           venue4.location == None 
