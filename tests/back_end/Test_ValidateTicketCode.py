from blockchain.Admit01_Blockchain import *
from datetime import datetime
from datetime import timedelta

def test_validateticketcode():
    venue = Venue("Max Palevsky", "Hyde Park")
    event = venue.createEvent("Rock Show", datetime.now() + timedelta(hours=4),
                              "An event for students to rock out!")
    seat = Seat("General Admission", "N/A", 1)
    ticket = venue.createTicket(event, 20, seat)
    user1 = User("Ethan", "Reeder", "er@example.com")
    user2 = User("Ross", "Piper", "rp@example.com")
    user1.wallet = 100000
    user2.wallet = 100000
    ticket.listTicket(ticket.face_value, venue.id)
    user1.buyTicket(ticket)
    # checks original purchaser still holds ticket, true
    assert venue.validateTicketCode(event.id, ticket.ticket_num,
                                    user1.id, event.blockchain.blocks[-1].hash)
    # checks bogus event id doesn't pass
    assert not venue.validateTicketCode(event.id + 5, ticket.ticket_num, user1.id, event.blockchain.blocks[-1].hash)
    # checks invalid ticket number doesnt pass
    assert not venue.validateTicketCode(event.id, ticket.ticket_num + 1, user1.id, event.blockchain.blocks[-1].hash)
    ticket.listTicket(21, user1.id)
    user2.buyTicket(ticket)
    # checks that user1 can no longer use their code, as the ids dont match, even with a current hash
    assert not venue.validateTicketCode(event.id, ticket.ticket_num, user1.id, event.blockchain.blocks[-1].hash)
    # checks that someone cannot spoof user2's id, with a previously correct hash
    assert not venue.validateTicketCode(event.id, ticket.ticket_num, user2.id, event.blockchain.blocks[-2].hash)
    # check the the second user's code now works
    assert venue.validateTicketCode(event.id, ticket.ticket_num, user2.id, event.blockchain.blocks[-1].hash)
    event2 = venue.createEvent("Pop Show", datetime.now() + timedelta(hours=14), "An event for students to pop out!")
    ticket2 = venue.createTicket(event2, 20, seat)
    ticket2.listTicket(20, venue.id)
    user1.buyTicket(ticket2)
    # event2 is too far away to check in for
    assert not venue.validateTicketCode(event2.id, ticket.ticket_num, user1.id, event2.blockchain.blocks[-1].hash)
    user3 = User("Hayden", "Mans", "hm@example.com")
    user3.wallet = 100000
    # a user who never owned the ticket can't just sub their id into a qr code
    assert not venue.validateTicketCode(event.id, ticket.ticket_num, user3.id, event.blockchain.blocks[-1].hash)
    event.blockchain.blocks[-1].data[0].target = user3.id
    # even if the user is able to change the target of the transaction in the blockchain, the chain will not
    # pass validation tests, thus the validation of the code will fail
    assert not venue.validateTicketCode(event.id, ticket.ticket_num, user3.id, event.blockchain.blocks[-1].hash)


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