from blockchain.Admit01_Blockchain import *
from datetime import datetime
from datetime import timedelta

date1 = datetime.now()
date2 = datetime.now() - timedelta(days=3)
date3 = datetime.now() + timedelta(days=730)
date4 = datetime.now() + timedelta(days=60)
date5 = datetime.now() + timedelta(seconds=49)
date6 = datetime.now() + timedelta(days=1460)


def test_schedulerelease():
    venue = Venue("Max Palevsky", "Hyde Park")
    event = venue.createEvent("Rock Show", datetime.now() + timedelta(days=1095),
                              "An event for students to rock out!")
    seat = Seat("General Admission", "N/A", 1)
    ticket = venue.createTicket(event, 20, seat)
    # there are no balcony seats, so this will fail
    assert not venue.scheduleRelease(event, "Balcony", date2, 1)
    assert not ticket.isForSale()
    assert not ticket.isScheduled
    # Past dates should return false, but put ticket on sale
    assert not venue.scheduleRelease(event, "General Admission", date1, 1)
    assert ticket.isForSale()
    assert not ticket.isScheduled
    ticket.for_sale = False
    # if the ticket is already for sale, return false, don't schedule
    assert not venue.scheduleRelease(event, "General Admission", date2, 1)
    assert ticket.isForSale()
    assert not ticket.isScheduled
    ticket.for_sale = False
    # future date should set isScheduled to True, but isForSale is still false
    assert venue.scheduleRelease(event, "General Admission", date3, 1)
    assert not ticket.isForSale()
    assert ticket.isScheduled
    # if there are no more non-scheduled tickets, this should fail
    assert not venue.scheduleRelease(event, "General Admission", date3, 1)
    seat2 = Seat("General Admission", "N/A", 2)
    ticket2 = venue.createTicket(event, 20, seat2)
    assert not ticket2.isScheduled
    # setting number to a non-positive number returns false, does not schedule or release the ticket
    # so second ticket will not be scheduled
    assert not venue.scheduleRelease(event, "General Admission", date4, 0)
    assert not ticket2.isScheduled
    # this will pass since there is now a second ticket that still isnt scheduled
    assert venue.scheduleRelease(event, "General Admission", date4, 1)
    assert not ticket.isForSale()
    assert ticket.isScheduled
    assert not ticket2.isForSale()
    assert ticket2.isScheduled
    ticket.isScheduled = False
    ticket.for_sale = False
    ticket2.isScheduled = False
    ticket2.for_sale = False
    # if date is past the date of event, return false
    # for sale and scheduled remain false
    assert not venue.scheduleRelease(event, "General Admission", date6, 2)
    assert not ticket.isForSale()
    assert not ticket2.isForSale()
    assert not ticket.isScheduled
    assert not ticket2.isScheduled
    # can schedule both tickets, both scheduled, neither for sale
    assert venue.scheduleRelease(event, "General Admission", date5, 2)
    assert not ticket.isForSale()
    assert not ticket2.isForSale()
    assert ticket.isScheduled
    assert ticket2.isScheduled
    ticket.isScheduled = False
    ticket2.isScheduled = False
    # if more tickets than are currently not scheduled are entered to be scheduled
    # we return false, but set any remaining non-scheduled tickets to scheduled
    assert venue.scheduleRelease(event, "General Admission", date4, 1)
    assert (ticket.isScheduled != ticket2.isScheduled)
    assert not venue.scheduleRelease(event, "General Admission", date4, 2)
    assert not (ticket.isScheduled != ticket2.isScheduled)
    seat100 = Seat("General Admission", "N/A", 100)
    seat101 = Seat("Balcony", "N/A", 101)
    ticket100 = venue.createTicket(event, 20, seat100)
    ticket101 = venue.createTicket(event, 20, seat101)
    # should return false, but schedule one
    assert not venue.scheduleRelease(event, "Balcony", date4, 2)
    assert not ticket100.isScheduled
    assert ticket101.isScheduled


def test_checkrelease():
    soon1 = date.datetime.now() + timedelta(seconds=1)
    venue = Venue("Max Traplevsky", "Hyde Park Town")
    event = venue.createEvent("Rock Show", datetime.now() + timedelta(days=1095),
                              "An event for students to rock out!")
    seat = Seat("General Admission", "N/A", 1)
    seat2 = Seat("General Admission", "N/A", 2)
    seat3 = Seat("General Admission", "N/A", 3)
    seat4 = Seat("General Admission", "N/A", 4)
    ticket = venue.createTicket(event, 20, seat)
    venue.scheduleRelease(event, "General Admission", soon1, 1)
    sleep(1)
    # tests that the single ticket is released
    assert event.checkRelease() == 1
    ticket2 = venue.createTicket(event, 20, seat2)
    ticket3 = venue.createTicket(event, 20, seat3)
    ticket4 = venue.createTicket(event, 20, seat4)
    soon2 = date.datetime.now() + timedelta(seconds=1)
    venue.scheduleRelease(event, "General Admission", soon2, 2)
    sleep(1)
    # tests that only 2 of the 3 are released
    assert event.checkRelease() == 2
