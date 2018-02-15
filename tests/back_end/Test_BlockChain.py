from blockchain.Admit01_Blockchain import *
from datetime import timedelta

valid_date = date.datetime.now() + timedelta(days = 7)

event1 = Event("event1", valid_date, "test")

venue1 = Venue("Apollo Theater", "Chicago, IL")

user1 = User("Ethan", "Reeder", "er@example.com")
user2 = User("Ross", "Piper", "rp@example.com")

trans1 = Transaction(venue1.id, None, 50, 0)
trans2 = Transaction(user1.id, user2.id, 50, 1)
trans3 = Transaction(user2.id, user1.id, 50, 2)
trans4 = Transaction(user2.id, user1.id, 50, 1)
trans5 = Transaction(user1.id, user2.id, 80, 1)

block1 = Block(0, date, [trans1], None) # success
block2 = Block(1, date, [trans2, trans3], block1.hash) # success
block3 = Block(2, date, [trans4], block2.hash) # success
block4 = Block(-3, date, [trans5], block3.hash) # failure
block5 = Block(None, date, [trans5], block3.hash) # failure
block6 = Block(3, date, [trans5], block1.hash) # failure
block7 = Block(3, date.datetime.now() - timedelta(days=7), [trans5], block3.hash) # failure
block8 = Block(3, None, [trans5], block3.hash) # failure
block9 = Block(3, date, None, block3.hash) # failure
block10 = Block(2, date, [trans5], block3.hash) # failure

def test_goodparameters():
    #
    # Block should be added if all parameters are valid and no source
    # This simulates the first block in a chain
    #
    assert (block1.index == 0 and
            block1.timestamp == date and
            block1.data[0] == trans1 and
            block1.prev_hash == "")

def test_goodexchange():
    #
    # Block should accept multiple transactions in one block
    # Simulates UpgradeTicket
    #
    assert (#block2.index == 1 and
            block2.timestamp == date and
            block2.data[0] == trans2 and
            block2.data[1] == trans3)

def test_goodtransactions():
    #
    # Block should accept multiple transactions from one source to one target
    #
    assert (#block3.index == 2 and
            block3.timestamp == date and
            block3.data[0] == trans4)

def test_badindex():
    #
    # Block should reject negative index
    #
    assert (block4.index is None and
            block4.timestamp is None and
            block4.data is None)

def test_noindex():
    #
    # Block should reject negative index
    #
    assert (block5.index is None and
            block5.timestamp is None and
            block5.data is None)

# def test_repeathash():
#     #
#     # Block should reject repeated hash
#     #
#     assert (block7.index is None and
#             block7.timestamp is None and
#             block7.data is None)
#
# def test_badtime():
#     #
#     # Block should reject blocks with old time as a parameter
#     #
#     assert (block8.index is None and
#             block8.timestamp is None and
#             block8.data is None)

def test_notime():
    #
    # Block should reject blocks with no time stamp
    #
    assert (block8.index is None and
            block8.timestamp is None and
            block8.data is None)

def test_notrans():
    #
    # Block should reject blocks with no transaction
    #
    assert (block9.index is None and
            block9.timestamp is None and
            block9.data is None)

chaintrans0 = event1.blockchain.findRecentTrans(0) # failure

event1.blockchain.blocks.append(block2)

chaintrans1 = event1.blockchain.findRecentTrans(1) # success
chaintrans2 = event1.blockchain.findRecentTrans(0) # failure

event1.blockchain.blocks.append(block3)

chaintrans3 = event1.blockchain.findRecentTrans(1)

def test_notransactions():
    #
    # Search should be empty if ticket has no transactions
    # Functionally this should not happen since ticket genesis involves transactions
    # This is mainly for debugging purposes
    #
    assert chaintrans0 is None

def test_listofone():
    #
    # Should return the only transaction in the list
    #
    assert chaintrans1 is not None

# def test_falseticketid():
#     #
#     # Return no ticket if ticket id is incorrect
#     #
#     assert (chaintrans2.target is None and
#             chaintrans2.source is None and
#             chaintrans2.value is None)
#
# def test_newtransaction():
#     #
#     # Should return only most recent transaction
#     #
#     assert (chaintrans3.target == user2.id and
#             chaintrans3.source == user1.id and
#             chaintrans3.value == 50)

