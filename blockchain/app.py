"""
This flask app handles requests from the requests server to make changes to the blockchain.
"""

from blockchain.Admit01_Blockchain import *
from flask import Flask
from flask import request, jsonify
from datetime import datetime
from datetime import timedelta
import copy

app = Flask(__name__)
venue_i = 0

def load_venues():
    """ Load up the dummy venues """
    Venue('Adrienne Arsht Center', 'Miami, FL')
    Venue('American Airlines Arena', 'Miami, FL')
    Venue('Apollo Theater', 'Chicago, IL')
    Venue('Civic Opera House', 'Chicago, IL')
    Venue('Madison Square Garden', 'New York, NY')


def load_events():
    """ Load up the dummy events """
    venue_list = list_venues()
    venue = venue_list[venue_i][3]
    dt1 = datetime.now() + timedelta(days=7)
    dt2 = datetime.now() + timedelta(days=23)
    event1 = Event("Lady Gaga", dt1, "Pop music concert")
    event2 = Event("Hamilton", dt2, "Award-winning musical")
    event1.venue = venue
    event2.venue = venue
    venue.events[event1.id] = (event1, copy.deepcopy(event1.blockchain))
    venue.events[event2.id] = (event2, copy.deepcopy(event2.blockchain))
    return event1, event2


def list_venues():
    """ List venues and return a list of tuples """
    venue_list = []
    for city in Trackers.registered_venues:
        for name in Trackers.registered_venues[city]:
            venue = Trackers.registered_venues[city][name]
            venue_list.append((venue.id, name, city, venue))
    venue_list.sort()
    return venue_list


def create_tickets(event):
    """Create a dummy ticket for an event"""
    seat = Seat("Section 1", "Row 1", 1)
    venue_list = list_venues()
    venue = venue_list[venue_i][3]
    ticket = venue.createTicket(event, 100, seat)
    print('ticket created: {}'.format(ticket.ticket_num))


@app.route("/tickets/", methods=['POST'])
def tickets():
    return 'Hello'


@app.route("/tickets/buy", methods=['POST'])
def buyTicket():
    print('buy ticket')
    venue_list = list_venues()
    print(venue_list)
    venue = venue_list[venue_i][3]
    print(venue)
    print(request.json)
    user = request.json['user']
    print(user)

    email = user['email']
    email = "jd@uchicago.edu"
    print(email)
    ticket_num = request.json['ticket_num']
    print(ticket_num)
    event_id = request.json['event']
    print(email, event_id, ticket_num)

    event = venue.events[event_id][0]
    ticket = None
    print(event)
    for t in event.tickets:
        if t.ticket_num == ticket_num:
            ticket = t

    if t is None:
        print ('t is None')
        return False

    bcuser = Trackers.registered_users[email]
    bcuser.wallet += 1000
    return str(bcuser.buyTicket(ticket))


@app.route("/tickets/list", methods=["POST"])
def listTicket():
    """ List venues and return a list of tuples """
    venue_list = list_venues()
    venue = venue_list[venue_i][3]
    event_id = request.json.get('event')
    ticket_num = request.json.get('ticket_num')
    face_value = 100
    event = venue.events[event_id][0]
    ticket = None
    for t in event.tickets:
        if t.ticket_num == ticket_num:
            ticket = t

    if t is None:
        return str(False)

    ticket.listTicket(face_value, venue.id)
    return str(True)


@app.route("/ticket/list_events")
def getEvents():
    venue_location = request.json.get('venue_location')
    venue_name = request.json.get('venue_name')
    venue = Trackers.registered_venues[venue_location][venue_name]
    event_names = venue.events.keys()
    return event_names




def main():
    load_venues()
    event1, event2 = load_events()
    print('creating ticket 1')
    create_tickets(event1)
    print('creating ticket 2')
    create_tickets(event2)
    User('Jane', 'Doe', 'jd@uchicago.edu')

    print('running app')
    app.run(debug=True, host='0.0.0.0', port=80)


if __name__ == '__main__':
    main()
