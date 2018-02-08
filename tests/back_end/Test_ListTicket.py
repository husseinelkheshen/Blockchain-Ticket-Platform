from ../../back_end/Admit01_Blockchain.py import *

event1 = Event("Test Event", datetime_obj, "Test description")
seat1 = Seat("Orchestra Center", "B", 5)
ticket1 = Ticket(event1, 150, seat1)
user1 = User("Ethan", "Reeder", "er@example.com")

def test_allvalid:
    list_price = 200
    ticket1.listTicket(list_price, user1.getID())
    assert(ticket1.isForSale() and ticket1.list_price == list_price)
