from ../../back_end/Admit01_Blockchain.py import *
from datetime import timedelta
import pytest

date = dt.datetime.now()

event1 = Event("event1", dt.datetime.now(), "test")
seat1 = Seat("seat1", "A", 1)
ticket1 = Ticket(event1, 100, seat1)
ticket1.id = "ticket1"

event2 = Event("event2", dt.datetime.now(), "test")
seat2 = Seat("seat2", "C", 2)
ticket2 = Ticket(event2, 50, seat2)
ticket2.id = "ticket2"

venue1 = Venue("Apollo Theater", "Chicago, IL")

user1 = User("Ethan", "Reeder", "er@example.com")
user1.id = "user1"
user1.inventory[0] == ticket1

user2 = User("Ross", "Piper", "rp@example.com")
user2.id = "user2"
user2.inventory[0] == ticket2

trans1 = Transaction.genesisTransaction("venue1")
trans1.content == "ticket0"

trans2 = Transaction("user1", "user2", 50)
trans2.content == "ticket2"

trans3 = Transaction("user2", "user1", 50)
trans3.content = "ticket1"

trans4 = Transaction("user2", "user1", 50)
trans4.content = "ticket2"

trans5 = Transaction("user1", "venue1", 50)
trans5.content = "ticket0"

trans6 = Transaction("user1", "user2", 50)
trans5.content = "ticket1"

block1 = Block(0, date, trans1, 0, venue1) # success
block2 = Block(1, date, trans2, block1.hash, venue1) # success
block3 = Block(2, date, trans3, block2.hash, venue1) # success
block4 = Block(3, date, trans4, block3.hash, venue1) # success
block5 = Block(4, date, trans5, block4.hash, venue1) # success
block6 = Block(4, date, trans6, block5.hash, venue1) # failure
block7 = Block(5, date, trans6, block1.hash, venue1) # failure
block8 = Block(5, dt.datetime.now() - timedelta(days=7), trans6, block5.hash, venue1) # failure
block9 = Block(5, date, None, block5.hash, venue1) # failure
block10 = Block(5, date, trans6, block5.hash, None) # failure
block11 = Block(5, date, trans6, " ", venue1) # failure

def test_genesis:
    #
    # Genesis block should succeed if parameters are valid
    # Not testing hash functions due to expectation of randomness
    # Hash function integrity tested with mining testing suite
    #
    assert block1.index == 0 and
           block1.timestamp == date and
           block1.data == trans1
            
def test_goodparameters:
    #
    # Block should be added if all parameters are valid
    #
    assert block2.index == 1 and
           block2.timestamp == date and
           block2.data == trans2
            
def test_goodexchange:
    #
    # Block should accept multiple exchanges between same parties
    #
    assert block3.index == 2 and
           block3.timestamp == date and
           block3.data == trans3
            
def test_goodtransactions:
    #
    # Block should accept multiple transactions in one direction
    #
    assert block4.index == 3 and
           block4.timestamp == date and
           block4.data == trans4
            
def test_goodvenuesale:
    #
    # Block should accept sales from genesis block
    #
    assert block5.index == 4 and
           block5.timestamp == date and
           block5.data == trans5

def test_badindex:
    #
    # Block should reject repeated index
    #
    assert block6.index == None and
           block6.timestamp == None and
           block6.data == None
            
def test_repeathash:
    #
    # Block should reject repeated hash
    #
    assert block7.index == None and
           block7.timestamp == None and
           block7.data == None
            
def test_badtime:
    #
    # Block should reject blocks with old time as a parameter
    #
    assert block8.index == None and
           block8.timestamp == None and
           block8.data == None
            
def test_notime:
    #
    # Block should reject blocks with no time stamp
    #
    assert block9.index == None and
           block9.timestamp == None and
           block9.data == None
            
def test_notarget:
    #
    # Block should reject blocks with no target
    #
    assert block10.index == None and
           block10.timestamp == None and
           block10.data == None
            
def test_nohash:
    #
    # Block should reject blocks with no target
    #
    assert block11.index == None and
           block11.timestamp == None and
           block11.data == None