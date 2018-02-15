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
    print('\nExcellent! Let\'s take a look at the events currently listed in ' +
          venue_list[v_index][2] + ' at ' + venue_list[v_index][1] + '.')

    return v_index

def load_events(venue):
    """ Loading events into the selected venue """
    dt1 = datetime.now() + timedelta(days=7)
    dt2 = datetime.now() + timedelta(days=23)
    event1 = Event("Lady Gaga", dt1, "World Tour")
    event2 = Event("Hamilton", dt2, "2016 Tony Award Winner")
    event1.venue = venue
    event2.venue = venue
    venue.events[event1.id] = (event1, copy.deepcopy(event1.blockchain))
    venue.events[event2.id] = (event2, copy.deepcopy(event2.blockchain))

def main():
    """ Main method """
    load_venues()
    venue_list = list_venues()
    venue_index = select_venue(venue_list)
    venue = venue_list[venue_index][3]
    load_events(venue)

if __name__ == '__main__': main()
