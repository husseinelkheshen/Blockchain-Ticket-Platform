from blockchain.Admit01_Blockchain import *
from datetime import datetime
from datetime import timedelta

date1 = datetime.now()
date2 = datetime.now() - timedelta(days=3)
date3 = datetime.now() + timedelta(years=2)
date4 = datetime.now() + timedelta(months=2)
date5 = datetime.now() + timedelta(seconds=49)
date6 = datetime.now() + timedelta(years=4)


def test_schedulerelease():
    venue = Venue("Max Palevsky", "Hyde Park")
    event = venue.createEvent("Rock Show", datetime.now() + timedelta(years=3),
                              "An event for students to rock out!")
    seat = Seat("General Admission", "N/A", 1)
    ticket = venue.createTicket(event, 20, seat)
    # Past dates should return false, but put ticket on sale
    assert venue.scheduleRelease(event, "General Admission", date1) is False
    assert len(event.scheduled) == 1
    assert ticket.isForSale() is True
    assert ticket.isScheduled is False
    ticket.for_sale = False
    # if the ticket is already for sale, return false, don't schedule
    assert venue.scheduleRelease(event, "General Admission", date2, 1) is False
    assert ticket.isForSale() is True
    assert ticket.isScheduled is False
    ticket.for_sale = False
    # future date should set isScheduled to True, but isForSale is still false
    assert venue.scheduleRelease(event, "General Admission", date3, 1) is True
    assert ticket.isForSale() is False
    assert ticket.isScheduled is True
    # if there are no more non-scheduled tickets, this should fail
    assert venue.scheduleRelease(event, "General Admission", date3, 1) is False
    seat2 = Seat("General Admission", "N/A", 2)
    ticket2 = venue.createTicket(event, 20, seat2)
    # added a second ticket, so this should pass
    # states of both tickets are the same
    assert venue.scheduleRelease(event, "General Admission", date4, 1) is True
    assert ticket.isForSale() is False
    assert ticket.isScheduled is True
    assert ticket2.isForSale() is False
    assert ticket2.isScheduled is True
    ticket.isScheduled = False
    ticket.for_sale = False
    ticket2.isScheduled = False
    ticket2.for_sale = False
    # if date is past the date of event, return false
    # for sale and scheduled remain false
    assert venue.scheduleRelease(event, "General Admission", date6, 2) is False
    assert ticket.isForSale() is False
    assert ticket2.isForSale() is False
    assert ticket.isScheduled is False
    assert ticket2.isScheduled is False
    # can schedule both tickets, both scheduled, neither for sale
    assert venue.scheduleRelease(event, "General Admission", date5, 2) is True
    assert ticket.isForSale() is False
    assert ticket2.isForSale() is False
    assert ticket.isScheduled is True
    assert ticket2.isScheduled is True
    ticket.isScheduled = False
    ticket2.isScheduled = False
    # if more tickets than are currently not scheduled are entered to be scheduled
    # we return false, but set any remaining non-scheduled tickets to scheduled
    assert venue.scheduleRelease(event, "General Admission", date4, 1) is True
    assert (ticket.isScheduled != ticket2.isScheduled) is True
    assert venue.scheduleRelease(event, "General Admission", date4, 2) is False
    assert (ticket.isScheduled != ticket2.isScheduled) is False
    seat100 = Seat("General Admission", "N/A", 100)
    seat101 = Seat("Balcony", "N/A", 101)
    ticket100 = venue.createTicket(event, 20, seat100)
    ticket101 = venue.createTicket(event, 20, seat101)
    # should return false, but schedule one
    assert venue.scheduleRelease(event, "Balcony", date4, 2) is False
    assert ticket100.isScheduled is False
    assert ticket101.isScheduled is True


def test_checkrelease():
    soon1 = date.datetime.now + date.timedelta(seconds=39)
    venue = Venue("Max Palevsky", "Hyde Park")
    event = venue.createEvent("Rock Show", datetime.now() + timedelta(years=3),
                              "An event for students to rock out!")
    seat = Seat("General Admission", "N/A", 1)
    seat2 = Seat("General Admission", "N/A", 2)
    seat3 = Seat("General Admission", "N/A", 3)
    seat4 = Seat("General Admission", "N/A", 4)
    ticket = venue.createTicket(event, 20, seat)
    venue.scheduleRelease(event, "General Admission", soon1, 1)
    sleep(40)
    # tests that the single ticket is released
    assert event.checkRelease() == 1
    ticket2 = venue.createTicket(event, 20, seat2)
    ticket3 = venue.createTicket(event, 20, seat3)
    ticket4 = venue.createTicket(event, 20, seat4)
    soon2 = date.datetime.now + timedelta(seconds=31)
    venue.scheduleRelease(event, "General Admission", soon2, 2)
    sleep(32)
    # tests that only 2 of the 3 are released
    assert event.checkRelease() == 2
