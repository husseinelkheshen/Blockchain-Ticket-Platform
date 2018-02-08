from ../../back_end/Admit01_Blockchain.py import *

event = Event("Test Event", datetime_obj, "Test description")
seat = Seat("Orchestra Center", "B", 5)
ticket1 = Ticket(event, 150, seat)

def test_allvalid:
    ticket1.
