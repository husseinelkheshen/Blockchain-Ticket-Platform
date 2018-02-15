from back_end.Admit01_Blockchain import *

event1 = Event("event1", date.datetime.now(), "test")
seat1 = Seat("seat1", "A", 1)
ticket1 = Ticket(event1, 100, seat1)
ticket1.id = 1

event2 = Event("event2", date.datetime.now(), "test")
seat2 = Seat("seat2", "C", 2)
ticket2 = Ticket(event2, 50, seat2)
ticket2.id = 2

user1 = User("Ethan", "Reeder", "er@example.com")
user1.id = "user1"
user1.inventory[0] == ticket1

user2 = User("Ross", "Piper", "rp@example.com")
user2.id = "user2"
user2.inventory[0] == ticket2

venue1 = Venue("Apollo Theater", "Chicago, IL")
venue1.id = "venue1"

venue2 = Venue("Apollo Theater", "Chicago, IL")
venue2.id = "venue2"

trans3 = Transaction("venue1", "user1", 50, 1) # success
trans4 = Transaction("venue2", "venue1", 50, 1) # success
trans5 = Transaction("user2", "venue2", 50, 1) # success
trans6 = Transaction("user1", "user2", 50, 1) # success
trans7 = Transaction("user1", None, 50, 1) # failure
trans8 = Transaction(None, "user2", 50, 1) # failure
trans9 = Transaction("user1", "user2", -100, 1) # failure
trans1 = Transaction("user1", "user2", 50, -1) # failure

def test_goodusertovenue():
    #
    # Transaction should succeed if user to venue and good parameters
    #
    assert (trans3.target == "venue1" and
            trans3.source == "user1" and
            trans3.value == 50)
            
def test_venuetovenue():
    #
    # Transaction should fail if between two venues
    #
    assert (trans4.target is None and
            trans4.source is None and
            trans4.value is None)
            
def test_goodvenuetouser():
    #
    # Transaction should succeed if venue to user and good parameters
    #
    assert (trans5.target is "user2" and
            trans5.source is "venue1" and
            trans5.value is 50)
            
def test_goodusertouser():
    #
    # Transaction should succeed if user to user and good parameters
    #
    assert (trans6.target is "user1" and
            trans6.source is "user2" and
            trans6.value is 50)
            
def test_badsource():
    #
    # Transaction should fail if invalid source
    #
    assert (trans7.target is None and
            trans7.source is None and
            trans7.value is None)
            
def test_badtarget():
    #
    # Transaction should fail if invalid target
    #
    assert (trans8.target is None and
            trans8.source is None and
            trans8.value is None)
            
def test_badvalue():
    #
    # Transaction should fail if invalid transaction value
    #
    assert (trans9.target is None and
            trans9.source is None and
            trans9.value is None)
