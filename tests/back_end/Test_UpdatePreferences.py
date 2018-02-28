from blockchain.Admit01_Blockchain import *
from datetime import datetime
from datetime import timedelta
import copy


valid_datetime = datetime.now() + timedelta(days=7) # one week from now
venue1 = Venue("Wrigley Field", "Chicago, IL")
event1 = Event("Lady Gaga", valid_datetime, "Stadium world tour")
event1.venue = venue1
seat1 = Seat("Floor Center", "G", 23)
venue1.events[event1.id] = (event1, copy.deepcopy(event1.blockchain))
ticket1 = venue1.createTicket(venue1.events[event1.id][0], 550, seat1)    # success

user1 = User("Gina", "Yu", "gy@example.com") 

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


def test_buyTicket_insertion():
""" Test insertion of preferences when user purchases ticket """
	user1.buyTicket(ticket1)
	assert(venue1 in user1.venue_pref and venue1.location in user1.location_pref)

def test_upgradeTicket_insertion():
""" Test insertion of preferences when user upgrades ticket """
	user1.upgradeTicket(ticket1)
	assert(venue1 in user1.venue_pref and venue1.location in user1.location_pref)

def test_search_insertion():
""" Test insertion of preferences when user searches """
























