from blockchain.Admit01_Blockchain import *

first_id = Trackers.getNextUserVenueID()
next_id = Trackers.getNextUserVenueID()

first_event_id = Trackers.getNextEventID()
next_event_id = Trackers.getNextEventID()

venue1 = Venue("Apollo Theater", "Chicago, IL")
venue2 = Venue("American Airlines Arena", "Miami, FL")
venue3 = Venue("Madison Square Garden", "New York, NY")

def test_firstuservenueid():
    assert first_id == 0

def test_uservenueincrement():
    assert next_id == first_id + 1

def test_firsteventid():
    assert first_event_id == 0

def test_eventincrement():
    assert next_event_id == first_event_id + 1

def test_venueexists():
    assert Trackers.venueExists(venue1.id)

def test_venuedoesnotexist():
    assert not Trackers.venueExists(venue3.id + 23)

def test_badvenue():
    assert not Trackers.venueExists(None)
