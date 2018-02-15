from back_end.Admit01_Blockchain import *
from datetime import timedelta

valid_datetime = date.datetime.now() + timedelta(days=7) # one week from now

event1 = Event("event1", valid_datetime, "test")

user1 = User("Ethan", "Reeder", "er@example.com")
user2 = User("Ross", "Piper", "rp@example.com")

venue1 = Venue("Apollo Theater", "Chicago, IL")
venue2 = Venue("United Center", "Chicago, IL")

trans1 = Transaction("venue1", "user1", 50, 1) # success
trans2 = Transaction("venue2", "venue1", 50, 1) # success
trans3 = Transaction("user2", "venue2", 50, 1) # success
trans4 = Transaction("user1", "user2", 50, 1) # success
trans5 = Transaction("user1", "", 50, 1) # failure
trans6 = Transaction("", "user2", 50, 1) # failure
trans7 = Transaction("user1", "user2", -100, 1) # failure
trans8 = Transaction("user1", "user2", 50, -1) # failure


def test_badsource():
    #
    # Transaction should fail if invalid source
    #
    assert (trans5.target is None and
            trans5.source is None and
            trans5.value is None and
            trans5.ticket_num is None)
            
def test_badtarget():
    #
    # Transaction should fail if invalid target
    #
    assert (trans6.target is None and
            trans6.source is None and
            trans6.value is None and
            trans6.ticket_num is None)
            
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