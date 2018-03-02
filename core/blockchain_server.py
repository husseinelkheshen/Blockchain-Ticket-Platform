from flask import Flask
from flask_restful import Resource, Api
from flask import request, jsonify, status
from blockchain_methods import *

app = Flask(__name__)
# api = Api(app)
venue_i = 0

def bad_request(reason):
	content = {'reason': reason}
    return content, status.HTTP_400_BAD_REQUEST

def good_request(content):
	return content, status.HTTP_200_OK


"""
{
	"venue_location": String,
	"venue_name": String
}
"""
@app.route("/venue/create", methods=['POST'])
def venue_create():
	venue_name = request.json.get('venue_name')
	venue_location = request.json.get('venue_location')
	if venue_name is None or venue_location is None:
		return bad_request('Bad parameters')
	vid = bc_create_venue(venue_name, venue_location)
	if vid is False:
		return bad_request('Creating venue failed')
	return good_request({'venue_id': vid})

"""
{
	fname: String,
    lname: String,
    email_address: String
}
"""
@app.route("/user/create", methods=['POST'])
def user_create():
	user_fname = request.json.get('fname')
	user_lname = request.json.get('lname')
	email_address = request.json.get('email_address')
	if user_fname is None or user_lname is None or email_address is None:
		return bad_request('Bad user parameters')
	uid = bc_create_user(user_fname, user_lname, email_address)
	if uid is False:
		return bad_request('Creating user failed')
	return good_request({'user_id': uid})

"""
Input:
{
	venue: {
		"venue_location": String,
		"venue_name": String
	},
	name: String,
	description: String,
	event_id: Integer,
	time: {
		minute: Integer,
		hour: Integer,
		day: Integer,
		month: Integer,
		year: Integer
	}
}
Output:
{
	'event_id': Integer
}
"""
@app.route("/venue/event/create", methods=['POST'])
def event_create():
	# get venue
	venue = request.json.get('venue')
	if (venue is None):
		return bad_request('Need venue')

	# get venue location
	venue_location = venue.get('venue_location')
	if venue_location is None:
		return bad_request('Need venue location')

	# get venue name
	venue_name = venue.get('venue_name')

	# get venue object
	v = bc_get_venue(venue_name, venue_location)
	if v is None:
		return bad_request('Venue does not exist')
	
	# get event details
	event_name = request.json.get('name')
	event_desc = request.json.get('description')
	event_time = request.json.get('time')
	event_id = int(request.json.get('event_id'))
	
	if event_name is None:
		return bad_request('Need event name')
	if event_desc is None:
		return bad_request('Need event description')
	if event_time is None:
		return bad_request('Need event time')
	
	# create event
	eid = bc_create_event(event_id, event_name, event_desc, event_time, v)
	if eid is False:
		return bad_request('Creating event failed')
	return good_request({'event_id': eid})


"""
Input:
{
	venue: {
		"venue_location": String,
		"venue_name": String
	},
	event_id: Integer,
	tickets_info: {
		"face_value": Integer,
		"section": String,
		"row_range": {
			begin: Integer,
			end: Integer
		},
		"seat_range": {
			"begin": Integer,
			"end": Integer
		},
	}
}
Output:
{
	"no_tickets_created": Integer
}
"""
@app.route("/venue/event/tickets/create", methods=['POST'])
def tickets_create():
	# get venue
	venue = request.json.get('venue')
	if (venue is None):
		return bad_request('Need venue')

	# get venue location
	venue_location = venue.get('venue_location')
	if venue_location is None:
		return bad_request('Need venue location')

	# get venue name
	venue_name = venue.get('venue_name')

	# get venue object
	v = bc_get_venue(venue_name, venue_location)
	if v is None:
		return bad_request('Venue does not exist')

	# get event
	event_id = request.json.get('event_id')
	if (event_id is None):
		return bad_request('Event does not exist')

	# get event object
	e = bc_get_event(event_id)

	# get ticket info
	ticket_info = json.get('tickets_info')
	if (ticket_info is None):
		return bad_request('Need ticket information')

	# get ticket value
	face_value = int(ticket_info.get('face_value'))

	# get section name
	section_name = ticket_info.get('section')

	# get row range
	min_row = tickets_info.get('row_range')['begin']
	max_row = tickets_info.get('row_range')['end']

	# get seat range
	min_seat = tickets_info.get('seat_range')['begin']
	max_seat = tickets_info.get('seat_range')['end']

	# create tickets
	no_tickets_created = bc_create_tickets(section_name, min_row, max_row, min_seat, max_seat, e, v, face_value):

	return good_request({'no_tickets_created': no_tickets_created})


