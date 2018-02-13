from back_end.Admit01_Blockchain import *

first_id = Trackers.getNextUserVenueID()
next_id = Trackers.getNextUserVenueID()

first_event_id = Trackers.getNextEventID()
next_event_id = Trackers.getNextEventID()

def test_firstuservenueid():
    assert first_id == 0

def test_uservenueincrement():
    assert next_id == first_id + 1

def test_firsteventid():
    assert first_event_id == 0

def test_eventincrement():
    assert next_event_id == first_event_id + 1
