from blockchain.Admit01_Blockchain import *
import datetime as date

valid_date = date.datetime.now() + timedelta(days = 7)

testSeat1 = Seat("Cheap Seats", "C", 5)
testSeat2 = Seat("Cheap Seats", "B", 5)
testSeat3 = Seat("Cheap Seats", "C", 6)

testEvent1 = Event("Class1", valid_date, "Tuesday and Thursday")

ticket1 = Ticket(testEvent1, 50, testSeat1)
ticket2 = Ticket(testEvent1, 70, testSeat2)
ticket3 = Ticket(testEvent1, 90, testSeat3)

