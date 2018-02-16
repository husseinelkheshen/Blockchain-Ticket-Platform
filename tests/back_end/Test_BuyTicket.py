from blockchain.Admit01_Blockchain import *
import datetime as date
import copy

#
# Creation of Peripheral Objects
#
testDatetime1 = date.datetime(2018, 3, 31, 0, 0, 0, 0)
testDatetime2 = date.datetime(2017, 3, 31, 0, 0, 0, 0)

testSeat1 = Seat("Cheap Seats", "C", 5)
testSeat2 = Seat("Steak Sauce", "A", 1)
testSeat3 = Seat("Cheap Seats", "D", 6)
testSeat4 = Seat("Cheap Seats", "E", 7)
testSeat5 = Seat("Cheap Seats", "F", 8)
testSeat6 = Seat("Cheap Seats", "G", 9)

#
# Creation of Test Venue
#
testVenue = Venue("venue", "DC")
testVenue.id = 1

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
testEvent1.venue = testVenue
testEvent1.id = 2
testVenue.events[testEvent1.id] = (testEvent1, copy.deepcopy(testEvent1.blockchain))

'''
testEvent2 = Event("Class2", testDatetime2, "Tuesday and Thursday")
testEvent2.venue = testVenue
testEvent2.id = 3
testVenue.events[testEvent2.id] = (testEvent2, copy.deepcopy(testEvent2.blockchain))
'''

#
# Creation of Test Tickets
#
testTicket1 = testVenue.createTicket(testVenue.events[testEvent1.id][0], 100, testSeat1)
testTicket1.for_sale = True

testTicket2 = testVenue.createTicket(testVenue.events[testEvent1.id][0], 500, testSeat2)
testTicket2.for_sale = False

testTicket3 = testVenue.createTicket(testVenue.events[testEvent1.id][0], 50, testSeat3)
testTicket3.for_sale = True

testTicket4 = testVenue.createTicket(testVenue.events[testEvent1.id][0], 0, testSeat4)
testTicket4.for_sale = True

testTicket5 = testVenue.createTicket(testVenue.events[testEvent1.id][0], 100, testSeat5)
testTicket5.for_sale = True

testTicket6 = testVenue.createTicket(testVenue.events[testEvent1.id][0], 0, testSeat6)
testTicket6.for_sale = True

#
# Test purchasing of tickets with funds in wallet
#
def test_buyTicket_funds1():
	assert(testUser1.buyTicket(testTicket1)
		   and testUser1.inventory[-1] == testTicket1
	       and testTicket1.for_sale == False
	       and testUser1.wallet == 0)

def test_buyTicket_funds2():
	assert(testUser4.buyTicket(testTicket4)
		   and testUser4.inventory[-1] == testTicket4
	       and testTicket4.for_sale == False
	       and testUser4.wallet == 0)

def test_buyTicket_funds3():
	assert(testUser4.buyTicket(testTicket3)
		   and testTicket3 not in testUser4.inventory
	       and testTicket3.for_sale == True
	       and testUser4.wallet == 0)

def test_buyTicket_funds4():
	assert(testUser3.buyTicket(testTicket3)
		   and testTicket3 not in testUser3.inventory
	       and testTicket3.for_sale == False
	       and testUser3.wallet == 950)

#
# Test purchasing of tickets based on availability
#
def test_buyTicket_availability1():
	assert(testUser2.buyTicket(testTicket1)
		   and testTicket1 not in testUser2.inventory
	       and testTicket1.for_sale == False
	       and testUser2.wallet == 500)

def test_buyTicket_availability2():
	assert(testUser2.buyTicket(testTicket2)
		   and testTicket2 not in testUser2.inventory
	       and testTicket1.for_sale == False
	       and testUser2.wallet == 500)
