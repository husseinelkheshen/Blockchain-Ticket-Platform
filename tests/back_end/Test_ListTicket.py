from blockchain.Admit01_Blockchain import *
from datetime import datetime
from datetime import timedelta

valid_datetime = datetime.now() + timedelta(days=7)    # one week from now
event1 = Event("Test Event", valid_datetime, "Test description")
seat1 = Seat("Orchestra Center", "B", 5)
ticket1 = Ticket(event1, 150, seat1)
user1 = User("Ethan", "Reeder", "er@example.com")

user1.wallet = 200    # user1 deposits enough money to buy ticket1
user1.buyTicket(ticket1)    # user1 buys ticket1

# def test_allvalid():
#     """
#     A Ticket for a future-dated Event should list successfully by its owner
#     at any non-negative list price
#     """
#     ticket1.for_sale = False
#     list_price = 200
#     ticket1.listTicket(list_price, user1.getID())
#     assert (ticket1.isForSale() and
#             ticket1.list_price == list_price)

def test_badlistprice():
    """ List prices must be non-negative """
    ticket1.for_sale = False
    list_price = -50
    ticket1.listTicket(list_price, user1.getID())
    assert not (ticket1.isForSale() or
                ticket1.list_price == list_price)

def test_baduser():
    """
    A Ticket can not be listed by a User who does not exist and/or does not
    currently own that Ticket
    """
    ticket1.for_sale = False
    list_price = 200
    ticket1.listTicket(list_price, user1.getID() + 1)
    assert not (ticket1.isForSale() or
                ticket1.list_price == list_price)
