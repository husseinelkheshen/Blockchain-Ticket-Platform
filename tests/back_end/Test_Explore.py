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

testVenue3 = Venue("The314", "Space")
testEvent12 = testVenue3.createEvent("Informative Talk 1", testDatetime, "lecture")
testEvent13 = testVenue3.createEvent("Informative Talk 2", testDatetime, "lecture")

testVenue4 = Venue("The201", "Space")
testEvent14 = testVenue4.createEvent("Informative Talk 3", testDatetime, "lecture")
testEvent15 = testVenue4.createEvent("Informative Talk 4", testDatetime, "lecture")
testEvent16 = testVenue4.createEvent("Informative Talk 5", testDatetime, "lecture")
testEvent17 = testVenue4.createEvent("Informative Talk 6", testDatetime, "lecture")
testEvent18 = testVenue4.createEvent("Informative Talk 7", testDatetime, "lecture")
testEvent19 = testVenue4.createEvent("Informative Talk 8", testDatetime, "lecture")
testEvent20 = testVenue4.createEvent("Informative Talk 9", testDatetime, "lecture")
testEvent21 = testVenue4.createEvent("Informative Talk 10", testDatetime, "lecture")

testVenue5 = Venue("The196", "Space")
testEvent22 = testVenue5.createEvent("Informative Talk 11", testDatetime, "lecture")
testEvent23 = testVenue5.createEvent("Informative Talk 12", testDatetime, "lecture")

testVenue6 = Venue("The Tag", "NLTKLand")
testEvent24 = testVenue6.createEvent("Tag ID Test 1", testDatetime, "Ethan Reeder goes to CSIL")
testEvent25 = testVenue6.createEvent("Tag ID Test 1", testDatetime, "Ethan Reeder goes to CSIL")
testEvent26 = testVenue6.createEvent("Tag ID Test 1", testDatetime, "Ethan Reeder goes to CSIL")
testEvent27 = testVenue6.createEvent("Tag ID Test 1", testDatetime, "Ethan Reeder goes to CSIL")
testEvent28 = testVenue6.createEvent("Tag ID Test 1", testDatetime, "Ethan Reeder goes to CSIL")
testEvent29 = testVenue6.createEvent("Tag ID Test 1", testDatetime, "Ethan Reeder goes to CSIL")
testEvent30 = testVenue6.createEvent("Tag ID Test 1", testDatetime, "Ethan Reeder goes to CSIL")
testEvent31 = testVenue6.createEvent("Tag ID Test 1", testDatetime, "Ethan Reeder goes to CSIL")
testEvent32 = testVenue6.createEvent("Tag ID Test 1", testDatetime, "Ethan Reeder goes to CSIL")
testEvent33 = testVenue6.createEvent("Tag ID Test 1", testDatetime, "Ethan Reeder goes to CSIL")
testEvent34 = testVenue6.createEvent("Tag ID Test 1", testDatetime, "Ethan Reeder goes to CSIL")
testEvent35 = testVenue6.createEvent("Tag ID Test 1", testDatetime, "Ethan Reeder goes to CSIL")
testEvent36 = testVenue6.createEvent("Tag ID Test 1", testDatetime, "Ethan Reeder goes to CSIL")
testEvent37 = testVenue6.createEvent("Tag ID Test 1", testDatetime, "Ethan Reeder goes to CSIL")
testEvent38 = testVenue6.createEvent("Tag ID Test 1", testDatetime, "Ethan Reeder goes to CSIL")
testEvent39 = testVenue6.createEvent("Tag ID Test 1", testDatetime, "Ethan Reeder goes to CSIL")
testEvent40 = testVenue6.createEvent("Tag ID Test 1", testDatetime, "Ethan Reeder goes to CSIL")
testEvent41 = testVenue6.createEvent("Tag ID Test 1", testDatetime, "Ethan Reeder goes to CSIL")
testEvent42 = testVenue6.createEvent("Tag ID Test 1", testDatetime, "Ethan Reeder goes to CSIL")
testEvent43 = testVenue6.createEvent("Tag ID Test 1", testDatetime, "Ethan Reeder goes to CSIL")

# To Note - simple weights are introduced to allow for proper testing of preferences
testUser1 = User("Hello", "World", "abcedfg@uchicago.edu")
testUser1.location_pref.update({"New York City, New York":5, "Chicago, IL":1})

# testUser2 = User("Abraham", "Lincoln", "fourscore@uchicago.edu")

testUser3 = User("John", "Doe", "johndoe@uchicago.edu")
testUser3.location_pref.update({"New York City, New York":7, "Chicago, IL":6})
testUser3.venue_pref.update({"Regenstein":1, "Washington Square Park":1})

testUser4 = User("Jane", "Doe", "janedoe@uchicago.edu")
testUser4.location_pref.update({"New York City, New York":5, "Chicago, IL":6})
testUser4.venue_pref.update({"Regenstein":1, "Washington Square Park":1})

testUser5 = User("Jack", "Inthebox", "jitb@gmail.com")
testUser5.venue_pref.update({"The314":10, "The201":5, "The196":0})

testUser6 = User("Jill", "Aroundthehill", "jath@gmail.com")
testUser6.venue_pref.update({"The314":0, "The201":5, "The196":10})

def test_eventslistsize():
	"""
	Make sure everything works properly if inputs are correct, and explore picks out 10 events
	"""
	assert len(testUser1.explore()) == 10

# def test_addtags():
# 	"""
# 	Make sure tags are being added to user's preferences based on each suggested event
# 	"""
# 	testUser2.explore()
# 	assert "New York City, New York" in testUser2.preferences
# 	assert "Chicago, IL" in testUser2.preferences
# 	assert "Regenstein" in testUser2.preferences
# 	assert "Washington Square Park" in testUser2.preferences
# 	assert "Maroon 5" in testUser2.preferences
# 	assert "Zero 7" in testUser2.preferences

def test_location_pref1():
	"""
	Test recommendation agreement with user preferences for location
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

def test_location_pref2():
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

def test_venue_pref1():
	eventsList = testUser5.explore()
	assert testEvent12 in eventsList
	assert testEvent13 in eventsList
	assert testEvent14 in eventsList
	assert testEvent15 in eventsList
	assert testEvent16 in eventsList
	assert testEvent17 in eventsList
	assert testEvent18 in eventsList
	assert testEvent19 in eventsList
	assert testEvent20 in eventsList
	assert testEvent21 in eventsList

def test_venue_pref2():
	eventsList = testUser6.explore()
	assert testEvent14 in eventsList
	assert testEvent15 in eventsList
	assert testEvent16 in eventsList
	assert testEvent17 in eventsList
	assert testEvent18 in eventsList
	assert testEvent19 in eventsList
	assert testEvent20 in eventsList
	assert testEvent21 in eventsList
	assert testEvent22 in eventsList
	assert testEvent23 in eventsList

def test_description_pref1():
	pass

def test_description_pref2():
	pass
