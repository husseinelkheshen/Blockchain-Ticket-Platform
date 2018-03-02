import sys
sys.path.insert(0, '..')
from blockchain.Admit01_Blockchain import *
from misc import *
from datetime import datetime
import sys
Trackers.next_event_id = sys.maxsize-100000

print('download crap')
nltk.download('maxent_ne_chunker')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('words')
print('finished downloading crap')


def bc_create_venue(venue_name, venue_loc_str):
    # check if parameters are valid
    if (venue_loc_str is None or venue_name is None):
        return False
    v = Venue(venue_name, venue_loc_str)
    # check if venue creation succeeded
    if v.id is None:
        return False
    return v.id

def parse_venue(venue):
    # get venue
    if (venue is None):
        return None
    # get venue location
    venue_location = venue.get('venue_location')
    if venue_location is None:
        return None
    # get venue name
    venue_name = venue.get('venue_name')
    # get venue object
    v = bc_get_venue(venue_name, venue_location)
    return v


def bc_get_venue(venue_name, venue_loc_str):
    if venue_loc_str in Trackers.registered_venues:
        if venue_name in Trackers.registered_venues[venue_loc_str]:
            return Trackers.registered_venues[venue_loc_str][venue_name]
    return None

def bc_create_user(user_fname, user_lname, user_email):
    # check if parameters are valid
    if (user_fname is None or user_lname is None or user_email is None):
        return False
    u = User(user_fname, user_lname, user_email)
    # check if user creation succeeded
    if u.id is None:
        return False
    return u.id

def bc_create_event(event_id, event_name, event_desc, event_time, venue):
    # check if parameters are valid
    if (event_name is None or event_desc is None or event_time is None
        or event_id is None):
        return False
    dt = parse_event_time(event_time)
    e = venue.createEvent(event_name, dt, event_desc)
    if e is None:
        print('e is none')
        return False
    # change event id
    venue.events[event_id] = venue.events[e.id]
    del venue.events[e.id]
    e.id = event_id
    return e.id

def bc_get_event(venue, event_id):
    return venue.events[event_id][0]

def bc_create_tickets(section_name, min_row, max_row, min_seat, max_seat, event, venue, face_value):
    seat_nos = range(min_seat, max_seat)
    no_tickets = 0
    for row in range(min_row, max_row):
        no_tickets += len(venue.createTickets(event, face_value, section_name, str(row), seat_nos))
    return no_tickets

def bc_edit_event(venue, event, event_name, event_time, event_desc):
    dt = parse_event_time(event_time)
    return venue.manageEvent(event, event_name, dt, event_desc)

def bc_edit_tickets(venue, event, new_price, section, row, seat_num):
    print(new_price, section, row, seat_num)
    return venue.manageTickets(event, new_price, section, row, seat_num)

def bc_get_all_events(venue):
    return [e[0] for e in venue.events.values()]

def bc_list_tickets(venue, event, ticket_num):
    # if section is None and (row is not None or seat_num is not None):
    #     return False

    # if section is not None and row is None and seat_num is not None:
    #     return False
    
    ticketsListed = 0
    # print(len(event.tickets))
    for ticket in event.tickets:
        # print(ticket.seat.section)
        # if section == ticket.seat.section or section is None:
        #     # print(ticket.seat.row)
        #     if row == ticket.seat.row or row is None:
        #         print('ticket seat_num', ticket.seat.seat_no)
        #         print('seat_num', seat_num)
        #         if seat_num == ticket.seat.seat_no or seat_num is None:
        if ticket_num == ticket.ticket_num:
            print('success')
            ticketsListed+=(ticket.listTicket(ticket.face_value, venue.id))

    return ticketsListed

def bc_buy_ticket(venue, event, user, section, row, seat_num):
    for ticket in event.tickets:
        if ticket.seat.seat_no == seat_num and ticket.seat.row == row and ticket.seat.section == section:
            print("found ticket")
            return user.buyTicket(ticket) and ticket.ticket_num
    return False


def bc_search(user, text, date, date_range):
    if date is not None:
        month = date.get('month')
        year = date.get('year')
        day = date.get('day')
        if month is None or year is None or day is None:
            return []
        dt = datetime(month=month, day=day, year=year)
    else:
        dt = None
    print(text)
    return user.search(text=(text or ""), datetime=dt, date_range=(date_range or 0))

def bc_explore(user):
    return user.explore()

def bc_schedule_release(venue, event, section, release_date):
    if release_date is not None:
        month = release_date.get('month')
        year = release_date.get('year')
        day = release_date.get('day')
        if month is None or year is None or day is None:
            return False
        dt = datetime(month=month, day=day, year=year)
    else:
        dt = None

    return venue.scheduleRelease(event, section, dt, len(event.tickets))