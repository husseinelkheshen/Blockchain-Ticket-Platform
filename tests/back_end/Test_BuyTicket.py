from blockchain.Admit01_Blockchain import *

#
# Creation of Peripheral Objects
#
testDatetime1 = date.datetime(2018, 3, 31, 0, 0, 0, 0)
testDatetime2 = date.datetime(2017, 3, 31, 0, 0, 0, 0)

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
testEvent2 = Event("Class2", testDatetime2, "Tuesday and Thursday")

#
# Creation of Test Tickets
#
testTicket1 = Ticket(testEvent1, 100, testSeat1)
testTicket1.for_sale = True

testTicket2 = Ticket(testEvent1, 500, testSeat2)
testTicket2.for_sale = False

testTicket3 = Ticket(testEvent1, 50, testSeat1)
testTicket3.for_sale = True

testTicket4 = Ticket(testEvent1, 0, testSeat2)
testTicket4.for_sale = True

testTicket5 = Ticket(testEvent1, 100, testSeat1)
testTicket5.for_sale = True

testTicket6 = Ticket(testEvent2, 0, testSeat2)
testTicket.for_sale = True

#
# Test purchasing of tickets with funds in wallet
#
def test_buyTicket_funds1():
	testUser1.buyTicket(testTicket1)
	assert(testUser1.inventory[0] == testTicket1
	       and testTicket1.for_sale == False
	       and testUser1.wallet == 0)

def test_buyTicket_funds2():
	testUser4.buyTicket(testTicket4)
	assert(testUser4.inventory[0] == testTicket4
	       and testTicket4.for_sale == False
	       and testUser4.wallet == 0)

def test_buyTicket_funds3():
	testUser4.buyTicket(testTicket3)
	assert(testUser4.inventory[0] == None
	       and testTicket3.for_sale == True
	       and testUser4.wallet == 0)

def test_buyTicket_funds4():
	testUser3.buyTicket(testTicket3)
	assert(testUser3.inventory[0] == testTicket3
	       and testTicket3.for_sale == False
	       and testUser3.wallet == 950)

#
# Test purchasing of tickets based on availability
#
def test_buyTicket_availability1():
	testUser2.buyTicket(testTicket1)
	assert(testUser.inventory[0] == None
	       and testTicket1.for_sale == False
	       and testUser.wallet == 500)

def test_buyTicket_availability2():
	testUser2.buyTicket(testTicket2)
	assert(testUser2.inventory[0] == None
	       and testTicket1.for_sale == False
	       and testUser2.wallet == 500)

#
# Test purchasing of tickets when user does not exist
#
def test_buyTicket_userDNE():
	assert not testUser5.buyTicket(testTicket5)

#
# Test buyTicket when ticket does not exist
#
def test_buyTicket_ticketDNE():
	assert not testUser3.buyTicket(testTicket7)

#
# Test buyTicket when event has transpired
#
def test_buyTicket_eventDNE():
	assert not testUser3.buyTicket(testTicket6)