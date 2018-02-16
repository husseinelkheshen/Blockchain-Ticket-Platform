from blockchain.Admit01_Blockchain import *
from datetime import datetime
from datetime import timedelta
import copy

valid_datetime = datetime.now() + timedelta(days=7) # one week from now
venue1 = Venue("Wrigley Field", "Chicago, IL")
event1 = Event("Lady Gaga", valid_datetime, "Stadium world tour")
event1.venue = venue1
seat1 = Seat("Floor Center", "G", 23)
seat2 = Seat("Upper Center", "H", 58)

venue1.events[event1.id] = (event1, copy.deepcopy(event1.blockchain))

venue1.createTicket(venue1.events[event1.id][0], 550, seat1)    # success
venue1.createTicket(venue1.events[event1.id][0], 365, seat1)    # failure
venue1.createTicket(venue1.events[event1.id][0], 365, None)     # failure
venue1.createTicket(venue1.events[event1.id][0], -5, seat2)     # failure
venue1.createTicket(None, 700, seat2)     # failure

most_recent_event_block = venue1.events[event1.id][0].blockchain.blocks[-1]
most_recent_venue_block = venue1.events[event1.id][1].blocks[-1]

def test_cloning():
    """ Make sure that both blockchains are in sync after update """
    assert most_recent_event_block == most_recent_venue_block

def test_duplicate():
    """ Make sure that the duplicate Ticket is not posted """
    assert len(most_recent_event_block.data) == 1

def test_noSeat():
    """ Make sure that the Ticket with no Seat is not posted """
    assert len(most_recent_event_block.data) == 1

def test_noEvent():
    """ Make sure that the Ticket with no Seat is not posted """
    assert len(most_recent_event_block.data) == 1

def test_negativeValue():
    """ Make sure that the Ticket with negative value is not posted """
    assert len(most_recent_event_block.data) == 1

def test_noValue():
    """ Make sure that the Ticket with no value is not posted  """
    assert len(most_recent_event_block.data) == 1

def test_listing():
    """ Make sure that only the correct Ticket is listed under the Event """
    assert len(venue1.events[event1.id][0].tickets) == 1
    assert venue1.events[event1.id][0].tickets[0].face_value == 550

def test_ownership():
    """ Make sure that the Venue is the current owner of the Ticket """
    assert most_recent_event_block.data[0].target == venue1.id

def test_tickethistory():
    """ Make sure that the Ticket's history reflects the update """
    b = most_recent_event_block
    latest_history = (b.index, b.hash)
    assert venue1.events[event1.id][0].tickets[0].history[-1] == latest_history
