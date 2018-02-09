from ../../back_end/Admit01_Blockchain.py import *

venue1 = Venue("Apollo Theater", "Chicago, IL") # success
venue2 = Venue("Apollo Theater", "Chicago, IL") # failure
venue3 = Venue("", "Miami, FL") # failure
venue4 = Venue("Civic Opera House", "") # failure
# "Miami" and "IL" should also fail; regex validation handled on front end

def test_allvalid:
    #
    # Any unique combination of non-empty name and location Strings should
    # successfully construct a new Venue object
    #
    assert venue1.id != None and
           venue1.name == "Apollo Theater" and
           venue1.location == "Chicago, IL"

def test_dupvenue:
    #
    # If the requested name and location already belong to an existing Venue,
    # then the constructor should create a null Venue object
    #
    assert venue2.id == None and
           venue2.name == None and
           venue2.location == None

def test_badname:
    #
    # Venue objects must have a non-empty name String
    #
    assert venue3.id == None and
           venue3.name == None and
           venue3.location == None

def test_badloc:
    #
    # Venue objects must have a non-empty location String
    #
    assert venue4.id == None and
           venue4.name == None and
           venue4.location == None