"""
Input:
{
	venue: {
		"venue_location": String,
		"venue_name": String
	},
	event_id: Integer,
	update_info : {
		name(+): String,
		time(+): {
			minute: Integer,
			hour: Integer,
			day: Integer,
			month: Integer,
			year: Integer
		},
		desc(+): String
	}
}
Output:
{
	"no_tickets_created": Integer
}
"""
@app.route("/venue/event/edit", methods=['POST'])
def event_edit():
	# get venue
	venue = request.json.get('venue')
	if (venue is None):
		return bad_request('Need venue')

	# get venue object
	v = parse_venue(venue)
	if v is None:
		return bad_request('Venue does not exist')

	# get event id
	event_id = request.json.get('event_id')
	if (event_id is None):
		return bad_request('Event does not exist')

	# get event object
	e = bc_get_event(event_id)

	update_info = request.json.get('update_info')
	if update_info is None:
		return bad_request('Need update_info')
	name = update_info.get('name')
	time = update_info.get('time')
	desc = update_info.get('desc')

	if not bc_edit_event(v, e, name, time, desc or e.desc):
		return bad_request('Update failed')
	return good_request({'event_id': e.id})

"""
Edit Ticket price by section, row and seat number
No seat number means all seats in the row and section get updated
No seat number and no row means all in the section get updated
No anything means all tickets in the event get updated
Input:
{
	venue: {
		"venue_location": String,
		"venue_name": String
	},
	event_id: Integer,
	update_info : {
		new_price: Number,
		which_seats: {
			section(+): String,
			row(+): Integer,
			seat_num(+): Integer
		}
	}
}
Output:
{
}
"""
@app.route("/venue/event/tickets/edit", methods=['POST'])
def tickets_edit():
	# get venue
	venue = request.json.get('venue')
	if (venue is None):
		return bad_request('Need venue')

	# get venue object
	v = parse_venue(venue)
	if v is None:
		return bad_request('Venue does not exist')

	# get event id
	event_id = request.json.get('event_id')
	if (event_id is None):
		return bad_request('Event does not exist')

	# get event object
	e = bc_get_event(event_id)

	update_info = request.json.get('update_info')
	if update_info is None:
		return bad_request('Need update_info')
	new_price = update_info.get('new_price')
	if new_price is None:
		return bad_request('Need a new price')
	which_seats = update_info.get('which_seats')
	if which_seats is None:
		return bad_request('Need update_info.which_seats')
	section = update_info.get('section')
	row = update_info.get('row')
	seat_num = update_info.get('seat_num')
	if seat_num is not None:
		seat_num = int(seat_num)

	if not bc_edit_tickets(v, e, new_price, section, row, seat_num):
		return bad_request('Updating tickets failed')
	return good_request({})

"""
List all of a venues events
Input:
{
	venue: {
		"venue_location": String,
		"venue_name": String
	}
}
Output:
{
	'event_id': Integer, 
	'name': String, 
	'desc': String,
	'num_scheduled_tickets': len(e.scheduled)
}
"""
@app.route("/venue/view_events", methods=['POST'])
def venue_view_events():
	# get venue
	venue = request.json.get('venue')
	if (venue is None):
		return bad_request('Need venue')

	# get venue object
	v = parse_venue(venue)
	if v is None:
		return bad_request('Venue does not exist')

	# create list of events
	events = bc_get_all_events(v)
	ret = []
	for e in events:
		e_dict = {'event_id': e.id, 'name': e.name, 'desc': e.desc,
		'num_scheduled_tickets': len(e.scheduled)}
		ret.append(e_dict)

	return good_request(ret)




if __name__ == "__main__":
    app.run(debug=True)
