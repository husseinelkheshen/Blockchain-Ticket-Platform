from blockchain.Admit01_Blockchain import *
from misc import venue_location_to_string
from datetime import datetime

def bc_create_venue(venue_name, venue_city, venue_loc_str):
	# check if parameters are valid
	if (venue_city is None or venue_state is None or venue_name is None):
		return False
	v = Venue(venue_name, venue_loc_str)
	# check if venue creation succeeded
	if v.id is None:
		return False
	return v.id

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
	dt = datetime(
		year=event_time.get('year'),
		month=event_time.get('month'),
		day=event_time.get('day'),
		hour=event_time.get('hour'),
		minute=event_time.get('minute'))
	e = venue.createEvent(event_name, dt, event_desc)
	if e is None:
		return False
	# change event id
	del venue.events[e.id]
	e.id = event_id
	venue.events[event_id] = e
	return e.id

def bc_get_event(event_id, venue):
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
	return venue.manageTickets(event, new_price, section, row, seat_num)

def bc_get_all_events(venue):
	return [e[0] for e in venue.events.values()]

