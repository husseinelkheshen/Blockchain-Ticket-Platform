from blockchain.Admit01_Blockchain import *
from datetime import datetime
from datetime import timedelta
import copy


valid_datetime = datetime.now() + timedelta(days=7) # one week from now

user1 = User("Gina", "Yu", "gy@example.com") 
user1.wallet = 10000
description_dict = user1.description_pref

venue1 = Venue("Wrigley Field", "Chicago, IL")
desc = "Lady Gaga in Chicago for the stadium world tour"
description_list = user1.chunkTags(desc)

event1 = Event("Lady Gaga", valid_datetime, desc)
event1.venue = venue1
seat1 = Seat("Floor Center", "G", 1)
seat2 = Seat("Floor Center", "G", 2)
venue1.events[event1.id] = (event1, copy.deepcopy(event1.blockchain))

ticket1 = venue1.createTicket(event1, 550, seat1)    # success
ticket2 = venue1.createTicket(event1, 600, seat2)


"""
Test updatePreference's success both when called alone
and when called in function
"""

def test_locationpref_insertion():
    """ Test insertion of ticket location into location_pref dictionary """
    user1.updatePreferences(ticket1, "buy", None)
    assert(venue1.location in user1.location_pref)

def test_venuepref_insertion():
    """ Test insertion of ticket venue into venue_pref dictionary """
    user1.updatePreferences(ticket1, "buy", None)
    assert(venue1 in user1.venue_pref)

def test_descriptionpref_insertion():
    """ Test insertion of tags list into description_pref dictionary """
    user1.updatePreferences(ticket1, "buy", None)
    success = 0
    n = len(description_list)
    for i, elem in enumerate(description_list):
        if elem in description_dict:
            success += 1
    assert(success is n)

def test_buyTicket_insertion():
    """ Test insertion of preferences when user purchases ticket """
    user1.buyTicket(ticket1)
    assert(venue1 in user1.venue_pref and venue1.location in user1.location_pref)

def test_upgradeTicket_insertion():
    """ Test insertion of preferences when user upgrades ticket """
    user1.buyTicket(ticket1)
    user1.upgradeTicket(ticket1, ticket2)
    assert(venue1 in user1.venue_pref and venue1.location in user1.location_pref)

def test_search_insertion():
    """ Test insertion of preferences when user searches """
    user1.search(desc)
    success = 0
    n = len(description_list)
    for i, elem in enumerate(description_list):
        if elem in description_dict:
            success += 1
    assert(success is n)