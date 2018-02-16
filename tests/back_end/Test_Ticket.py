from blockchain.Admit01_Blockchain import *

#
# Creation of Test Objects
#
testDatetime1 = date.datetime(2018, 3, 31, 0, 0, 0, 0)
testDatetime2 = date.datetime(2017, 3, 31, 0, 0, 0, 0)

testSeat1 = Seat("Cheap Seats", "C", 5)

testEvent1 = Event("Class1", testDatetime1, "Tuesday and Thursday")
testEvent2 = Event("Class2", testDatetime2, "Tuesday and Thursday")

#
# Test construction with invalid events
#
def test_validEvent():
	assert not(Ticket(None, 1, testSeat1))

#
# Test construction with invalid price
#
def test_validValue1():
	assert not (Ticket(testEvent1, -1, testSeat1))

def test_validValue2():
	assert not (Ticket(testEvent1, None, testSeat1))

#
# Test construction with an event that has transpired
#
def test_validTime():
	assert not (Ticket(testEvent2, 1, testSeat1))

#
# Test construction with an invalid seat
#
def test_validSeat():
	assert not (Ticket(testEvent1, 1, None))

#
# Test normal construction
#
def test_normal():
	testTicket = (Ticket(testEvent1, 1, testSeat1))
	assert(testTicket.event == testEvent1
		   and testTicket.face_value == 1
		   and testTicket.list_price == 1
		   and testTicket.for_sale == False
		   and testTicket.history == None
           and testTicket.seat == testSeat1)
