from Admit01_Blockchain import *
from datetime import datetime
from datetime import timedelta
import pyqrcode as qr
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
        bad_ticket = False
        seat_selected = False
        while not seat_selected:
            section = str(input('\nWhat section is the seat in? (e.g. Mezzanine, GA): '))
            row = str(input('What row is the seat in? (A string, e.g. C, H, AA): '))
            seat_no_str = input('What is the seat number? (An int): ')
            try:
                seat_no = int(seat_no_str)
            except ValueError:
                seat_no = -1
            seat = Seat(section, row, seat_no)
            seat_selected = seat.section is not None
            if not seat_selected:
                print('Whoops, something went wrong. Let\'s try that again...')
        print('\nSplendid. How much will this ticket cost?')
        face_value_str = input('Enter face value: $')
        try:
            face_value = float(face_value_str)
        except ValueError:
            face_value = -1
        print('\nPlease wait, we\'re doing blockchain stuff.')
        print('Currently mining new blocks...')
        ticket = venue.createTicket(event, face_value, seat)
        if ticket is None:
            bad_ticket = True
            print('\nWhoops, something went wrong. We couldn\'t create that '
                  'ticket. Either the seat has already been ticketed or you entered an invalid price. '
                  'Let\'s try that again...')
        else:
            print('\nWonderful. We\'ve created a ticket for seat (' + section +
                  ', ' + row + str(seat_no) + ') at ' + event.name + '. Its ' +
                  'face value is $' + '{0:.2f}'.format(ticket.face_value) + ', ' +
                  'and it\'s been posted to the blockchain for ' + venue.name +
                  ' and the blockchain for its event.')
            print('\nWould you like to list this ticket as \'For Sale\'?')
            yn = str(input('Enter Y/N: '))
            if yn.upper() == 'Y':
                # list the Ticket as For Sale
                ticket.listTicket(face_value, venue.id)
        if not bad_ticket:
            print('\nWould you like to create another ticket for this event?')
            yn = str(input('Enter Y/N: '))
            done = (yn.upper() != 'Y')
            if done and len([ticket.ticket_num for ticket in event.tickets if ticket.isForSale()]) == 0:
                print('\nWhoops! You need to make at least one ticket for sale. Let\'s make another...')
                done = False
        else:
            done = False
    ticket_count(event)
    print('\nNice job making those tickets. You\'re a natural!')

def load_users():
    """ Load some dummy users """
    User('Ross', 'Piper', 'rp@admit01.com')
    User('Ethan', 'Reeder', 'er@admit01.com')
    User('Jane', 'Doe', 'jd@uchicago.edu')
    User('Hillary', 'Clinton', 'hrc@emails.gov')
    User('Marlon', 'Brando', 'don@corleone.family')

def list_users():
    """ List all registered users """
    print('Name' + (' ' * 26) + 'Email Address')
    for email, user in Trackers.registered_users.items():
        print('{:<30}'.format(user.fname + ' ' + user.lname) + email)

def create_user_profile():
    """ Create a new user profile for the user """
    print('\nBefore you can buy a ticket to this awesome event, you\'ll need '
          'to set up a user profile. For your reference, here is a list of '
          'our current users.\n')
    list_users()
    print('\nTo set up your user account, we\'ll need some information from you.')
    print('Note that you can not use an email address already registered by '
          'an existing user, and both name fields must be filled.')
    done = False
    while not done:
        fname = str(input('\nFirst name: '))
        lname = str(input('Last name:  '))
        email = str(input('Email address: '))
        user = User(fname, lname, email)
        done = user.id is not None
        if not done:
            print('\nWhoops, looks like you messed up! Let\'s try that again, shall we?')
    user.wallet = 1000000.00
    print('\nCongratulations, ' + fname + '! To celebrate your new account, we\'ve gone ahead ' +
          'and wired $' + '{0:.2f}'.format(user.wallet) + ' into your ' +
          'account. That should be enough to get you started!')

    return user

def list_all_tickets(event):
    """ List all tickets for an event, both for and not for sale """
    print('\nID\tFor Sale?' + (' ' * 6) + 'Price' + (' ' * 10) + 'Seat')
    for ticket in event.tickets:
        seat = ticket.seat
        print(str(ticket.ticket_num) + '\t' + '{:<15}'.format(('Yes' if ticket.isForSale() else 'No')) +
              '{:<15}'.format('{0:.2f}'.format(ticket.list_price)) +
              '(' + seat.section + ', ' + seat.row + ', ' +
              str(seat.seat_no) + ')')

