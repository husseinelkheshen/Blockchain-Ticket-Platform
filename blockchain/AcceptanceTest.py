from Admit01_Blockchain import *
from datetime import datetime
from datetime import timedelta
import copy

valid_venue = False
more_venues = True

def make_venue():
    """ Makes a new venue """
    valid_venue = False
    while not valid_venue:
        # create a new venue
        print('Let\'s make a new venue!')
        name = input('Venue name (ex. Apollo Theater): ')
        loc = input('Venue location (ex. Chicago, IL): ')
        venue1 = Venue(name, loc)

        # check if valid venue
        valid_venue = venue1.id is not None
        if not valid_venue:
            print('Oh no! You entered invalid parameters for your new venue.')
            print('Let\'s try that again...\n')

    print('Great! You\'ve successfully created ' + name + ' in ' + loc + '.\n')

def make_event(venue):
    """ Makes a new event at the venue """
    name = input('Event name: ')
    desc = input('Brief event description (optional): ')
    date = input('Date (MM/DD/YYYY): ')
    time = input('Time (24-hour clock, HH:MM): ')
    dt = datetime.strptime('{}, {}'.format(date, time), '%m/%d/%Y, %H:%M')


def main():
    """ Main method """
    more_venues = True
    while more_venues:
        make_venue()
        yn = input('Do you want to create another venue? (Y/N): ')
        more_venues = (yn.upper() == 'Y')
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
    print('\nNow let\'s create a new event.')
    venue_ids = [i[0] for i in venue_list]
    valid_id = False
    while not valid_id:
        print('At which venue do you want to create the event?')
        venue_id = int(input('Enter venue id: '))
        valid_id = venue_id in venue_ids
        if not valid_id:
            print('\nThat\'s not a valid venue id, let\'s try again...')
    v_index = [y[0] for y in venue_list].index(venue_id)
    print('\nExcellent! Let\'s make a new event in ' + venue_list[v_index][2] +
          ' at ' + venue_list[v_index][1] + '.')

if __name__ == '__main__': make_event(None)
