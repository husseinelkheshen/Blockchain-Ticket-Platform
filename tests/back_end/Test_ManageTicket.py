from blockchain.Admit01_Blockchain import *
import datetime as date

valid_date = date.datetime.now() + timedelta(days = 7)

testSeat1 = Seat("Cheap Seats", "C", 5)
testEvent1 = Event("Class1", valid_date, "Tuesday and Thursday")

ticket1 = Ticket(testEvent1, 50, testSeat1)