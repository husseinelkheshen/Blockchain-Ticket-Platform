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
	"venue_location": {
		"city": String,
		"state": String
	},
	"venue_name": String
}
"""
@app.route("/venue/create", methods=['POST'])
def venue_create():
	venue_name = request.json.get('venue_name')
	venue_location = request.json.get('venue_location')
	if venue_name is None or venue_location is None:
		return bad_request('Bad parameters\n {\n"venue_location": {\n"city": String,\n"state": String},\n"venue_name": String\n}')
	venue_city = venue_location.get('city')
	venue_state = venue_location.get('state')
	vid = bc_create_venue(venue_name, venue_city, venue_state)
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
{
	venue: {
		"venue_location": {
			"city": String,
			"state": String
		},
		"venue_name": String
	},
	name: String,
	description: String,
	time: {
		minute: Integer,
		hour: Integer,
		day: Integer,
		month: Integer,
		year: Integer
	}
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

	venue_city = venue_location.get('city')
	venue_state = venue_location.get('state')

	# get venue name
	venue_name = venue.get('venue_name')

	# get venue object
	v = bc_get_venue(venue_name, venue_city, venue_state)
	if v is None:
		return bad_request('Venue doesn\'t exist')
	
	# get event details
	event_name = request.json.get('name')
	event_desc = request.json.get('description')
	event_time = request.json.get('time')
	
	if event_name is None:
		return bad_request('Need event name')
	if event_desc is None:
		return bad_request('Need event description')
	if event_time is None:
		return bad_request('Need event time')
	
	# create event
	eid = bc_create_event(event_name, event_desc, event_time, venue)
	if eid is False:
		return bad_request('Creating event failed')
	return good_request({'event_id': eid})



# api.add_resource(TicketList, "/tickets")
# api.add_resource(TicketCreate, "/tickets/create")
# api.add_resource(Ticket, "/tickets/<ticket_id>")

if __name__ == "__main__":
    app.run(debug=True)
