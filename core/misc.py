def venue_location_to_string(venue_city, venue_state):
	venue_loc_str = venue_city.strip() + ', ' + venue_state.strip()
	return venue_loc_str

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

def parse_event_time(time):
	year=event_time.get('year')
	month=event_time.get('month')
	day=event_time.get('day')
	hour=event_time.get('hour')
	minute=event_time.get('minute')
	if year is None or month is None or day is None or hour is None or minute is None:
		return None
	dt = datetime(
		year=int(year),
		month=int(month),
		day=int(day),
		hour=int(hour),
		minute=int(minute))
	return dt