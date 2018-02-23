from blockchain.Admit01_Blockchain import *
import datetime as date

valid_date = date.datetime.now() + timedelta(days = 7)

testSeat1 = Seat("Cheap Seats", "C", 5)
testSeat2 = Seat("Cheap Seats", "B", 5)
testSeat3 = Seat("Cheap Seats", "C", 6)

venue1 = Venue("Wrigley Field", "Chicago, IL")
event1 = Event("Lady Gaga", valid_datetime, "Stadium world tour")
event1.venue = venue1

ticket1 = Ticket(testEvent1, 50, testSeat1)
ticket2 = Ticket(testEvent1, 70, testSeat2)
ticket3 = Ticket(testEvent1, 90, testSeat3)

def test_no_event():
    """ You can't manage Tickets if the event is not specified """
    assert (not venue1.manageTickets(None, 80, "Cheap Seats", "C", 5) and
            ticket1.list_price == 50)

def test_no_price():
    """ TODO """
    assert (not venue1.manageTickets(event1, None, "Cheap Seats", "C", 5) and
            ticket1.list_price == 50)

def test_invalid_price():
    """ TODO """
    assert (not venue1.manageTickets(event1, -30, "Cheap Seats", "C", 5) and
            ticket1.list_price == 50)

def test_invalid_row():
    """ TODO """
    assert (not venue1.manageTickets(event1, 80, "Cheap Seats", None, 5) and
            ticket1.list_price == 50)

def test_invalid_section():
    """ TODO """
    assert (not venue1.manageTickets(event1, 80, None, "C", 5) and
            ticket1.list_price == 50)


def test_valid_seat():
    """ TODO """
    assert (venue1.manageTickets(event1, 80, "Cheap Seats", "C", 5) and
            ticket1.list_price == 80)

def test_valid_row():
    """ TODO """
    assert (venue1.manageTickets(event1, 100, "Cheap Seats", "C", None) and
            ticket1.list_price == 100 and
            ticket3.list_price == 100)

def test_valid_section():
    """ TODO """
    assert (venue1.manageTickets(event1, 120, "Cheap Seats", None, None) and
            ticket1.list_price == 120 and
            ticket2.list_price == 120 and
            ticket3.list_price == 120)
