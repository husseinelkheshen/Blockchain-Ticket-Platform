from blockchain.Admit01_Blockchain import *
from datetime import datetime
from datetime import timedelta
import copy

valid_datetime1 = datetime.now() + timedelta(days=5)
valid_datetime2 = datetime.now() + timedelta(days=7)
valid_datetime3 = datetime.now() + timedelta(days=1)
valid_datetime4 = datetime.now() + timedelta(days=3)

# initialize two venues
venue1 = Venue("Apollo Theater", "Chicago, IL")
venue2 = Venue("Adrienne Arsht Center", "Miami, FL")

# initialize events for venue1
event1 = Event("Ellen DeGeneres", valid_datetime1, "Stand-up comedy show")
event1.venue = venue1
venue1.events[event1.id] = (event1, copy.deepcopy(event1.blockchain))

event2 = Event("Lana Del Rey", valid_datetime2, "Pop music concert")
event2.venue = venue1
venue1.events[event2.id] = (event2, copy.deepcopy(event2.blockchain))

# initialize events for venue2
event3 = Event("Lady Gaga", valid_datetime3, "Pop artist world tour")
event3.venue = venue2
venue2.events[event3.id] = (event3, copy.deepcopy(event3.blockchain))

event4 = Event("Lana Del Rey", valid_datetime4, "Pop music concert")
event4.venue = venue2
venue2.events[event4.id] = (event4, copy.deepcopy(event4.blockchain))

def test_allevents():
    """ A generic call to search() should return all Events """
    search_results = search()
    assert len(search_results) == 4
    for event in [event1, event2, event3, event4]:
        assert event in search_results
