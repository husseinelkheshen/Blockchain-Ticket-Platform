from blockchain.Admit01_Blockchain import *
from datetime import timedelta

valid_date = date.datetime.now() + timedelta(days = 7)

testSeat1 = Seat("Cheap Seats", "C", 5)
testSeat2 = Seat("Cheap Seats", "B", 5)
testSeat3 = Seat("Cheap Seats", "C", 6)
testSeat4 = Seat("Dank Seats", "C", 5)

venue1 = Venue("Wrigley Field", "Chicago, IL")
venue1.createEvent("Lady Gaga", valid_date, "Stadium world tour")

venue1.createTicket(venue1.events[0][0], 50, testSeat1)
venue1.createTicket(venue1.events[0][0], 70, testSeat2)
venue1.createTicket(venue1.events[0][0], 90, testSeat3)
venue1.createTicket(venue1.events[0][0], 30, testSeat4)

user1 = User("Ethan", "Reeder", "er@example.com")

def test_no_event():
    """ Tests a ManageTicket call with no Event to check for failure """
    assert (not venue1.manageTickets(None, 80, "Cheap Seats", "C", 5) and
            venue1.events[0][0].tickets[0].list_price == 50)

def test_no_price():
    """ Tests a ManageTicket call with no new price to check for failure """
    assert (not venue1.manageTickets(venue1.events[0][0], None, "Cheap Seats", "C", 5) and
            venue1.events[0][0].tickets[0].list_price == 50)

def test_invalid_price():
    """ Tests a ManageTicket call with an invalid price to check for failure """
    assert (not venue1.manageTickets(venue1.events[0][0], -30, "Cheap Seats", "C", 5) and
            venue1.events[0][0].tickets[0].list_price == 50)

def test_invalid_row():
    """ Tests a ManageTicket call where seat is specified but row is not to check for failure """
    assert (not venue1.manageTickets(venue1.events[0][0], 80, "Cheap Seats", None, 5) and
            venue1.events[0][0].tickets[0].list_price == 50)

def test_invalid_section():
    """ Tests a ManageTicket call where row is specified but section is not to check for failure """
    assert (not venue1.manageTickets(venue1.events[0][0], 80, None, "C", 5) and
            venue1.events[0][0].tickets[0].list_price == 50)

def test_valid_seat():
    """ Tests a ManageTicket call with correct parameters for changing the price of one ticket"""
    assert (venue1.manageTickets(venue1.events[0][0], 80, "Cheap Seats", "C", 5) and
            venue1.events[0][0].tickets[0].list_price == 80 and
            venue1.events[0][0].tickets[1].list_price == 70 and
            venue1.events[0][0].tickets[2].list_price == 90 and
            venue1.events[0][0].tickets[3].list_price == 30)

def test_valid_row():
    """ Tests a ManageTicket call with correct parameters for changing the price of one row of tickets"""
    assert (venue1.manageTickets(venue1.events[0][0], 100, "Cheap Seats", "C", None) and
            venue1.events[0][0].tickets[0].list_price == 100 and
            venue1.events[0][0].tickets[1].list_price == 70 and
            venue1.events[0][0].tickets[2].list_price == 100 and
            venue1.events[0][0].tickets[3].list_price == 30)

def test_valid_section():
    """ Tests a ManageTicket call with correct parameters for changing the price of one section of tickets"""
    assert (venue1.manageTickets(venue1.events[0][0], 120, "Cheap Seats", None, None) and
            venue1.events[0][0].tickets[0].list_price == 120 and
            venue1.events[0][0].tickets[1].list_price == 120 and
            venue1.events[0][0].tickets[2].list_price == 120 and
            venue1.events[0][0].tickets[3].list_price == 30)

def test_valid_tickets():
    """ Tests a ManageTicket call with correct parameters for changing the price of all Venue tickets"""
    assert (venue1.manageTickets(venue1.events[0][0], 150, None, None, None) and
            venue1.events[0][0].tickets[0].list_price == 150 and
            venue1.events[0][0].tickets[1].list_price == 150 and
            venue1.events[0][0].tickets[2].list_price == 150 and
            venue1.events[0][0].tickets[3].list_price == 150)

def test_venue_owned():
    """ Tests a ManageTicket to ensure it doesn't affect non-venue owned tickets """

    venue1.events[0][0].tickets[3].listTicket(0, venue1.id)
    user1.buyTicket(venue1.events[0][0].tickets[3])

    assert (venue1.manageTickets(venue1.events[0][0], 200, None, None, None) and
            venue1.events[0][0].tickets[0].list_price == 200 and
            venue1.events[0][0].tickets[1].list_price == 200 and
            venue1.events[0][0].tickets[2].list_price == 200 and
            venue1.events[0][0].tickets[3].list_price == 0)
