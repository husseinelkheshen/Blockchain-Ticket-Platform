from back_end.Admit01_Blockchain import *
from datetime import timedelta

valid_date = date.datetime.now() + timedelta(days = 7)

event1 = Event("event1", valid_date, "test")

venue1 = Venue("Apollo Theater", "Chicago, IL")

user1 = User("Ethan", "Reeder", "er@example.com")
user2 = User("Ross", "Piper", "rp@example.com")

trans1 = Transa
trans2 = Transaction("user1", "user2", 50, 1)
trans3 = Transaction("user2", "user1", 50, 1)
trans4 = Transaction("user2", "user1", 50, 1)
trans5 = Transaction("user1", "venue1", 50, 1)
trans6 = Transaction("user1", "user2", 80, 1)

block1 = Block(0, date, trans1, 0, venue1) # success
block2 = Block(1, date, trans2, block1.hash, venue1) # success
block3 = Block(2, date, trans3, block2.hash, venue1) # success
block4 = Block(3, date, trans4, block3.hash, venue1) # success
block5 = Block(4, date, trans5, block4.hash, venue1) # success
block6 = Block(4, date, trans6, block5.hash, venue1) # failure
block7 = Block(5, date, trans6, block1.hash, venue1) # failure
block8 = Block(5, date.datetime.now() - timedelta(days=7), trans6, block5.hash, venue1) # failure
block9 = Block(5, date, None, block5.hash, venue1) # failure
block10 = Block(5, date, trans6, block5.hash, None) # failure
block11 = Block(5, date, trans6, "", venue1) # failure

            
def test_goodparameters():
    #
    # Block should be added if all parameters are valid
    #
    assert (block2.index == 1 and
            block2.timestamp == date and
            block2.data == trans2)
            
def test_goodexchange():
    #
    # Block should accept multiple exchanges between same parties
    #
    assert (block3.index == 2 and
            block3.timestamp == date and
            block3.data == trans3)
            
def test_goodtransactions():
    #
    # Block should accept multiple transactions in one direction
    #
    assert (block4.index == 3 and
            block4.timestamp == date and
            block4.data == trans4)
            
def test_goodvenuesale():
    #
    # Block should accept sales from genesis block
    #
    assert (block5.index == 4 and
            block5.timestamp == date and
            block5.data == trans5)

def test_badindex():
    #
    # Block should reject repeated index
    #
    assert (block6.index == None and
            block6.timestamp == None and
            block6.data == None)
            
def test_repeathash():
    #
    # Block should reject repeated hash
    #
    assert (block7.index == None and
            block7.timestamp == None and
            block7.data == None)
            
def test_badtime():
    #
    # Block should reject blocks with old time as a parameter
    #
    assert (block8.index == None and
            block8.timestamp == None and
            block8.data == None)
            
def test_notime():
    #
    # Block should reject blocks with no time stamp
    #
    assert (block9.index == None and
            block9.timestamp == None and
            block9.data == None)
            
def test_notarget():
    #
    # Block should reject blocks with no target
    #
    assert (block10.index == None and
            block10.timestamp == None and
            block10.data == None)
            
def test_nohash():
    #
    # Block should reject blocks with no target
    #
    assert (block11.index == None and
            block11.timestamp == None and
            block11.data == None)
            
chain1 = Chain(event1, ticket2)
chain1.blocks = None

chaintrans0 = chain1.findRecentTrans("ticket2") # failure

chain1.blocks = list(block2)

chaintrans1 = chain1.findRecentTrans("ticket2") # success
chaintrans2 = chain1.findRecentTrans("ticket1") # failure

chain1.blocks.append(block4)

chaintrans3 = chain1.findRecentTrans("ticket2")

def test_notransactions():
    #
    # Search should be empty if ticket has no transactions
    # Functionally this should not happen since ticket genesis involves transactions
    # This is mainly for debugging purposes
    #
    assert (chaintrans0.target == None and
            chaintrans0.source == None and
            chaintrans0.value == None)
            
def test_listofone():
    #
    # Should return the only transaction in the list
    #
    assert (chaintrans1.target == "user1" and
            chaintrans1.source == "user2" and
            chaintrans1.value == 50)
            
def test_falseticketid():
    #
    # Return no ticket if ticket id is incorrect
    #
    assert (chaintrans2.target == None and
            chaintrans2.source == None and
            chaintrans2.value == None)
            
def test_newtransaction():
    #
    # Should return only most recent transaction
    #
    assert (chaintrans3.target == "user2" and
            chaintrans3.source == "user1" and
            chaintrans3.value == 50)
            
