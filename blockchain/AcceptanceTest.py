from Admit01_Blockchain import *
from datetime import datetime
from datetime import timedelta
import copy

valid_venue = False
more_venues = True

def load_venues():
    """ Load up the dummy venues """
    Venue('Adrienne Arsht Center', 'Miami, FL')
    Venue('American Airlines Arena', 'Miami, FL')
    Venue('Apollo Theater', 'Chicago, IL')
    Venue('Civic Opera House', 'Chicago, IL')
    Venue('Madison Square Garden', 'New York, NY')

def list_venues():
    """ List venues and return a list of tuples """
    print('\nHere is a list of all registered venues')
    print('\nID\tName')
    venue_list = []
    for city in Trackers.registered_venues:
        for name in Trackers.registered_venues[city]:
            venue = Trackers.registered_venues[city][name]
            venue_list.append((venue.id, name, city, venue))
    venue_list.sort()
    for vtup in venue_list:
        print(str(vtup[0]) + '\t' + vtup[1] + ' (' + vtup[2] + ')')

    return venue_list

def select_venue(venue_list):
    """
    Select a venue from the list of venues and return
    its index in venue_list
    """
    print('\nSelect a Venue to explore its events.')
    venue_ids = [i[0] for i in venue_list]
    valid_id = False
    while not valid_id:
        venue_id = int(input('Enter venue id: '))
        valid_id = venue_id in venue_ids
        if not valid_id:
            print('\nThat\'s not a valid venue id, let\'s try again...')
    v_index = [y[0] for y in venue_list].index(venue_id)

    return v_index

def load_events(venue):
    """ Loading events into the selected venue """
    print('\nExcellent! Let\'s take a look at the events currently listed in ' +
          venue.location + ' at ' + venue.name + '.')
    dt1 = datetime.now() + timedelta(days=7)
    dt2 = datetime.now() + timedelta(days=23)
    event1 = Event("Lady Gaga", dt1, "Pop music concert")
    event2 = Event("Hamilton", dt2, "Award-winning musical")
    event1.venue = venue
    event2.venue = venue
    venue.events[event1.id] = (event1, copy.deepcopy(event1.blockchain))
    venue.events[event2.id] = (event2, copy.deepcopy(event2.blockchain))

def select_event(venue):
    """ List events at the current venue and select one by ID """
    gap = ' '
    print('\nID' + (gap * 13) + 'Name' + (gap * 11) +
          'Description' + (gap * 14) + 'Date\t\tTime')
    for event_id in venue.events:
        event = venue.events[event_id][0]
        e_id = '{:<15}'.format(str(event.id))
        name = '{:<15}'.format(event.name)
        desc = '{:<25}'.format(event.desc)
        dt = event.datetime.strftime('%m/%d/%Y\t%H:%M')
        print(e_id + name + desc + dt)
    print('\nPlease select an event to explore further.')
    valid_id = False
    while not valid_id:
        e_id = int(input('Enter event id: '))
        valid_id = e_id in venue.events
        if not valid_id:
            print('\nThat\'s not a valid event id, let\'s try again...')

    return e_id

def ticket_count(event):
    """
    Prints the current count of available tickets for an event and
    returns a list of unsold tickets
    """
    print('\nGreat! Let\'s take a look at what tickets are available for ' +
          event.name + ' at ' + event.venue.name + '.')
    count = len(event.tickets)
    unsold = len([ticket for ticket in event.tickets if ticket.isForSale()])
    print('\nThere are currently', count, 'tickets for this event.')
    print(unsold, 'of these are currently listed for sale.')

    return unsold

def create_tickets(venue, event):
    """ Create some tickets for the event """
    print('\nLet\'s create some tickets for this event.')
    done = False
    while not done:
        seat_selected = False
        while not seat_selected:
            section = input('What section is the seat in? (e.g. Mezzanine, GA): ')
            row = input('What row is the seat in? (A string, e.g. C, H, AA): ')
            seat_no = int(input('What is the seat number? (An int): '))
            seat = Seat(section, row, seat_no)
            seat_selected = seat.section is not None
            if not seat_selected:
                print('Whoops, something went wrong. Let\'s try that again...')
        print('\nSplendid. How much will this ticket cost?')
        face_value = float(input('Enter face value: $'))
        print('\nPlease wait, we\'re doing blockchain stuff.')
        print('Currently mining new blocks...')
        ticket = venue.createTicket(event, face_value, seat)
        if ticket is None:
            print('\nWhoops, something went wrong. We couldn\'t create that ' +
                  'ticket. Likely, that seat has already been ticketed.')
        else:
            print('\nWonderful. We\'ve created a ticket for seat (' + section +
                  ', ' + row + str(seat_no) + ') at ' + event.name + '. Its ' +
                  'face value is $' + '{0:.2f}'.format(ticket.face_value) + ', ' +
                  'and it\'s been posted to the blockchain for ' + venue.name +
                  ' and the blockchain for its event.')
            print('\nWould you like to list this ticket as \'For Sale\'?')
            yn = input('Enter Y/N: ')
            if yn.upper() == 'Y':
                # list the Ticket as For Sale
                ticket.listTicket(face_value, venue.id)
        print('\nWould you like to create another ticket for this event?')
        yn = input('Enter Y/N: ')
        done = (yn.upper() != 'Y')
    ticket_count(event)

def main():
    """ Main method """
    load_venues()
    venue_list = list_venues()
    venue_i = select_venue(venue_list)
    venue = venue_list[venue_i][3]
    load_events(venue)
    event = venue.events[select_event(venue)][0]
    ticket_count(event)
    create_tickets(venue, event)

if __name__ == '__main__': main()
