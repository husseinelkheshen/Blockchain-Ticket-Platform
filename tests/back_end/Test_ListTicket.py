from blockchain.Admit01_Blockchain import *
from datetime import datetime
from datetime import timedelta
import copy

valid_datetime = datetime.now() + timedelta(days=7)    # one week from now
venue1 = Venue("Apollo Theater", "Chicago, IL")
event1 = Event("Test Event", valid_datetime, "Test description")
event1.venue = venue1
venue1.events[event1.id] = (event1, copy.deepcopy(event1.blockchain))
seat1 = Seat("Orchestra Center", "B", 5)
ticket1 = venue1.createTicket(event1, 150, seat1)
assert ticket1 is not None
user1 = User("Ethan", "Reeder", "er@example.com")

ticket1.listTicket(ticket1.face_value, venue1.id)
user1.wallet = 200    # user1 deposits enough money to buy ticket1
user1.buyTicket(ticket1)    # user1 buys ticket1
assert len(user1.inventory) == 1

def test_allvalid():
    """
    A Ticket for a future-dated Event should list successfully by its owner
    at any non-negative list price
    """
    ticket1.for_sale = False
    list_price = 200
    ticket1.listTicket(list_price, user1.id)
    assert ticket1.isForSale()
    assert ticket1.list_price == list_price

def test_badlistprice():
    """ List prices must be non-negative """
    ticket1.for_sale = False
    list_price = -50
    ticket1.listTicket(list_price, user1.id)
    assert not ticket1.isForSale()
    assert not ticket1.list_price == list_price

def test_baduser():
    """
    A Ticket can not be listed by a User who does not exist and/or does not
    currently own that Ticket
    """
    ticket1.for_sale = False
    list_price = 23
    ticket1.listTicket(list_price, user1.id + 1)
    assert not ticket1.isForSale()
    assert not ticket1.list_price == list_price
