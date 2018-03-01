from blockchain.Admit01_Blockchain import *
from datetime import datetime
from datetime import timedelta
from time import sleep
from copy import deepcopy

def test_rwvalidation():
    """
    This tests that the validation performed on the blockchains prior to any read or write
     correctly judges the validity of the chain. It essentially confirms that no data has
     been altered anywhere down the line
    """
    venue = Venue("Max Palevsky", "Hyde Park")
    event = venue.createEvent("Rock Show", datetime.now() + timedelta(days=1095),
                              "An event for students to rock out!")
    seat = Seat("General Admission", "N/A", 1)
    ticket = venue.createTicket(event, 20, seat)
    user1 = User("Ethan", "Reeder", "er@example.com")
    user2 = User("Ross", "Piper", "rp@example.com")
    user1.wallet = 100000
    user2.wallet = 100000
    ticket.for_sale = True
    user1.buyTicket(ticket)
    # chain is valid after genesis plus one sale
    assert event.rwValidation() is True
    ticket.for_sale = True
    user2.buyTicket(ticket)
    # chain is valid after a second transaction
    assert event.rwValidation() is True
    error1 = deepcopy(event)
    error1.blockchain.blocks[-2].hash = ""
    # altering a hash breaks the validation
    assert error1.rwValidation() is False
    ticket.for_sale = True
    user1.buyTicket(ticket)
    error2 = deepcopy(event)
    error2.venue.events[error2.id][1].blocks[-2].data[0].target = user1.getID()
    # changing target of a previous transaction breaks the validation
    assert error2.rwValidation() is False
    error2.blockchain.blocks[-2].data[0].target = user1.getID()
    # even if changed in the mirror chain as well, validation is still broken
    assert error2.rwValidation() is False
    user3 = User("Hayden", "Mans", "hm@example.com")
    user3.wallet = 100000
    seat2 = Seat("General Admission", "N/A", 2)
    ticket2 = venue.createTicket(event, 20, seat2)
    ticket2.for_sale = True
    user3.buyTicket(ticket2)
    error3 = deepcopy(event)
    error3.blockchain.blocks[-2].index = len(error3.blockchain.blocks) - 1
    # changing the index of a block will break the validation
    assert error3.rwValidation() is False
    error4 = deepcopy(event)
    error4.blockchain.blocks[-1].prev_hash = "somefakehash"
    # changing the previous hash of a block will break the validation
    assert error4.rwValidation() is False
    # a slightly longer valid chain with transactions between multiple users with multiple tickets is still valid if not altered
    assert event.rwValidation() is True









