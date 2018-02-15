from blockchain.Admit01_Blockchain import *
from datetime import timedelta

valid_datetime = date.datetime.now() + timedelta(days=7) # one week from now

event1 = Event("event1", valid_datetime, "test")

user1 = User("Ethan", "Reeder", "er@example.com")
user2 = User("Ross", "Piper", "rp@example.com")

venue1 = Venue("Apollo Theater", "Chicago, IL")
venue2 = Venue("United Center", "Chicago, IL")

trans0 = Transaction(venue1.id, None, 50, 1)
trans1 = Transaction(venue1.id, user1.id, 50, 1) # success
trans2 = Transaction(venue2.id, venue1.id, 50, 1) # success
trans3 = Transaction(user2.id, venue2.id, 50, 1) # success
trans4 = Transaction(user1.id, user2.id, 50, 1) # success
trans5 = Transaction(user1.id, None, 50, 1) # failure
trans6 = Transaction(None, user2.id, 50, 1) # failure
trans7 = Transaction(user1.id, user2.id, -100, 1) # failure
trans8 = Transaction(user1.id, user2.id, 50, -1) # failure
trans9 = Transaction(user1.id, user2.id, None, 1) # failure
trans10 = Transaction(user1.id, user2.id, 50, None) # failure
            
def test_badvalue():
    #
    # Transaction should fail if invalid transaction value
    #
    assert (trans7.target is None and
            trans7.source is None and
            trans7.value is None and
            trans7.ticket_num is None)

def test_badticketnum():
    #
    # Transaction should fail if invalid ticket_num value
    #
    assert (trans8.target is None and
            trans8.source is None and
            trans8.value is None and
            trans8.ticket_num is None)

def test_novalue():
    #
    # Transaction should fail if invalid transaction value
    #
    assert (trans9.target is None and
            trans9.source is None and
            trans9.value is None and
            trans9.ticket_num is None)

def test_noticketnum():
    #
    # Transaction should fail if invalid transaction value
    #
    assert (trans10.target is None and
            trans10.source is None and
            trans10.value is None and
            trans10.ticket_num is None)