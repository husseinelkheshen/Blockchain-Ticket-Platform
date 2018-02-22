from blockchain.Admit01_Blockchain import *
from datetime import datetime
from datetime import timedelta

def test_validateticketcode():
    venue = Venue("Max Palevsky", "Hyde Park")
    event = venue.createEvent("Rock Show", datetime.now() + timedelta(years=3),
                              "An event for students to rock out!")
    seat = Seat("General Admission", "N/A", 1)
    ticket = venue.createTicket(event, 20, seat)
    user1 = User("Ethan", "Reeder", "er@example.com")
    user2 = User("Ross", "Piper", "rp@example.com")
    user1.wallet = 100000
    user2.wallet = 100000
    ticket.for_sale = True
    user1.buyTicket(ticket)
    qrcode = user1.generateTicketCode(venue, event, ticket)
    # checks original purchaser still holds ticket, true
    assert venue.validateTicketCode(event.id, ticket.ticket_num,
                                    ticket.mostRecentTransaction().target, event.blockchain[-1].hash, qrcode) is True
    ticket.listTicket(21, user1.id)
    user2.buyTicket(ticket)
    # checks when user sells ticket that the code no longer works
    assert venue.validateTicketCode(event.id, ticket.ticket_num, ticket.mostRecentTransaction().target, event.blockchain[-1].hash, qrcode) is False
    qrcode = user2.generateTicketCode(venue, event, ticket)
    # check the the second user's code now works
    assert venue.validateTicketCode(event.id, ticket.ticket_num, ticket.mostRecentTransaction().target, event.blockchain[-1].hash, qrcode) is True
    user3 = User("Hayden", "Mans", "hm@example.com")
    seat2 = Seat("General Admission", "N/A", 2)
    ticket2 = venue.createTicket(event, 20, seat2)
    ticket2.for_sale = True
    # check that once a new transaction occurs (genesis transaction in this case) that the code no longer works
    assert venue.validateTicketCode(event.id, ticket.ticket_num, ticket.mostRecentTransaction().target, event.blockchain[-1].hash, qrcode) is False
    qrcode = user2.generateTicketCode(venue, event, ticket)
    # check that second user's code is now valid
    assert venue.validateTicketCode(event.id, ticket.ticket_num, ticket.mostRecentTransaction().target, event.blockchain[-1].hash, qrcode) is True
    user3.buyTicket(ticket2)
    # check that a user buying another ticket invalidates this previous code
    assert venue.validateTicketCode(event.id, ticket.ticket_num, ticket.mostRecentTransaction().target, event.blockchain[-1].hash, qrcode) is False
    qrcode = user3.generateTicketCode(venue, event, ticket2)
    # checks the user3's code is valid now
    assert venue.validateTicketCode(event.id, ticket2.ticket_num, ticket2.mostRecentTransaction().target, event.blockchain[-1].hash, qrcode) is True
    qrcode = user1.generateTicketCode(venue, event, ticket)
    # checks that a user that does not own the ticket cannot create a valid code on a ticket he doesn't own
    assert venue.validateTicketCode(event.id, ticket.ticket_num, ticket.mostRecentTransaction().target, event.blockchain[-1].hash, qrcode) is False

"""
Validate Ticket Code

Check that a given QR code contains up-to-date content
--requirements
    Verify that the checks in the implementation portion evaluate as expected

--implementation
    Verify that a venue with this id exists, and that it matches the id of the checking venue
    Verify that this venue has an event with this id, and the time is appropriate
    Verify that this event has a ticket with this id
    Verify that the owner of this ticket is the same as the code states
"""