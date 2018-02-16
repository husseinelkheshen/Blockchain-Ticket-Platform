from blockchain.Admit01_Blockchain import *
import datetime as date

import copy

#
# Creation of Peripheral Objects
#
testDatetime1 = date.datetime.now() + date.timedelta(days=7) # one week from now

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
testTicket1.listTicket(testTicket1.face_value, testVenue.id)

testTicket2 = testVenue.createTicket(testVenue.events[testEvent1.id][0], 500, testSeat2)
testTicket2.for_sale = False

testTicket3 = testVenue.createTicket(testVenue.events[testEvent1.id][0], 50, testSeat3)
testTicket3.listTicket(testTicket3.face_value, testVenue.id)

testTicket4 = testVenue.createTicket(testVenue.events[testEvent1.id][0], 0, testSeat4)
testTicket4.listTicket(testTicket4.face_value, testVenue.id)

testTicket5 = testVenue.createTicket(testVenue.events[testEvent1.id][0], 100, testSeat5)
testTicket5.listTicket(testTicket5.face_value, testVenue.id)

testTicket6 = testVenue.createTicket(testVenue.events[testEvent1.id][0], 0, testSeat6)
testTicket6.listTicket(testTicket6.face_value, testVenue.id)


#
# Test purchasing of tickets with funds in wallet
#
def test_buyTicket_funds1():
    assert testUser1.buyTicket(testTicket1)
    assert testUser1.inventory[-1] == testTicket1
    assert not testTicket1.for_sale
    assert testUser1.wallet == 0


def test_buyTicket_funds2():
    assert testUser4.buyTicket(testTicket4)
    assert testUser4.inventory[-1] == testTicket4
    assert not testTicket4.for_sale
    assert testUser4.wallet == 0


def test_buyTicket_funds3():
    assert not testUser4.buyTicket(testTicket3)
    assert testTicket3 not in testUser4.inventory
    assert testTicket3.for_sale
    assert testUser4.wallet == 0


def test_buyTicket_funds4():
    assert testUser3.buyTicket(testTicket3)
    assert testTicket3 in testUser3.inventory
    assert not testTicket3.for_sale
    assert testUser3.wallet == 950


#
# Test purchasing of tickets based on availability
#
def test_buyTicket_availability1():
    assert not testUser2.buyTicket(testTicket1)
    assert testTicket1 in testUser1.inventory
    assert testTicket1 not in testUser2.inventory
    assert not testTicket1.for_sale
    assert testUser2.wallet == 500


def test_buyTicket_availability2():
    assert not testUser2.buyTicket(testTicket2)
    assert testTicket2 not in testUser2.inventory
    assert not testTicket1.for_sale
    assert testUser2.wallet == 500
