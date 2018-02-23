from blockchain.Admit01_Blockchain import *
from datetime import datetime
from datetime import timedelta
import copy

testDatetime = datetime.now() + timedelta(days=7)

testVenue1 = Venue("Regenstein", "Chicago, IL")
testEvent1 = testVenue1.createEvent("Maroon 5", testDatetime, "this is a band")
testEvent2 = testVenue1.createEvent("Maroon 5", testDatetime, "this is a band")
testEvent3 = testVenue1.createEvent("Maroon 5", testDatetime, "this is a band")
testEvent4 = testVenue1.createEvent("Maroon 5", testDatetime, "this is a band")
testEvent5 = testVenue1.createEvent("Maroon 5", testDatetime, "this is a band")
testEvent6 = testVenue1.createEvent("Maroon 5", testDatetime, "this is a band")
testEvent7 = testVenue1.createEvent("Maroon 5", testDatetime, "this is a band")
testEvent8 = testVenue1.createEvent("Maroon 5", testDatetime, "this is a band")
testEvent9 = testVenue1.createEvent("Maroon 5", testDatetime, "this is a band")
testEvent10 = testVenue1.createEvent("Another band", testDatetime, "this is a band")

testVenue2 = Venue("Washington Square Park", "New York City, New York")
testEvent11 = testVenue2.createEvent("Zero 7", testDatetime, "this is also a band")

# To Note - simple weights are introduced to allow for proper testing of preferences
testUser1 = User("Hellen", "Keller", "abcedfg@uchicago.edu")
testUser1.preferences.update({"New York City, New York":5, "Chicago, IL":1})

testUser2 = User("Abraham", "Lincoln", "fourscore@uchicago.edu")

testUser3 = User("John", "Doe", "jdoe@uchicago.edu")
testUser3.preferences.update({"New York City, New York":6, "Chicago, IL":5, "Regenstein":1,
							  "Washington Square Park":1, "Maroon 5":2, "Zero 7":1})

testUser4 = User("Alpha", "Bet", "alphabet@uchicago.edu")
testUser4.preferences.update({"New York City, New York":4, "Chicago, IL":5, "Regenstein":2,
							  "Washington Square Park":1, "Maroon 5":1, "Zero 7":1})

def test_eventslistsize():
	"""
	Make sure everything works properly if inputs are correct, and explore picks out 10 events
	"""
	assert len(testUser1.explore()) == 10

def test_addtags():
	"""
	Make sure tags are being added to user's preferences based on each suggested event
	"""
	testUser2.explore()
	assert "New York City, New York" in testUser2.preferences
	assert "Chicago, IL" in testUser2.preferences
	assert "Regenstein" in testUser2.preferences
	assert "Washington Square Park" in testUser2.preferences
	assert "Maroon 5" in testUser2.preferences
	assert "Zero 7" in testUser2.preferences

def test_usingpreferences1():
	"""
	Make sure the events which are added to list are those which most agree with user preferences
	"""
	eventsList = testUser3.explore()
	assert testEvent1 in eventsList
	assert testEvent2 in eventsList
	assert testEvent3 in eventsList
	assert testEvent4 in eventsList
	assert testEvent5 in eventsList
	assert testEvent6 in eventsList
	assert testEvent7 in eventsList
	assert testEvent8 in eventsList
	assert testEvent9 in eventsList
	assert testEvent11 in eventsList
	assert testEvent10 not in eventsList

def test_usingpreferences2():
	"""
	Similar to above but using a different equivalence class to ensure full testing
	"""
	eventsList = testUser4.explore()
	assert testEvent1 in eventsList
	assert testEvent2 in eventsList
	assert testEvent3 in eventsList
	assert testEvent4 in eventsList
	assert testEvent5 in eventsList
	assert testEvent6 in eventsList
	assert testEvent7 in eventsList
	assert testEvent8 in eventsList
	assert testEvent9 in eventsList
	assert testEvent10 in eventsList
	assert testEvent11 not in eventsList