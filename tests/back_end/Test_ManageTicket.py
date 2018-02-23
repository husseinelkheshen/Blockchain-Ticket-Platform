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
    assert (venue1.manageTicket(None, 80, "Cheap Seats", "C", 5) is False and
            ticket1.list_price == 50)

def test_no_price():
    assert (venue1.manageTicket(event1, None, "Cheap Seats", "C", 5) is False and
            ticket1.list_price == 50)

def test_invalid_price():
    assert (venue1.manageTicket(event1, -30, "Cheap Seats", "C", 5) is False and
            ticket1.list_price == 50)

def test_invalid_row():
    assert (venue1.manageTicket(event1, 80, "Cheap Seats", None, 5) is False and
            ticket1.list_price == 50)

def test_invalid_section():
    assert (venue1.manageTicket(event1, 80, None, "C", 5) is False and
            ticket1.list_price == 50)


def test_valid_seat():
    assert (venue1.manageTicket(event1, 80, "Cheap Seats", "C", 5) is True and
            ticket1.list_price == 80)

def test_valid_row():
    assert (venue1.manageTicket(event1, 100, "Cheap Seats", "C", None) is True and
            ticket1.list_price == 100 and
            ticket3.list_price == 100)

def test_valid_section():
    assert (venue1.manageTicket(event1, 120, "Cheap Seats", None, None) is True and
            ticket1.list_price == 120 and
            ticket2.list_price == 120 and
            ticket3.list_price == 120)
