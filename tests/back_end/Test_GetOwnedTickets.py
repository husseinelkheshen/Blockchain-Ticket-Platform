from blockchain.Admit01_Blockchain import *
from datetime import timedelta

def test_getownedtickets():
    user1 = User("Ethan", "Reeder", "er@example.com")
    user2 = User("Ross", "Piper", "rp@example.com")
    margin = date.timedelta(days=3)
    event = Event("sample event", date.datetime.now() + margin, "an event")
    ticket1 = Ticket(event, 20, 1)
    ticket2 = Ticket(event, 30, 2)
    ticket3 = Ticket(event, 30, 3)
    ticket4 = Ticket(event, 30, 4)
    ticket5 = Ticket(event, 30, 5)
    user1.inventory.append(ticket1)
    user2.inventory.append(ticket2)
    user2.inventory.append(ticket3)
    # the following tests make sure that getOwnedTickets properly tracks changes
    # in the user's inventory
    assert(user1.getOwnedTickets() == [0])
    assert(user2.getOwnedTickets() == [1, 2])
    user1.inventory.append(ticket4)
    user2.inventory.append(ticket5)
    assert(user1.getOwnedTickets() == [0,3])
    assert(user2.getOwnedTickets() == [1, 2, 4])
    user2.inventory.pop(1)
    assert(user2.getOwnedTickets() == [1,4])
    user1.inventory.append(ticket3)
    assert(user1.getOwnedTickets() == [0, 3, 2])
