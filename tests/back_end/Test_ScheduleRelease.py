from blockchain.Admit01_Blockchain import *
from datetime import datetime
from datetime import timedelta
from time import sleep

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
    assert venue.scheduleRelease(event, "General Admission", date1, 1) is False
    assert ticket.isForSale() is True
    assert ticket.isScheduled is False
    ticket.for_sale = False
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
    sleep(50)
    # after time passes, tickets should now be for sale
    assert ticket.isForSale() is True
    assert ticket2.isForSale() is True
    assert ticket.isScheduled is False
    assert ticket2.isScheduled is False
    ticket.isScheduled = False
    ticket.for_sale = False
    ticket2.isScheduled = False
    ticket2.for_sale = False
    # if more tickets than are currently not scheduled are entered to be scheduled
    # we return false, but set any remaining non-scheduled tickets to scheduled
    assert venue.scheduleRelease(event, "General Admission", date4, 1) is True
    assert (ticket.isScheduled != ticket2.isScheduled) is True
    assert venue.scheduleRelease(event, "General Admission", date4, 2) is False
    assert (ticket.isScheduled != ticket2.isScheduled) is False


# def test_timercheck():

    """

    Schedule Release

    Enter a time to put a class of tickets on sale
    --requirements
        Make sure time is after current time
        Make sure time is of valid format
        Make sure tickets aren't already on sale
        Make sure timer check is functioning correctly
            Make sure it occurs synchronously
            Make sure that it evaluates appropriately per time type
            Edge cases include a time that is now in the past, current time, future time

    --implementation
        Check time is valid
        Check tickets aren't on sale already
        Send notification to people who may be interested (Explore)
        Call timerCheck function
    --timerCheck function
        Check if time is within a year,
        if so, call again within a month,
        if so, call again within a week,
        if so, call again within a day,
        if so, call again within an hour,
        if so, call again within a minute,
        if so, call again within a second
        Whenever one evaluates to false, sleep the function synchronously so that
        it sleeps concurrently with other actions, then perform the check again
        when the sleep is over
        When within a second evaluates to true, put all of the specified tickets up
        for sale and notify the people who may be interested
    """