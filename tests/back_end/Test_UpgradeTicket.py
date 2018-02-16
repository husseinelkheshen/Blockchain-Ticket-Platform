from blockchain.Admit01_Blockchain import *
import datetime as date
import copy

#
# Creation of Peripheral Objects
#
testDatetime1 = date.datetime.now() + date.timedelta(days=7)

testSeat1 = Seat("Cheap Seats", "C", 5)
testSeat2 = Seat("Steak Sauce", "A", 1)
testSeat3 = Seat("Steak Sauce", "B", 2)
testSeat4 = Seat("Steak Sauce", "C", 3)
testSeat5 = Seat("Steak Sauce", "D", 4)
testSeat6 = Seat("Steak Sauce", "E", 5)
testSeat7 = Seat("Steak Sauce", "F", 6)
testSeat8 = Seat("Steak Sauce", "G", 7)
testSeat9 = Seat("Steak Sauce", "H", 8)

#
# Creation of Test Venue
#
testVenue = Venue("venue", "DC")

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

testEvent2 = Event("Class2", testDatetime1, "Tuesday and Thursday")
testEvent2.venue = testVenue
testEvent2.id = 3
testVenue.events[testEvent2.id] = (testEvent2, copy.deepcopy(testEvent2.blockchain))

#
# Creation of Test Tickets
#
testTicket1 = testVenue.createTicket(testEvent1, 100, testSeat1)
testTicket1.listTicket(testTicket1.face_value, testVenue.id)

testTicket2 = testVenue.createTicket(testEvent1, 550, testSeat2)
testTicket2.for_sale = False

testTicket3 = testVenue.createTicket(testEvent1, 500, testSeat3)
testTicket3.listTicket(testTicket3.face_value, testVenue.id)

testTicket4 = testVenue.createTicket(testEvent1, 0, testSeat4)
testTicket4.listTicket(testTicket4.face_value, testVenue.id)

testTicket5 = testVenue.createTicket(testEvent1, 100, testSeat5)
testTicket5.listTicket(testTicket5.face_value, testVenue.id)

testTicket6 = testVenue.createTicket(testEvent2, 200, testSeat6)
testTicket6.listTicket(testTicket6.face_value, testVenue.id)

testTicket7 = testVenue.createTicket(testEvent2, 600, testSeat7)
testTicket7.listTicket(testTicket7.face_value, testVenue.id)

testTicket8 = testVenue.createTicket(testEvent1, 100, testSeat8)
testTicket8.listTicket(testTicket8.face_value, testVenue.id)

testTicket9 = testVenue.createTicket(testEvent1, 100, testSeat9)
testTicket9.listTicket(testTicket9.face_value, testVenue.id)

#
# Test upgrading tickets validly for sale
#
def test_upgradeTicket_valid1():
	testUser3.buyTicket(testTicket1)
	assert testUser3.upgradeTicket(testTicket1, testTicket3)
	assert testUser3.wallet == 500
	assert testUser3.inventory[0] == testTicket3
	assert testTicket1.for_sale == True
	assert testTicket2.for_sale == False

#
# Test upgrading tickets between different events
#
def test_upgradeTicket_valid2():
	testUser2.buyTicket(testTicket5)
	assert not testUser2.upgradeTicket(testTicket5, testTicket6)
	assert testUser2.wallet == 400
	assert testUser2.inventory[0] == testTicket5

#
# Test upgrading tickets user does not own
#
def test_upgradeTicket_unowned():
	assert not testUser4.upgradeTicket(testTicket6, testTicket4)

#
# Test upgrading tickets not for sale
#
def test_upgradeTicket_notforsale():
	assert not testUser3.upgradeTicket(testTicket3, testTicket2)

#
# Test upgrading tickets that are worth less than current
#
def test_upgradeTicket_less():
	assert not testUser3.upgradeTicket(testTicket3, testTicket4)

#
# Test upgrading invalid tickets
#
def test_upgradeTicket_invalid():
	assert not testUser3.upgradeTicket(testTicket3, None)

#
# Test upgrading tickets for events that have transpired
#
def test_upgradeTicket_transpired():
	assert not testUser3.upgradeTicket(testTicket3, testTicket7)

#
# Test upgrading tickets equal to current
#
def test_upgradeTicket_equal():
	testUser1.buyTicket(testTicket8)
	assert not testUser1.upgradeTicket(testTicket8, testTicket9)
