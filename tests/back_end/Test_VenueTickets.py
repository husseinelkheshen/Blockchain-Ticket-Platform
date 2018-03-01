from blockchain.Admit01_Blockchain import *
from datetime import timedelta

valid_date = date.datetime.now() + timedelta(days = 7)

testSeat1 = Seat("Cheap Seats", "C", 5)
testSeat2 = Seat("Cheap Seats", "C", 6)

venue1 = Venue("Wrigley Field", "Chicago, IL")
venue1.createEvent("Chicago Bulls", valid_date, "Tanking season")

user1 = User("Ethan", "Reeder", "er@example.com")

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

def test_one_ticket():
    """ Tests an Event with one ticket """
    venue1.createTicket(venue1.events[0][0], 50, testSeat1)
    assert venue1.venueTickets(0) == [0]

def test_two_tickets():
    """ Tests an Event with two ticket """
    venue1.createTicket(venue1.events[0][0], 30, testSeat2)
    assert venue1.venueTickets(0) == [0, 1]


def test_post_transaction():
    """ Tests an Event after the Venue sells a ticket """
    venue1.events[0][0].tickets[0].listTicket(0, venue1.id)
    user1.buyTicket(venue1.events[0][0].tickets[0])
    assert venue1.venueTickets(0) == [1]
