from blockchain.Admit01_Blockchain import *
from datetime import timedelta

valid_date = date.datetime.now() + timedelta(days = 7)

testSeat1 = Seat("Cheap Seats", "C", 5)

testEvent1 = Event("Class1", valid_date, "Tuesday and Thursday")

ticket1 = Ticket(None, 50, testSeat1)
ticket2 = Ticket(testEvent1, -1, testSeat1)
ticket3 = Ticket(testEvent1, None, testSeat1)
ticket4 = Ticket(testEvent1, 1, None)
ticket5 = Ticket(testEvent1, 50, testSeat1)

def test_noEvent():
    """ Test that a Ticket fails if event is None """
    assert (ticket1.ticket_num is None and
            ticket1.event is None and
			ticket1.seat is None and
			ticket1.face_value is None and
			ticket1.list_price is None and
			ticket1.for_sale is None and
			ticket1.history is None)

def test_invalidValue():
    """ Test that a Ticket fails if ticket value is invalid (negative) """
    assert (ticket2.ticket_num is None and
            ticket2.event is None and
			ticket2.seat is None and
			ticket2.face_value is None and
			ticket2.list_price is None and
			ticket2.for_sale is None and
			ticket2.history is None)

def test_noValue():
    """ Test that a Ticket fails if ticket value is None """
    assert (ticket3.ticket_num is None and
            ticket3.event is None and
			ticket3.seat is None and
			ticket3.face_value is None and
			ticket3.list_price is None and
			ticket3.for_sale is None and
			ticket3.history is None)

def test_noSeat():
    """ Test that a Ticket fails if Seat is None """
    assert (ticket4.ticket_num is None and
            ticket4.event is None and
			ticket4.seat is None and
			ticket4.face_value is None and
			ticket4.list_price is None and
			ticket4.for_sale is None and
			ticket4.history is None)

def test_normal():
	""" Test that a Ticket constructs successfully if all parameters valid """
	assert (ticket5.ticket_num == 0 and
			ticket5.event == testEvent1 and
			ticket5.seat == testSeat1 and
			ticket5.face_value == 50 and
			ticket5.list_price == 50)
