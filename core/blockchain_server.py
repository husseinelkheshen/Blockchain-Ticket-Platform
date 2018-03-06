from flask import Flask
from flask import send_file
from flask import request, jsonify
from blockchain_methods import *
from misc import parse_events

app = Flask(__name__)
# api = Api(app)
venue_i = 0

def bad_request(reason):
    content = {'reason': reason}
    return jsonify(content), 400

def good_request(content):
    return jsonify(content), 200


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
    "fname": String,
    "lname": String,
    "email_address": String
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
        minute: Integer [0-59],
        hour: Integer [0-23],
        day: Integer [1-31],
        month: Integer [1-12],
        year: Integer [1-infinity)
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
    event_id = request.json.get('event_id')
    
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
    "venue": {
        "venue_location": String,
        "venue_name": String
    },
    "event_id": Integer,
    "tickets_info": {
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
    e = bc_get_event(v, event_id)

    # get ticket info
    tickets_info = request.json.get('tickets_info')
    if (tickets_info is None):
        return bad_request('Need ticket information')

    # get ticket value
    face_value = int(tickets_info.get('face_value'))

    # get section name
    section_name = tickets_info.get('section')

    # get row range
    min_row = tickets_info.get('row_range')['begin']
    max_row = tickets_info.get('row_range')['end']

    # get seat range
    min_seat = tickets_info.get('seat_range')['begin']
    max_seat = tickets_info.get('seat_range')['end']

    # create tickets
    no_tickets_created = bc_create_tickets(section_name, min_row, max_row, min_seat, max_seat, e, v, face_value)

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
    e = bc_get_event(v, event_id)

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
    e = bc_get_event(v, event_id)

    update_info = request.json.get('update_info')
    if update_info is None:
        return bad_request('Need update_info')
    new_price = update_info.get('new_price')
    if new_price is None:
        return bad_request('Need a new price')
    which_seats = update_info.get('which_seats')
    if which_seats is None:
        return bad_request('Need update_info.which_seats')
    section = which_seats.get('section')
    row = which_seats.get('row')
    seat_num = which_seats.get('seat_num')
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
[
    {
        'event_id': Integer, 
        'name': String, 
        'desc': String,
        'num_scheduled_tickets': Integer
    }
]
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
    ret = parse_events(events)

    return good_request(ret)

"""
View all tickets for an event
Input:
{
    venue: {
        venue_location: String,
        venue_name: String
    },
    event_id: Integer
}
Output:
[
    {
        'ticket_num': Integer, 
        'event_id': Integer,
        'face_value': Number, 
        'list_price': Number,
        'for_sale': Bool, 
        'is_scheduled': Bool,
        'seat': 
            {
                'seat_no': Integer, 
                'row': String, 
                'section': String
            }
    }
]
"""
@app.route("/venue/event/view_tickets", methods=['POST'])
def event_view_tickets():
    # get venue
    venue = request.json.get('venue')
    if (venue is None):
        return bad_request('Need venue')

    # get venue object
    v = parse_venue(venue)
    if v is None:
        return bad_request('Venue does not exist')

    # get event
    event_id = request.json.get('event_id')
    e = bc_get_event(v, event_id)
    if e is None:
        return bad_request('Event does not exist')

    ret = []
    for t in e.tickets:
        seat = t.seat
        seat_dict = {'seat_no': seat.seat_no, 'row': seat.row, 'section': seat.section}
        t_dict = {'ticket_num': t.ticket_num, 'event_id': t.event.id,
            'face_value': t.face_value, 'list_price': t.list_price,
            'for_sale': t.for_sale, 'is_scheduled': t.isScheduled,
            }
        t_dict['seat'] = seat_dict
        t_dict['listed'] = t.for_sale
        ret.append(t_dict)
    return good_request(ret)


"""
List tickets for an event
Input:
{
    venue: {
        venue_location: String,
        venue_name: String
    },
    event_id: Integer,
    list_info: {
        which_seats: {
            section(+): String,
            row(+): String,
            seat_num(+): Integer
        }
    }
}
Output:
{
        
}
"""
@app.route("/venue/event/tickets/list", methods=['POST'])
def tickets_list():
    # get venue
    venue = request.json.get('venue')
    if (venue is None):
        return bad_request('Need venue')

    # get venue object
    v = parse_venue(venue)
    if v is None:
        return bad_request('Venue does not exist')

    # get event
    event_id = request.json.get('event_id')
    e = bc_get_event(v, event_id)
    if e is None:
        return bad_request('Event does not exist')

    # list_info = request.json.get('list_info')
    ticket_num = request.json.get('ticket_num')
    # if list_info is None:
    #     return bad_request('Need list_info')
    # which_seats = list_info.get('which_seats')
    # if which_seats is None:
    #     return bad_request('Need list_info.which_seats')
    # section = which_seats.get('section')
    # row = which_seats.get('row')
    # seat_num = which_seats.get('seat_num')

    ticketsListed = bc_list_tickets(v, e, ticket_num)
    return good_request({"num_tickets_listed": ticketsListed or 0})

"""
Let a user list tickets for resale
Input:
{
    venue: {
        venue_location: String,
        venue_name: String
    },
    user_email: String,
    event_id: Integer,
    ticket_num: Integer
}
Output:
{
        
}
"""
@app.route("/user/list_ticket", methods=['POST'])
def tickets_user_list():
    # get venue
    venue = request.json.get('venue')
    if (venue is None):
        return bad_request('Need venue')

    # get venue object
    v = parse_venue(venue)
    if v is None:
        return bad_request('Venue does not exist')

    # get event
    event_id = request.json.get('event_id')
    e = bc_get_event(v, event_id)
    if e is None:
        return bad_request('Event does not exist')

    # get user email
    user_email = request.json.get('user_email')
    u = Trackers.registered_users.get(user_email)
    if u is None:
        return bad_request('User does not exist')

    # get ticket_num
    ticket_num = request.json.get('ticket_num')

    ticketsListed = bc_list_tickets(u, e, ticket_num)
    if ticketsListed is not False:
        return good_request({"num_tickets_listed": ticketsListed})
    return bad_request("Listing failed")

"""
View information for a single event
Input:
{
    "event_id": Integer,
    "ticket_num": Integer,
    "user_email": String,
    "hash": String,
    "venue": 
    {
        "venue_location": String,
        "venue_name": String
    }
}
Output:
{}
"""
@app.route("/venue/event/tickets/validate", methods=['POST'])
def venue_ticket_validate():
    # get venue
    venue = request.json.get('venue')
    if (venue is None):
        return bad_request('Need venue')

    # get venue object
    v = parse_venue(venue)
    if v is None:
        return bad_request('Venue does not exist')

    # get event
    event_id = request.json.get('event_id')
    e = bc_get_event(v, event_id)
    if e is None:
        return bad_request('Event does not exist')

    # get user email
    user_email = request.json.get('user_email')
    u = Trackers.registered_users.get(user_email)
    if u is None:
        return bad_request('User does not exist')
    
    # get hash
    h = request.json.get('hash')
    ticket_num = request.json.get('ticket_num')


    if bc_validate_ticket(v, e, ticket_num, u, h):
        return good_request({})
    else:
        return bad_request("invalid ticket")


"""
Let a user buy a ticket
Input:
{
    user_email: String,
    venue: {
        venue_location: String,
        venue_name: String
    },
    event_id: Integer,
    ticket_num: Integer
}
Output:
{
    "ticket_num": Integer
}
"""
@app.route("/user/buy_ticket", methods=['POST'])
def user_buy_ticket():
    # get venue
    venue = request.json.get('venue')
    if (venue is None):
        return bad_request('Need venue')

    # get venue object
    v = parse_venue(venue)
    if v is None:
        return bad_request('Venue does not exist')

    # get event
    event_id = request.json.get('event_id')
    e = bc_get_event(v, event_id)
    if e is None:
        return bad_request('Event does not exist')

    # get ticket
    # tickets_info = request.json.get('ticket_info')
    # if tickets_info is None:
    #     return bad_request('Need ticket_info')
    # section = tickets_info.get('section')
    # row = tickets_info.get('row')
    # seat_num = tickets_info.get('seat_num')
    ticket_num = request.json.get('ticket_num')

    # get user email
    user_email = request.json.get('user_email')
    u = Trackers.registered_users.get(user_email)
    if u is None:
        return bad_request('User does not exist')
    u.wallet = 100000

    #buy ticket
    ret = bc_buy_ticket(v, e, u, ticket_num)
    if ret is not False:
        return good_request({"ticket_num": ret})
    return bad_request('Buying ticket failed')

"""
Let a user buy a ticket
Input:
{
    user_email: String,
    venue: {
        venue_location: String,
        venue_name: String
    },
    event_id: Integer,
    ticket_num: Integer,
    new_ticket_num: Integer
}
Output:
{
    "ticket_num": Integer
}
"""
@app.route("/user/upgrade_ticket", methods=['POST'])
def user_upgrade_ticket():
    # get venue
    venue = request.json.get('venue')
    if (venue is None):
        return bad_request('Need venue')

    # get venue object
    v = parse_venue(venue)
    if v is None:
        return bad_request('Venue does not exist')

    # get event
    event_id = request.json.get('event_id')
    e = bc_get_event(v, event_id)
    if e is None:
        return bad_request('Event does not exist')


    ticket_num = request.json.get('ticket_num')
    new_ticket_num = request.json.get('new_ticket_num')

    # get user email
    user_email = request.json.get('user_email')
    u = Trackers.registered_users.get(user_email)
    if u is None:
        return bad_request('User does not exist')
    u.wallet = 100000

    #upgrade ticket
    ret = bc_upgrade_ticket(v, e, u, ticket_num, new_ticket_num)
    if ret is not False:
        return good_request({"ticket_num": ret})
    return bad_request('Upgrading ticket failed')

"""
Let a user see his tickets
Input:
{
    user_email: String,
}
Output:
[
    {
        "ticket_num": Integer,
        "event_id": Integer,
        "venue": 
        {
            "venue_location": String,
            "venue_name": String
        }
    }
]
"""
@app.route("/user/view_tickets", methods=['POST'])
def user_view_tickets():
    # get user email
    user_email = request.json.get('user_email')
    u = Trackers.registered_users.get(user_email)
    if u is None:
        return bad_request('User does not exist')

    ret = []
    for ticket in u.inventory:
        event_id = ticket.event.id
        venue = ticket.event.venue
        venue_dict = {"venue_location": venue.location, "venue_name": venue.name}
        ticket_dict = {"ticket_num": ticket.ticket_num, "event_id": event_id, "venue": venue_dict}
        ticket_dict['seat_info'] = {"section": ticket.seat.section, "row": ticket.seat.row, "seat_num": ticket.seat.seat_no}
        ticket_dict['event_info'] = {"name": ticket.event.name}
        ret.append(ticket_dict)

    return good_request(ret)

"""
View information for a single event
Input:
{
    "event_id": Integer,
    "venue": 
    {
        "venue_location": String,
        "venue_name": String
    }
}
Output:
{
    'event_id': Integer, 
    'name': String, 
    'desc': String,
    'num_scheduled_tickets': Integer
}
"""
@app.route("/venue/view_event", methods=['POST'])
def venue_view_event():
    # get venue
    venue = request.json.get('venue')
    if (venue is None):
        return bad_request('Need venue')

    # get venue object
    v = parse_venue(venue)
    if v is None:
        return bad_request('Venue does not exist')

    # get event
    event_id = request.json.get('event_id')
    e = bc_get_event(v, event_id)
    if e is None:
        return bad_request('Event does not exist')

    e_dict = {'event_id': e.id, 'name': e.name, 'desc': e.desc,
            'num_scheduled_tickets': len(e.scheduled)}

    return good_request(e_dict)


"""
Search for events
Input:
{
    "user_email": String,
    "search_info": 
    {
        "search_text": String,
        "date_range": Integer,
        "date": 
        {
            "month": Integer,
            "year": Integer,
            "day": Integer
        }
    }
}
Output:
[
    {
        'event_id': Integer, 
        'name': String, 
        'desc': String,
        'num_scheduled_tickets': Integer
    }
]
"""
@app.route("/user/search", methods=['POST'])
def user_search():
    user_email = request.json.get('user_email')
    u = Trackers.registered_users.get(user_email)
    if u is None:
        return bad_request('User does not exist')
    search_info = request.json.get('search_info')

    if search_info is None:
        return bad_request('Need search_info')
    search_text = search_info.get('search_text')
    date_range = search_info.get('date_range')
    date = search_info.get('date')
    
    events = bc_search(u, search_text, date, date_range)
    ret = parse_events(events)
    return good_request(ret)

"""
Explore feature
Input:
{
    "user_email": String,
}
Output:
[
    {
        'event_id': Integer, 
        'name': String, 
        'desc': String,
        'num_scheduled_tickets': Integer
    }
]
"""
@app.route("/user/explore", methods=['POST'])
def user_explore():
    user_email = request.json.get('user_email')
    u = Trackers.registered_users.get(user_email)
    if u is None:
        return bad_request('User does not exist')
    events = bc_explore(u)
    ret = parse_events(events)
    return good_request(ret)


"""
Schedule release of all tickets for a section of an event
Input:
{
    "event_id": Integer,
    "venue": 
    {
        "venue_location": String,
        "venue_name": String
    },
    "release_info":
    {
        "section": String,
        "release_date":
        {
            "month": Integer,
            "day": Integer, 
            "year": Integer
        }
    }
}
"""
@app.route("/venue/schedule_release", methods=['POST'])
def venue_schedule_release():
    # get venue
    venue = request.json.get('venue')
    if (venue is None):
        return bad_request('Need venue')

    # get venue object
    v = parse_venue(venue)
    if v is None:
        return bad_request('Venue does not exist')

    # get event
    event_id = request.json.get('event_id')
    e = bc_get_event(v, event_id)
    if e is None:
        return bad_request('Event does not exist')

    # get release_info
    release_info = request.json.get('release_info')
    if release_info is None:
        return bad_request('Need release_info')
    section = release_info.get('section')
    release_date = release_info.get('release_date')

    # schedule releases
    if bc_schedule_release(v, e, section, release_date):
        return good_request({})
    return bad_request("Scheduling failed")


"""
View venue's wallet
Input:
{
    "venue": 
    {
        "venue_location": String,
        "venue_name": String
    }
}
"""
@app.route("/venue/view_wallet", methods=['POST'])
def venue_view_wallet():
    # get venue
    venue = request.json.get('venue')
    if (venue is None):
        return bad_request('Need venue')

    # get venue object
    v = parse_venue(venue)
    if v is None:
        return bad_request('Venue does not exist')
    return good_request({"wallet": v.wallet})

"""
View user's wallet
Input:
{
    "user_email": String
}
"""
@app.route("/user/view_wallet", methods=['POST'])
def user_view_wallet():
    # get user
    user_email = request.json.get('user_email')
    u = Trackers.registered_users.get(user_email)
    if u is None:
        return bad_request('User does not exist')

    return good_request({"wallet": u.wallet})

"""
Generate ticket code
Input:
{
    "venue": 
    {
        "venue_location": String,
        "venue_name": String
    },
    "user_email": String,
    "event_id": Integer,
    "ticket_num": Integer
}
"""
@app.route("/user/generate_ticket_code", methods=['POST'])
def user_generate_ticket_code():
    venue = request.json.get('venue')
    if (venue is None):
        return bad_request('Need venue')

    # get venue object
    v = parse_venue(venue)
    if v is None:
        return bad_request('Venue does not exist')

    # get event
    event_id = request.json.get('event_id')
    e = bc_get_event(v, event_id)

    # get user
    user_email = request.json.get('user_email')
    u = Trackers.registered_users.get(user_email)
    if u is None:
        return bad_request('User does not exist')

    ticket_num = request.json.get('ticket_num')
    qrobj = bc_generate_ticket_code(v, e, ticket_num, u)
    if qrobj is None:
        return bad_request('failed getting qr code')
    qrobj.png('/tmp/tempqr.png')
    return send_file('/tmp/tempqr.png', mimetype='image/png')



if __name__ == "__main__":
    app.run(debug=True)
