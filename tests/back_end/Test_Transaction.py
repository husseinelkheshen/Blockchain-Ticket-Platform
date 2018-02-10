from ../../back_end/Admit01_Blockchain.py import *
import pytest

event1 = Event("event1", dt.datetime.now(), "test")
seat1 = Seat("seat1", "A", 1)
ticket1 = Ticket(event1, 100, seat1)
ticket1.id = "ticket1"

event2 = Event("event2", dt.datetime.now(), "test")
seat2 = Seat("seat2", "C", 2)
ticket2 = Ticket(event2, 50, seat2)
ticket2.id = "ticket2"

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

trans1 = Transaction.genesisTransaction("venue1") # success
trans2 = Transaction.genesisTransaction("venue3") # failure
trans3 = Transaction("venue1", "user1", 50) # success
trans4 = Transaction("venue2", "venue1", 50) # failure
trans5 = Transaction("user2", "venue1", 50) # success
trans6 = Transaction("user1", "user2", 50) # success
trans7 = Transaction("user1", "", 50) # failure
trans8 = Transaction("", "user2", 50) # failure
trans9 = Transaction("user1", "user2", -100) # failure

def test_genesis:
    #
    # Genesis transaction should succeed if target is valid
    #
    assert trans1.target == venue1.id and
           trans1.source == None and
           trans1.value == 0
            
def test_badgenesis
    #
    # Genesis transaction should fail if target is invalid
    #
    assert trans2.target == None and
           trans2.source == None and
           trans2.value == None

def test_goodusertovenue
    #
    # Transaction should succeed if user to venue and good parameters
    #
    assert trans3.target == "venue1" and
           trans3.source == "user1" and
           trans3.value == 50
            
def test_venuetovenue
    #
    # Transaction should fail if between two venues
    #
    assert trans4.target == None and
           trans4.source == None and
           trans4.value == None
            
def test_goodvenuetouser
    #
    # Transaction should succeed if venue to user and good parameters
    #
    assert trans5.target == "user2" and
           trans5.source == "venue1" and
           trans5.value == 50
            
def test_goodusertouser
    #
    # Transaction should succeed if user to user and good parameters
    #
    assert trans6.target == "user1" and
           trans6.source == "user2" and
           trans6.value == 50    
            
def test_badsource
    #
    # Transaction should fail if invalid source
    #
    assert trans7.target == None and
           trans7.source == None and
           trans7.value == None
            
def test_badtarget
    #
    # Transaction should fail if invalid target
    #
    assert trans8.target == None and
           trans8.source == None and
           trans8.value == None
            
def test_badvalue
    #
    # Transaction should fail if invalid transaction value
    #
    assert trans9.target == None and
           trans9.source == None and
           trans9.value == None
