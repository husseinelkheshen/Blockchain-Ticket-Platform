from blockchain.Admit01_Blockchain import *
from misc import venue_location_to_string
from datetime import datetime

def bc_create_venue(venue_name, venue_city, venue_state):
	# check if parameters are valid
	if (venue_city is None or venue_state is None or venue_name is None):
		return False
	venue_loc_str = venue_location_to_string(venue_city, venue_state)
	v = Venue(venue_name, venue_loc_str)
	# check if venue creation succeeded
	if v.id is None:
		return False
	return v.id

def bc_get_venue(venue_name, venue_city, venue_state):
	venue_loc_str = venue_location_to_string(venue_city, venue_state)
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

def bc_create_event(event_name, event_desc, event_time, venue):
	# check if parameters are valid
	if (event_name is None or event_desc is None or event_time is None):
		return False
	dt = datetime(
		year=event_time.get('year'),
		month=event_time.get('month'),
		day=event_time.get('day'),
		hour=event_time.get('hour'),
		minute=event_time.get('minute'))
	e = Event(event_name, dt, event_desc)
	if e.id is None:
		return False
	return e.id