def buy_a_ticket(event, user):
    """ Select and purchase a ticket, then return it """
    ticket = None
    print('\nNow that you have a profile set up and have some money to spend, '
          'let\'s pick a ticket for ' + event.name + '.')
    list_all_tickets(event)
    print('\nWhich ticket would you like to buy? You currently have $' +
          '{0:.2f}'.format(user.wallet) + '.')
    ticket_nums = [ticket.ticket_num for ticket in event.tickets if ticket.isForSale()]
    ticket_num = -1
    while ticket_num not in ticket_nums:
        ticket_num = int(input('Enter ticket ID: '))
        if ticket_num not in ticket_nums:
            print('\nWhoa! That\'s not a legit ticket ID to buy. Try again...')
    print('\nNice choice. Now let\'s buy that ticket.')
    for t in event.tickets:
        if ticket_num == t.ticket_num:
            ticket = t
            break
    print('\nPlease wait, we\'re doing blockchain stuff.')
    print('Currently mining new blocks...')
    user.buyTicket(ticket)
    print('\nCongratulations! You\'re now the owner of Ticket #' + str(ticket_num) +
          ' for ' + event.name + '. Your new balance is $' + '{0:.2f}'.format(user.wallet) + '.')
    list_all_tickets(event)
    print('\nNotice that Ticket #' + str(ticket_num) + ' is no longer for sale!')
    return ticket

def generate_more_tickets(venue, event, user_ticket):
    """ Make a cheaper Ticket and a more expensive Ticket, then set for sale """
    face_value = user_ticket.face_value
    seat1 = Seat(user_ticket.seat.section, user_ticket.seat.row,
                 user_ticket.seat.seat_no + 2)
    seat2 = Seat(user_ticket.seat.section, user_ticket.seat.row,
                 user_ticket.seat.seat_no + 4)
    print('\nOh dear! It looks like ' + venue.name + ' is listing some more ' +
          'tickets for sale. Give us a moment, we\'re mining some blocks...')
    ticket1 = venue.createTicket(event, face_value + 50, seat1)
    ticket1.listTicket(ticket1.face_value, venue.id)
    ticket2 = venue.createTicket(event, face_value - 10 if face_value - 10 > 0 else 0, seat2)
    ticket2.listTicket(ticket2.face_value, venue.id)

def upgrade_ticket(event, user_ticket, user):
    """
    Upgrade to a more expensive ticket, pay the difference,
    and return the new ticket
    """
    print('\nLet\'s take a look at what tickets are currently available after ' +
          'this most recent update.')
    list_all_tickets(event)
    print('\nNow we\'re going to take advantage of our revolutionary Ticket ' +
          'Upgrade feature. Please pick an ID of a ticket with a higher ' +
          ' price than your ticket ($' + '{0:.2f}'.format(user_ticket.face_value) +
          '), and we\'ll upgrade you to that one. The venue will buy back ' +
          'your ticket at face value, so you\'ll only be charged the difference.')
    ticket_nums = [ticket.ticket_num for ticket in event.tickets if ticket.isForSale()]
    ticket_num = -1
    while ticket_num not in ticket_nums:
        ticket_num = int(input('Enter ticket ID: '))
        if ticket_num not in ticket_nums:
            print('\nWhoa! That ticket is not for sale. Try again...')
        else:
            selected_ticket = None
            for ticket in event.tickets:
                if ticket.ticket_num == ticket_num:
                    selected_ticket = ticket
                    break
            if selected_ticket.face_value < user_ticket.face_value:
                print('\nPlease select a ticket with an equal or higher face value ' +
                      'than your current ticket ($' + '{0:.2f}'.format(user_ticket.face_value) + ').')
                ticket_num = -1
    print('\nOk! How exciting. We\'ll upgrade you to from Ticket #' + str(user_ticket.ticket_num) +
          ' to Ticket #' + str(selected_ticket.ticket_num) + '. The difference of $' +
          '{0:.2f}'.format(selected_ticket.face_value - user_ticket.face_value) +
          ' will be charged to your account once the blocks are posted.')
    print('\nUpgrading your ticket now. Be patient, we\'ll have to mine a block for this...')
    user.upgradeTicket(user_ticket, selected_ticket)

    return selected_ticket

def generate_ticket(user, venue, event, ticket):
    """ Generate a PNG ticket QR code """
    print('\nOutstanding, you\'re ready for the concert! We\'re validating ' +
          'your ownership status on the blockchain and generating your ticket...')
    qrcode = user.generateTicketCode(venue, event, ticket)
    qrcode.png('../demo_ticket.png', scale = 10)
    print('\nCongratulations! Your ticket is waiting for you in the ' +
          'main directory as \'demo_ticket.png\'. Have fun at ' + event.name + '!\n')

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
    load_users()
    user = create_user_profile()
    ticket = buy_a_ticket(event, user)
    generate_more_tickets(venue, event, ticket)
    new_ticket = upgrade_ticket(event, ticket, user)
    generate_ticket(user, venue, event, new_ticket)

if __name__ == '__main__': main()
