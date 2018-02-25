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
    """ An empty call to search() should return all Events """
    search_results = search()
    assert len(search_results) == 4
    assert event1 in search_results
    assert event2 in search_results
    assert event3 in search_results
    assert event4 in search_results

def test_textsearch():
    """ Run a search using a text-only query """
    search_results = search(text='pop music')
    assert len(search_results) == 3
    assert event2 in search_results
    assert event3 in search_results
    assert event4 in search_results

def test_locationsearch():
    """ Run a search by location """
    search_results = search(text='miami')
    assert len(search_results) == 2
    assert event3 in search_results
    assert event4 in search_results

def test_compoundtextsearch():
    """ Run a search with description and location keywords """
    search_results = search_results = search(text='pop music miami')
    assert len(search_results) == 3
    assert event2 in search_results
    assert event3 in search_results
    assert event4 in search_results

def test_compoundtextsearch():
    """ Run a search with venue keywords """
    search_results = search_results = search(text='apollo theater')
    assert len(search_results) == 2
    assert event1 in search_results
    assert event2 in search_results

def test_uselessparameter():
    """ A search with date range but no datetime will ignore the range """
    search_results = search_results = search(text='pop', date_range=2)
    assert len(search_results) == 3
    assert event2 in search_results
    assert event3 in search_results
    assert event4 in search_results

def test_datefilter():
    """ Run a search on a single date """
    search_results = search(datetime=valid_datetime1)
    assert len(search_results) == 1
    assert event1 in search_results

def test_daterange():
    """ Run a search on a date range """
    search_results = search(datetime=valid_datetime1, date_range=2)
    assert len(search_results) == 2
    assert event1 in search_results
    assert event2 in search_results

def test_compoundsearch():
    """ Run a search with all parameters filled """
    search_results = search('ellen', valid_datetime1 - timedelta(days=1), 4)
    assert len(search_results) == 1
    assert event1 in search_results

def test_noresults():
    """ Run a search that returns no Events """
    search_results = search('hamilton new york')
    assert len(search_results) == 0
