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

block1 = Block(0, valid_date, [trans1], None) # success
block2 = Block(1, valid_date, [trans2, trans3], "testhash") # success
block3 = Block(2, valid_date, [trans4], "testhash") # success
block4 = Block(-3, valid_date, [trans5], "testhash") # failure
block5 = Block(None, valid_date, [trans5], "testhash") # failure
block6 = Block(3, None, [trans5], "testhash") # failure
block7 = Block(3, valid_date, None, "testhash") # failure

# def test_goodparameters():
#     """
#     Test that a Block successfully creates if there is no prev_hash
#     This simulates the first Block in a Chain
#     """
#     assert (block1.index == 0 and
#             block1.timestamp == date and
#             block1.data[0] == trans1 and
#             block1.prev_hash == "testhash")

# def test_goodmultitrans():
#     """
#     Test that a Block successfully creates if it contains multiple transactions
#     """
#     assert (block2.index == 1 and
#             block2.timestamp == date and
#             block2.data[0] == trans2 and
#             block2.data[1] == trans3 and
#             block2.prev_hash == "testhash")
#
# def test_goodtrans():
#     """ Test that a Block successfully creates if it contains one transactions """
#     assert (block3.index == 2 and
#             block3.timestamp == date and
#             block3.data[0] == trans4 and
#             block3.prev_hash == "testhash")
#
# def test_badindex():
#     """ Test that a Block fails if it contains an invalid index (negative) """
#     assert (block4.index is None and
#             block4.timestamp is None and
#             block4.data is None and
#             block4.prev_hash is None and
#             block4.hash is None)
#
# def test_noindex():
#     """ Test that a Block fails if it contains an index is None """
#     assert (block5.index is None and
#             block5.timestamp is None and
#             block5.data is None and
#             block5.prev_hash is None and
#             block5.hash is None)
#
# def test_notime():
#     """ Test that a Block fails if it containsNone no timestamp """
#     assert (block6.index is None and
#             block6.timestamp is None and
#             block6.data is None and
#             block6.prev_hash is None and
#             block6.hash is None)
#
# def test_notrans():
#     """ Test that a Block fails if it containsNone no Transaction """
#     assert (block7.index is None and
#             block7.timestamp is None and
#             block7.data is None and
#             block7.prev_hash is None and
#             block7.hash is None)

chaintrans0 = event1.blockchain.findRecentTrans(0) # failure

event1.blockchain.blocks.append(block2)

chaintrans1 = event1.blockchain.findRecentTrans(1) # success
chaintrans2 = event1.blockchain.findRecentTrans(0) # failure

event1.blockchain.blocks.append(block3)

chaintrans3 = event1.blockchain.findRecentTrans(1)


def test_noblocks():
    """ Tests that return value is None if Chain has no Blocks """
    assert chaintrans0 is None

def test_listofone():
    """ Tests that return value is correct if Chain has one Block with relevant ticket_id """
    assert (chaintrans1.target == user1.id and
            chaintrans1.source == user2.id and
            chaintrans1.value == 50)

def test_falseticketid():
    """ Tests that return value is None if Chain has no Blocks with relevant ticket_id """
    assert chaintrans2 is None

def test_newtransaction():
    """ Tests that return value is correct if Chain has multiple Blocks with relevant ticket_id """
    assert (chaintrans3.target == user2.id and
            chaintrans3.source == user1.id and
            chaintrans3.value == 50)

