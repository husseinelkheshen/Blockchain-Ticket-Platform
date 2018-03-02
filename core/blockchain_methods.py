import sys
sys.path.insert(0, '..')
from blockchain.Admit01_Blockchain import *
from misc import *
from datetime import datetime
import sys
Trackers.next_event_id = sys.maxsize-100000

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

def bc_list_tickets(venue, event, section, row, seat_num):
    if section is None and (row is not None or seat_num is not None):
        return False

    if section is not None and row is None and seat_num is not None:
        return False
    
    ticketsListed = 0
    print(len(event.tickets))
    for ticket in event.tickets:
        print(ticket.seat.section)
        if section == ticket.seat.section or section is None:
            print(ticket.seat.row)
            if row == ticket.seat.row or row is None:
                print(ticket.seat.seat_no)
                if seat_num == ticket.seat.seat_no or seat_num is None:
                    ticketsListed += ticket.listTicket(venue.id, ticket.face_value)

    return ticketsListed




