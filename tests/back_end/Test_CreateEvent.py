from blockchain.Admit01_Blockchain import *
from datetime import datetime
from datetime import timedelta

# Note: desc (event description) is NOT a mandatory field, can be "" or None
# Note: name is a mandatory field
# Note: datetime must be future-dated; you can't create an event in the past

valid_datetime = datetime.now() + timedelta(days=7) # one week from now
invalid_datetime = datetime.now() - timedelta(days=7) # one week ago

venue1 = Venue("Wrigley Field", "Chicago, IL")

event1 = venue1.createEvent("Lady Gaga", valid_datetime, "Stadium world tour") # success
event2 = venue1.createEvent("", valid_datetime, "Marlins vs. Red Sox") # failure
event3 = venue1.createEvent("Hamilton", invalid_datetime, "2016 Tony winner") # failure

def test_allvalid():
    """ Future-dated Event with non-empty name should be created successfully """
    assert (event1.id is not None and
            event1.name == "Lady Gaga" and
            event1.datetime == valid_datetime and
            event1.desc == "Stadium world tour")

def test_indictionary():
	""" Event should be created and stored in a Venue's events dictionary """
	assert (event1.id in venue1.events.keys())

def test_indictionary3():
	""" Event should not be created and stored in a Venue's events dictionary """
	assert len(venue1.events) == 1

def test_venueattribute1():
	""" Event's venue attribute should match the venue creating it """
	assert (event1.venue == venue1)

def test_badname():
    """ Nameless Event should not construct """
    assert event2 is None

def test_baddatetime():
    """ Past-dated Event should not construct """
    assert event3 is None
