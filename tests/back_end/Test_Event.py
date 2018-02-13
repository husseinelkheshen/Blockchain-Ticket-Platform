from back_end.Admit01_Blockchain import *
from datetime import datetime
from datetime import timedelta

# Note: desc (event description) is NOT a mandatory field, can be "" or None
# Note: name is a mandatory field
# Note: datetime must be future-dated; you can't create an event in the past

valid_datetime = datetime.now() + timedelta(days=7) # one week from now
invalid_datetime = datetime.now() - timedelta(days=7) # one week ago

event1 = Event("Lady Gaga", valid_datetime, "Stadium world tour") # success
event2 = Event("", valid_datetime, "Marlins vs. Red Sox") # failure
event3 = Event("Hamilton", invalid_datetime, "2016 Tony winner") # failure

def test_allvalid():
    """ Future-dated Event with non-empty name should construct successfully """
    assert (event1.name == "Lady Gaga" and
            event1.datetime == valid_datetime and
            event1.desc == "Stadium world tour")

def test_badname():
    """ Nameless Event should not construct """
    assert (event2.name == None and
            event2.datetime == None and
            event2.desc == None)

def test_baddatetime():
    """ Past-dated Event should not construct """
    assert (event3.name == None and
            event3.datetime == None and
            event3.desc == None)
