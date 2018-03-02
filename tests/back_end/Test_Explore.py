from blockchain.Admit01_Blockchain import *
from datetime import datetime
from datetime import timedelta
import copy

testDatetime = datetime.now() + timedelta(days=7)

testVenue1 = Venue("Regenstein", "Chicago, IL")
testEvent1a = testVenue1.createEvent("Maroon 5", testDatetime, "this is a band")
testEvent1b = testVenue1.createEvent("Maroon 5", testDatetime, "this is a band")
testEvent1c = testVenue1.createEvent("Maroon 5", testDatetime, "this is a band")
testEvent1d = testVenue1.createEvent("Maroon 5", testDatetime, "this is a band")
testEvent1e = testVenue1.createEvent("Maroon 5", testDatetime, "this is a band")
testEvent1f = testVenue1.createEvent("Maroon 5", testDatetime, "this is a band")
testEvent1g = testVenue1.createEvent("Maroon 5", testDatetime, "this is a band")
testEvent1h = testVenue1.createEvent("Maroon 5", testDatetime, "this is a band")
testEvent1i = testVenue1.createEvent("Maroon 5", testDatetime, "this is a band")
testEvent1j = testVenue1.createEvent("Another band", testDatetime, "this is a band")

testVenue2 = Venue("Washington Square Park", "New York City, New York")
testEvent2a = testVenue2.createEvent("Zero 7", testDatetime, "this is also a band")
testEvent2b = testVenue2.createEvent("Zero 7", testDatetime, "this is also a band")
testEvent2c = testVenue2.createEvent("Zero 7", testDatetime, "this is also a band")
testEvent2d = testVenue2.createEvent("Zero 7", testDatetime, "this is also a band")
testEvent2e = testVenue2.createEvent("Zero 7", testDatetime, "this is also a band")
testEvent2f = testVenue2.createEvent("Zero 7", testDatetime, "this is also a band")
testEvent2g = testVenue2.createEvent("Zero 7", testDatetime, "this is also a band")
testEvent2h = testVenue2.createEvent("Zero 7", testDatetime, "this is also a band")
testEvent2i = testVenue2.createEvent("Zero 7", testDatetime, "this is also a band")
testEvent2j = testVenue2.createEvent("Zero 7", testDatetime, "this is also a band")

testVenue3 = Venue("The314", "Space")
testEvent3a = testVenue3.createEvent("Informative Talk 1", testDatetime, "lecture")
testEvent3b = testVenue3.createEvent("Informative Talk 2", testDatetime, "lecture")

testVenue4 = Venue("The201", "Space")
testEvent4a = testVenue4.createEvent("Informative Talk 3", testDatetime, "lecture")
testEvent4b = testVenue4.createEvent("Informative Talk 4", testDatetime, "lecture")
testEvent4c = testVenue4.createEvent("Informative Talk 5", testDatetime, "lecture")
testEvent4d = testVenue4.createEvent("Informative Talk 6", testDatetime, "lecture")
testEvent4e = testVenue4.createEvent("Informative Talk 7", testDatetime, "lecture")
testEvent4f = testVenue4.createEvent("Informative Talk 8", testDatetime, "lecture")
testEvent4g = testVenue4.createEvent("Informative Talk 9", testDatetime, "lecture")
testEvent4h = testVenue4.createEvent("Informative Talk 10", testDatetime, "lecture")

testVenue5 = Venue("The196", "Space")
testEvent5a = testVenue5.createEvent("Informative Talk 11", testDatetime, "lecture")
testEvent5b = testVenue5.createEvent("Informative Talk 12", testDatetime, "lecture")

testVenue6 = Venue("The Tag", "NLTKLand")
testEvent6a = testVenue6.createEvent("Tag ID Test", testDatetime, "Ethan Reeder goes to CSIL with Rory Friedman")
testEvent6b = testVenue6.createEvent("Tag ID Test", testDatetime, "Ethan Reeder goes to CSIL with Zarek Drozda")
testEvent6c = testVenue6.createEvent("Tag ID Test", testDatetime, "Ethan Reeder goes to CSIL")
testEvent6d = testVenue6.createEvent("Tag ID Test", testDatetime, "Rory Friedman goes to CSIL with Ethan Reeder")
testEvent6e = testVenue6.createEvent("Tag ID Test", testDatetime, "Rory Friedman goes to CSIL with Zarek Drozda")
testEvent6f = testVenue6.createEvent("Tag ID Test", testDatetime, "Rory Friedman goes to CSIL")
testEvent6g = testVenue6.createEvent("Tag ID Test", testDatetime, "Zarek Drozda goes to CSIL with Rory Friedman")
testEvent6h = testVenue6.createEvent("Tag ID Test", testDatetime, "Zarek Drozda goes to CSIL with Ethan Reeder")
testEvent6i = testVenue6.createEvent("Tag ID Test", testDatetime, "Zarek Drozda goes to CSIL")
testEvent6j = testVenue6.createEvent("Tag ID Test", testDatetime, "Ethan Reeder goes to CSIL with his cat")
testEvent6k = testVenue6.createEvent("Tag ID Test", testDatetime, "Ethan Reeder goes to CSIL with Anders")
testEvent6l = testVenue6.createEvent("Tag ID Test", testDatetime, "Rory Friedman goes to CSIL with his cat")
testEvent6m = testVenue6.createEvent("Tag ID Test", testDatetime, "Rory Friedman goes to CSIL with Anders")
testEvent6n = testVenue6.createEvent("Tag ID Test", testDatetime, "Zarek Drozda goes to CSIL with his cat")
testEvent6o = testVenue6.createEvent("Tag ID Test", testDatetime, "Zarek Drozda goes to CSIL with Anders")
testEvent6p = testVenue6.createEvent("Tag ID Test", testDatetime, "Zarek Drozda goes to CSIL with Anders and Ethan Reeder")
testEvent6q = testVenue6.createEvent("Tag ID Test", testDatetime, "Zarek Drozda goes to CSIL with Anders. Ethan Reeder plays the drums")
testEvent6r = testVenue6.createEvent("Tag ID Test", testDatetime, "Zarek Drozda goes to CSIL without Ethan Reeder")

