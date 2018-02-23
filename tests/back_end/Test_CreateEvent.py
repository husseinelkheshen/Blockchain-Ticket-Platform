from blockchain.Admit01_Blockchain import *
from datetime import datetime
from datetime import timedelta

# Note: desc (event description) is NOT a mandatory field, can be "" or None
# Note: name is a mandatory field
# Note: datetime must be future-dated; you can't create an event in the past

valid_datetime = datetime.now() + timedelta(days=7) # one week from now
invalid_datetime = datetime.now() - timedelta(days=7) # one week ago

venue1 = Venue("Wrigley Field", "Chicago, IL")
venue2 = Venue("Madison Square Garden", "New York, NY")

event1 = venue1.createEvent("Lady Gaga", valid_datetime, "Stadium world tour") # success
event2 = venue2.createEvent("Adele", valid_datetime, "New album event") # success
event3 = venue1.createEvent("", valid_datetime, "Marlins vs. Red Sox") # failure
event4 = venue2.createEvent("Hamilton", invalid_datetime, "2016 Tony winner") # failure


def test_allvalid():
    """ Future-dated Event with non-empty name should be created successfully """
    assert (event1.id is not None and
            event1.name == "Lady Gaga" and
            event1.datetime == valid_datetime and
            event1.desc == "Stadium world tour")

def test_allvalid2():
    """ Future-dated Event with non-empty name should be created successfully """
    assert (event2.id is not None and
            event2.name == "Adele" and
            event2.datetime == valid_datetime and
            event2.desc == "New album event")

def test_indictionary():
	""" Event should be created and stored in a Venue's events dictionary """
	assert (venue1.events.has_key(event1.id) == True)

def test_indictionary2():
	""" Event should be created and stored in a Venue's events dictionary """
	assert (venue2.events.has_key(event2.id) == True)

def test_indictionary3():
	""" Event should not be created and stored in a Venue's events dictionary """
	assert (venue1.events.has_key(event3.id) == False)

def test_indictionary4():
	""" Event should be not created and stored in a Venue's events dictionary """
	assert (venue2.events.has_key(event4.id) == False)

def test_venueattribute1():
	





