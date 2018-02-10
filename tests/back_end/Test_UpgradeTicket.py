#
# Tests for upgradeTicket
#

from ../back_end/Admit01_Blockchain.py import *

#
# Creation of Peripheral Objects
#
testDatetime1 = datetime(2018, 3, 31, 0, 0, 0, 0)
testDatetime2 = datetime(2017, 3, 31, 0, 0, 0, 0)

testSeat1 = Seat("Cheap Seats", "C", 5)
testSeat2 = Seat("Steak Sauce", "A", 1)

#
# Creation of Test Users
#
testUser1 = User("Ethan", "Reeder", "asdf@uchicago.edu")
testUser1.wallet = 100

testUser2 = User("Ross", "Piper", "piedpiper@uchicago.edu")
testUser2.wallet = 500

testUser3 = User("Hayden", "Mans", "getyourmans@uchicago.edu")
testUser3.wallet = 1000

testUser4 = User("Hussein", "El Kheshen", "eloella@uchicago.edu")
testUser4.wallet = 0

#
# Creation of Test Events
#
testEvent1 = Event("Class1", testDatetime1, "Tuesday and Thursday")
testEvent2 = Event("Class2", testDatetime1, "Tuesday and Thursday")
testEvent3 = Event("Class3", testDatetime2, "Tuesday and Thursday")

#
# Creation of Test Tickets
#
testTicket1 = Ticket(testEvent1, 100, testSeat1)
testTicket1.for_sale = True

testTicket2 = Ticket(testEvent1, 550, testSeat2)
testTicket2.for_sale = False

testTicket3 = Ticket(testEvent1, 500, testSeat1)
testTicket3.for_sale = True

testTicket4 = Ticket(testEvent1, 0, testSeat2)
testTicket4.for_sale = True

testTicket5 = Ticket(testEvent1, 100, testSeat1)
testTicket5.for_sale = True

testTicket6 = Ticket(testEvent2, 200, testSeat1)
testTicket6.for_sale = True

testTicket7 = Ticket(testEvent3, 600, testSeat2)
testTicket7.for_sale = True

testTicket8 = Ticket(testEvent1, 100, testSeat1)
testTicket8.for_sale = True

testTicket9 = Ticket(testEvent1, 100, testSeat2)
testTicket9.for_sale = True

#
# Test upgrading tickets validly for sale
#
def test_upgradeTicket_valid():
	testUser3.buyTicket(testTicket1)
	assert(testUser3.upgradeTicket(testTicket1, testTicket3)
	       and testUser3.wallet == 500
		   and testUser3.inventory[0] == testTicket3
		   and testTicket1.for_sale == True
		   and testTicket2.for_sale == False)

#
# Test upgrading tickets between different events
#
def test_upgradeTicket_valid():
	testUser2.buyTicket(testTicket5)
	assert!(testUser2.upgradeTicket(testTicket5, testTicket6))
	assert(testUser2.wallet == 400)
    assert(testUser2.inventory[0] == testTicket5)

#
# Test upgrading tickets user does not own
#
def test_upgradeTicket_unowned():
	assert!(testUser4.upgradeTicket(testTicket6, testTicket4))

#
# Test upgrading tickets not for sale
#
def test_upgradeTicket_notforsale():
	assert!(testUser3.upgradeTicket(testTicket3, testTicket2))

#
# Test upgrading tickets that are worth less than current
#
def test_upgradeTicket_less():
	assert!(testUser3.upgradeTicket(testTicket3, testTicket4))

#
# Test upgrading invalid tickets
#
def test_upgradeTicket_invalid():
	assert!(testUser3.upgradeTicket(testTicket3, None))

#
# Test upgrading tickets for events that have transpired
#
def test_upgradeTicket_transpired():
	assert!(testUser3.upgradeTicket(testTicket3, testTicket7))

#
# Test upgrading tickets equal to current
#
def test_upgradeTicket_equal():
	testUser1.buyTicket(testTicket8)
	assert!(testUser1.upgradeTicket(testTicket8, testTicket9))