# To Note - simple weights are introduced to allow for proper testing of preferences
testUser1 = User("Hello", "World", "abcedfg@uchicago.edu")
testUser1.location_pref.update({"New York City, New York":5, "Chicago, IL":1})

testUser2 = User("John", "Doe", "johndoe@uchicago.edu")
testUser2.location_pref.update({"New York City, New York":7, "Chicago, IL":6})
testUser2.venue_pref.update({"Regenstein":2, "Washington Square Park":1})

testUser3 = User("Jane", "Doe", "janedoe@uchicago.edu")
testUser3.location_pref.update({"New York City, New York":5, "Chicago, IL":6})
testUser3.venue_pref.update({"Regenstein":1, "Washington Square Park":1})

testUser4 = User("Jack", "Inthebox", "jitb@gmail.com")
testUser4.venue_pref.update({"The314":10, "The201":5, "The196":0})

testUser5 = User("Jill", "Aroundthehill", "jath@gmail.com")
testUser5.venue_pref.update({"The314":0, "The201":5, "The196":10})

testUser6 = User("Julien", "Neiluj", "jn@gmail.com")
testUser6.description_pref.update({"Ethan Reeder":100, "Zarek Drozda":5, "Rory Friedman":50, "CSIL":10})

def test_eventslistsize():
	"""
	Make sure everything works properly if inputs are correct, and explore picks out 10 events
	"""
	assert len(testUser1.explore()) == 10

def test_location_pref1():
	""" Test recommendation agreement with user preferences for location """
	eventsList = testUser2.explore()
	assert testEvent2a in eventsList
	assert testEvent2b in eventsList
	assert testEvent2c in eventsList
	assert testEvent2d in eventsList
	assert testEvent2e in eventsList
	assert testEvent2f in eventsList
	assert testEvent2g in eventsList
	assert testEvent2h in eventsList
	assert testEvent2i in eventsList
	assert testEvent2j in eventsList
	assert testEvent1a not in eventsList
	assert testEvent1i not in eventsList

def test_location_pref2():
	""" Similar to above but using a different equivalence class to ensure full testing """
	eventsList = testUser3.explore()
	assert testEvent1a in eventsList
	assert testEvent1b in eventsList
	assert testEvent1c in eventsList
	assert testEvent1d in eventsList
	assert testEvent1e in eventsList
	assert testEvent1f in eventsList
	assert testEvent1g in eventsList
	assert testEvent1h in eventsList
	assert testEvent1i in eventsList
	assert testEvent1j in eventsList
	assert testEvent2a not in eventsList
	assert testEvent2b not in eventsList

def test_venue_pref1():
	""" Test recommendation agreement with user preferences for venue """
	eventsList = testUser4.explore()
	assert testEvent3a in eventsList
	assert testEvent3b in eventsList
	assert testEvent4a in eventsList
	assert testEvent4b in eventsList
	assert testEvent4c in eventsList
	assert testEvent4d in eventsList
	assert testEvent4e in eventsList
	assert testEvent4f in eventsList
	assert testEvent4g in eventsList
	assert testEvent4g in eventsList

def test_venue_pref2():
	""" Similar to above but using a different equivalence class to ensure full testing """
	eventsList = testUser5.explore()
	assert testEvent4a in eventsList
	assert testEvent4b in eventsList
	assert testEvent4c in eventsList
	assert testEvent4d in eventsList
	assert testEvent4e in eventsList
	assert testEvent4f in eventsList
	assert testEvent4g in eventsList
	assert testEvent4g in eventsList
	assert testEvent5a in eventsList
	assert testEvent5b in eventsList

def test_description_pref():
	""" Test recommendation agreement with user preferences for various tags """
	eventsList = testUser6.explore()
	assert testEvent6a in eventsList
	assert testEvent6b in eventsList
	assert testEvent6c in eventsList
	assert testEvent6d in eventsList
	assert testEvent6e not in eventsList
	assert testEvent6f not in eventsList
	assert testEvent6g not in eventsList
	assert testEvent6h in eventsList
	assert testEvent6i not in eventsList
	assert testEvent6j in eventsList
	assert testEvent6k in eventsList
	assert testEvent6l not in eventsList
	assert testEvent6m not in eventsList
	assert testEvent6n not in eventsList
	assert testEvent6o not in eventsList
	assert testEvent6p in eventsList
	assert testEvent6q in eventsList
	assert testEvent6r in eventsList
