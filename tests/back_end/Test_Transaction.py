from blockchain.Admit01_Blockchain import *
from datetime import timedelta

valid_datetime = date.datetime.now() + timedelta(days=7) # one week from now

event1 = Event("event1", valid_datetime, "test")

user1 = User("Ethan", "Reeder", "er@example.com")
user2 = User("Ross", "Piper", "rp@example.com")

venue1 = Venue("Apollo Theater", "Chicago, IL")
venue2 = Venue("United Center", "Chicago, IL")

trans1 = Transaction(venue1.id, user1.id, 50, 1) # success
trans2 = Transaction(venue2.id, venue1.id, 50, 1) # success
trans3 = Transaction(user2.id, venue2.id, 50, 1) # success
trans4 = Transaction(user1.id, user2.id, 50, 1) # success
trans5 = Transaction(venue1.id, None, 50, 1) # success
trans6 = Transaction(None, venue1.id, 50, 1) # success
trans7 = Transaction(user1.id, user2.id, -100, 1) # failure
trans8 = Transaction(user1.id, user2.id, 50, -1) # failure
trans9 = Transaction(user1.id, user2.id, None, 1) # failure
trans10 = Transaction(user1.id, user2.id, 50, None) # failure

def test_goodusertovenue():
    """ Test that a transaction succeeds if from valid user to valid venue """
    assert (trans1.target is venue1.id and
            trans1.source is user1.id and
            trans1.value is 50 and
            trans1.ticket_num is 1)

def test_goodvenuetovenue():
    """ Test that a transaction succeeds if from valid venue to valid venue """
    assert (trans2.target is venue2.id and
            trans2.source is venue1.id and
            trans2.value is 50 and
            trans2.ticket_num is 1)

def test_goodvenuetouser():
    """ Test that a transaction succeeds if from valid venue to valid user """
    assert (trans3.target is user2.id and
            trans3.source is venue2.id and
            trans3.value is 50 and
            trans3.ticket_num is 1)

def test_goodusertouser():
    """ Test that a transaction succeeds if from valid user to valid user """
    assert (trans4.target is user1.id and
            trans4.source is user2.id and
            trans4.value is 50 and
            trans4.ticket_num is 1)

def test_goodnonetovenue():
    """
    Test that a transaction succeeds if from None to valid venue
    This simulates the creation of a ticket in CreateTicket
    """
    assert (trans5.target is venue1.id and
            trans5.source is None and
            trans5.value is 50 and
            trans5.ticket_num is 1)

def test_goodvenuetonone():
    """
    Test that a transaction succeeds if from valid venue to None
    This simulates the destruction of used and expired tickets
    """
    assert (trans6.target is None and
            trans6.source is venue1.id and
            trans6.value is 50 and
            trans6.ticket_num is 1)

def test_badvalue():
    """ Test that a transaction fails if a Transaction value is invalid (negative) """
    assert (trans7.target is None and
            trans7.source is None and
            trans7.value is None and
            trans7.ticket_num is None)

def test_badticketnum():
    """ Test that a transaction fails if a ticket_num is invalid (negative) """
    assert (trans8.target is None and
            trans8.source is None and
            trans8.value is None and
            trans8.ticket_num is None)

def test_novalue():
    """ Test that a transaction fails if a Transaction value is None """
    assert (trans9.target is None and
            trans9.source is None and
            trans9.value is None and
            trans9.ticket_num is None)

def test_noticketnum():
    """ Test that a transaction fails if a ticket_num is None """
    assert (trans10.target is None and
            trans10.source is None and
            trans10.value is None and
            trans10.ticket_num is None)