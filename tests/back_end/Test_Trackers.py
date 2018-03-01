from blockchain.Admit01_Blockchain import *

first_id = Trackers.getNextUserVenueID()
next_id = Trackers.getNextUserVenueID()

first_event_id = Trackers.getNextEventID()
next_event_id = Trackers.getNextEventID()

venue1 = Venue("Apollo Theater", "Chicago, IL")
venue2 = Venue("American Airlines Arena", "Miami, FL")
venue3 = Venue("Madison Square Garden", "New York, NY")

user1 = User("Hayden", "Mans", "hm@example.com")

def test_firstuservenueid():
    """ Test that id generation starts at 0 """
    assert first_id == 0

def test_uservenueincrement():
    """ Test that venue/user id generator increments by 1 """
    assert next_id == 1

def test_firsteventid():
    """
    Test that id generation for events is independent of
    id generation for venues/users
    """
    assert first_event_id == 0

def test_eventincrement():
    """ Test that event id generator increments by 1 """
    assert next_event_id == first_event_id + 1

def test_venueexists():
    """ Tracker can retrieve a venue by its id """
    assert Trackers.getVenue(venue1.id) == venue1

def test_venuedoesnotexist():
    """ Tracker returns None for unregistered venue id """
    assert Trackers.getVenue(venue3.id + 23) is None

def test_badvenue():
    """ Tracker returns None for NoneType input """
    assert Trackers.getVenue(None) is None

def test_userexists():
    """ Tracker can retrieve a user by its id """
    assert Trackers.getUser(user1.id) == user1

def test_userdoesnotexist():
    """ Tracker returns None for unregistered user id """
    assert Trackers.getUser(user1.id + 23) is None

def test_baduser():
    """ Tracker returns None for NoneType input """
    assert Trackers.getUser(None) is None
