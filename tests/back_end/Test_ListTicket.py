from ../../back_end/Admit01_Blockchain.py import *

event1 = Event("Test Event", datetime_obj, "Test description")
event2 = None
seat1 = Seat("Orchestra Center", "B", 5)
seat2 = None
ticket1 = Ticket(event1, 150, seat1)
user1 = User("Ethan", "Reeder", "er@example.com")

def test_allvalid:
    list_price = 200
    ticket1.listTicket(list_price, user1.getID())
    assert ticket1.isForSale() and ticket1.list_price == list_price

def test_badlistprice:
    list_price = -50
    ticket1.listTicket(list_price, user1.getID())
    assert !(ticket1.isForSale() or ticket1.list_price == list_price)

def test_baduser:
    list_price = 200
    ticket1.listTicket(list_price, user1.getID() + 1)
    assert !(ticket1.isForSale() or ticket1.list_price == list_price)
