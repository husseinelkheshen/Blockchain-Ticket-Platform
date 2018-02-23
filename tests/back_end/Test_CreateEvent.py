from blockchain.Admit01_Blockchain import *
from datetime import datetime
from datetime import timedelta

# Note: desc (event description) is NOT a mandatory field, can be "" or None
# Note: name is a mandatory field
# Note: datetime must be future-dated; you can't create an event in the past

valid_datetime = datetime.now() + timedelta(days=7) # one week from now
invalid_datetime = datetime.now() - timedelta(days=7) # one week ago

event1 = createEvent("Lady Gaga", valid_datetime, "Stadium world tour") # success
event2 = createEvent("Adele", valid_datetime, "New album event") # success
event3 = createEvent("", valid_datetime, "Marlins vs. Red Sox") # failure
event4 = createEvent("Hamilton", invalid_datetime, "2016 Tony winner") # failure

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

def test_badname():
    """ Nameless Event should not be created """
    assert (event3.id is None and
            event3.name is None and
            event3.datetime is None and
            event3.desc is None)

def test_baddatetime():
    """ Past-dated Event should not be created """
    assert (event4.id is None and
            event4.name is None and
            event4.datetime is None and
            event4.desc is None)





