from blockchain.Admit01_Blockchain import *
from datetime import timedelta

valid_date = date.datetime.now() + timedelta(days = 7)

testSeat1 = Seat("Cheap Seats", "C", 5)

venue1 = Venue("Wrigley Field", "Chicago, IL")
venue1.createEvent("Lady Gaga", valid_date, "Stadium world tour")
venue1.createEvent("Chicago Bulls", valid_date, "Tanking season")

def test_no_event():
    """ Tests a function call with no Event """
    assert venue1.venueTickets(None) is None

def test_negative_event_value():
    """ Tests a function call with impossible Event ID """
    assert venue1.venueTickets(-5) is None

def test_nonexistent_event_value():
    """ Tests a function call with Event ID that doesn't exist"""
    assert venue1.venueTickets(2) is None

def test_no_tickets():
    """ Tests an Event with no tickets """
    assert venue1.venueTickets(0) is None

venue1.createTicket(venue1.events[0][0], 50, testSeat1)

def test_one_ticket():
    """ Tests an Event with one ticket """
    assert venue1.venueTickets(0) is not None