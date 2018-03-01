from blockchain.Admit01_Blockchain import *

testSeat1 = Seat("Cheap Seats", "C", 5)
testSeat2 = Seat("Cheap Seats", "B", 5)
testSeat3 = Seat("Cheap Seats", "C", 6)
testSeat4 = Seat("Dank Seats", "C", 5)

venue1 = Venue("Wrigley Field", "Chicago, IL")
venue1.createEvent("Lady Gaga", valid_date, "Stadium world tour")

venue1.createTicket(venue1.events[0][0], 50, testSeat1)
venue1.createTicket(venue1.events[0][0], 70, testSeat2)
venue1.createTicket(venue1.events[0][0], 90, testSeat3)
venue1.createTicket(venue1.events[0][0], 30, testSeat4)