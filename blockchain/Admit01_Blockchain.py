from random import *
import datetime as date
import hashlib as hasher
import pyqrcode as qr
import string


class Trackers:
    """ Holds all global tracker variables """

    # keep track of the next usable id number to avoid duplicates amongst or
    # between Users and Venues; must be incremented by 1 after each use
    next_user_venue_id = 0

    # keep track of the next Event id number to avoid duplicates
    next_event_id = 0

    # keep track of all Venues on the platform
    # dictionaries of Venues are mapped by their location
    # per-location dictionaries of Venues are mapped by their name
    # ex. {'Chicago, IL': {'Apollo Theater': <Venue obj>}}
    registered_venues = {}

    # keep track of all registered Users on the platform
    # a User is mapped by his or her email_addfress
    # ex. {'email@address.com': <User obj>}
    registered_users = {}

    @staticmethod
    def venueExists(venue_id):
        """ Checks if a Venue is registered """
        if venue_id is None or venue_id < 0:
            return False

        venues = Trackers.registered_venues
        for city in venues:
            for venue_name in venues[city]:
                if venue_id == venues[city][venue_name].id:
                    return True

        return False

    @staticmethod
    def getNextUserVenueID():
        """ Retrieves the next usable ID for User or Venue """
        next_id = Trackers.next_user_venue_id
        Trackers.next_user_venue_id += 1
        return next_id

    @staticmethod
    def getNextEventID():
        """ Retrieves the next usable ID for Event """
        next_id = Trackers.next_event_id
        Trackers.next_event_id += 1
        return next_id


# The Block class, constituting an instance of a block in the chain
class Block:
    def __init__(self, index, timestamp, transactions, prev_hash):
        if prev_hash is None or len(prev_hash) == 0:
            # genesis
            self.index = 0
            self.timestamp = timestamp
            self.data = transactions
            self.prev_hash = ""
            self.hash = ""
        else:
            self.index = index # numerical index, (matching the list index of the block?)
            self.timestamp = timestamp # a datetime timestamp object
            self.data = transactions # a list of transactions
            self.prev_hash = prev_hash # the hash of the previous block in the chain
            self.hash = "" # the new hash for this block, including all of the above fields

    # generates a sha256 hash given a string
    @staticmethod
    def generateHash(text):
        sha = hasher.sha256()
        sha.update(text.encode('utf-8'))
        return sha.hexdigest()

    # generates a hash of length random characters (ascii uppercase and digits)
    @staticmethod
    def genesisHash(length):
        return generateHash(
            ''.join(random.choice(string.ascii_uppercase + string.digits)
                    for _ in range(length)))

    def hashBlock(self, nonce):
        return self.genSHA1Hash(':'.join(["1", "20",
                                self.timestamp.strftime("%y%m%d%H%M%S"),
                                str(self), nonce]))

    def genSHA1Hash(self, text):
        sha = hasher.sha1()
        sha.update(text.encode('utf-8'))
        return sha.hexdigest()

    def __str__(self):
        return str(self.index) + str(self.data) + self.prev_hash


class Chain:
    """ Wrapper for a list of Block objects and some helper methods """
    def __init__(self):
        self.blocks = []    # no need for a genesis block here
        self.prev_hashes = []

    def findRecentTrans(self, ticket_id):
        recentTrans = None



    def mineNewBlock(self, otherchains):
        if self.blocks[-1].hash:
            return False
        else:
            counter = randint(0, 65536)
            result = "11111"
            randstring = ''.join(choice(string.ascii_uppercase +
                                        string.digits + string.ascii_lowercase +
                                         '+' + '/') for _ in range(16))
            while result[0:5] != "00000" or result in self.prev_hashes:
                counter += 1
                result = self.blocks[-1].genSHA1Hash(
                    ':'.join(["1", "20", self.blocks[-1].timestamp.strftime(
                    "%y%m%d%H%M%S"), str(self.blocks[-1]),
                    randstring, str(counter)]))
            # print("Got a matching hash\n")
            # print(result)
            if len(self.blocks) > 1:
                self.prev_hashes.append(self.blocks[-2].hash)
            nonce = randstring + ":" + str(counter)
            for chain in otherchains:
                if chain.blocks[-1].hashBlock(nonce) != result:
                    return False
            otherchains.append(self)
            for chain in otherchains:
                chain.blocks[-1].hash = result
            return True




# The Transaction class, pretty simple, to, from, value of transaction.
class Transaction:
    def __init__(self, target, source, value, ticket_num):
        has_target_or_source = (target != None) or (source is not None)
        has_ticket_num = (ticket_num is not None) and (ticket_num >= 0)
        if not has_target_or_source or not has_ticket_num:
            self. target = self.source = self.value = self.ticket_num = None
        else:
            self.target = target
            self.source = source
            self.value = value
            self.ticket_num = ticket_num #

class User:
    """
    Class to uniquely identify users, maintain and manage their Ticket
    inventory, and keep track of their usable funds (in their 'wallet')

    """
    def __init__(self, fname, lname, email_address):
        """
        User constructor

            fname: string
            lname: string
            email_address: string

        """
        if email_address:
            unique_email = email_address not in Trackers.registered_users
        else:
            unique_email = False
        # check for empty strings and confirm email isn't already registered
        if fname and lname and email_address and unique_email:
            self.id = Trackers.getNextUserVenueID()
            self.fname = fname
            self.lname = lname
            self.email_address = email_address
            self.inventory = []
            self.wallet = 0.00
            # add this User to the catalog of registered Users
            Trackers.registered_users[email_address] = self
        else:
            self.id = self.fname = self.lname = self.email_address = None
            self.inventory = self.wallet = None

    def getID(self):
        """ Getter for User's ID number """
        return self.id

    def buyTicket(self, ticket):
        '''
        Allows a User to buy a listed ticket

            ticket: Ticket object

        '''

        # check if involved objects are valid
        if (self.id == None
            or ticket.event == None
            or ticket.seat == None
            or ticket.face_value == None
            or ticket.list_value == None
            or ticket.for_sale == None
            or ticket.history == None):
            return False

        # check if the event has already transpired
        if ticket.event.datetime < datetime.now():
            return False

        # check if ticket is for sale
        if ticket.for_sale == True:
            return False

        # check if user calling has enough money in wallet
        if ticket.list_value > self.wallet:
            return False

        # check if user already owns the ticket
        if ticket in self.inventory:
            return False

        # generate new transactions
        new_transactions = []
        new_transactions.append(Transaction(self.id,
                                            ticket.event.id,
                                            ticket.list_value,
                                            ticket.ticket_num))

        # post the transaction to a new block
        prev_hash = None
        new_block_index = len(event.blockchain.blocks)
        if new_block_index > 0:
            prev_hash = event.blockchain.blocks[-1].hash
        new_block = Block(new_block_index,
                          date.datetime.now(),
                          new_transactions,
                          prev_hash)

        # append the new block to both blockchains
        event.blockchain.blocks.append(new_block)
        event.venue.events[event.id][1].blocks.append(new_block)

        # UNFINISHED mine one new block
        new_block_hash = None

        # UNFINISHED broadcast the nonce to the other blockchain

        # add record and hash to ticket's history
        ticket.history.append((new_block_index, new_block_hash))

        # add ticket to user's inventory
        self.inventory.append(ticket)

        # subtract appropriate funds from user's wallet
        self.wallet = self.wallet - ticket.list_value

        # mark ticket as sold
        ticket.for_sale = False

        # signify completion
        return True

    def upgradeTicket(self, owned_ticket, new_ticket):
        '''
        Allows a User to upgrade an owned ticket for another listed ticket

            ticket: Ticket object

        '''

        # check if involved objects are valid
        if (self.id == None
            or owned_ticket == None
            or new_ticket.event == None
            or new_ticket.seat == None
            or new_ticket.face_value == None
            or new_ticket.list_value == None
            or new_ticket.for_sale == None
            or new_ticket.history == None):
            return False

        # check if the event has already transpired
        if new_ticket.event.datetime < datetime.now():
            return False

        # check if ticket is for sale
        if new_ticket.for_sale == False:
            return False

        # check if new ticket is more valuable than old ticket
        if new_ticket.list_value < owned_ticket.list_value:
            return False

        # check if user owns ticket which will be upgraded
        if owned_ticket not in self.inventory:
            return False

        # check if user already owns the target ticket
        if new_ticket in self.inventory:
            return False

        # check if both tickets are for the same event
        if owned_ticket.event != new_ticket.event:
            return False

        # generate new transactions
        new_transactions = []
        new_transactions.append(Transaction(self.id,
                                            new_ticket.event.id,
                                            new_ticket.list_value,
                                            new_ticket.ticket_num))
        # new_transactions.append(Transaction(other party))

        # post the transactions to a new block
        prev_hash = None
        new_block_index = len(new_ticket.event.blockchain.blocks)
        if new_block_index > 0:
            prev_hash = event.blockchain.blocks[-1].hash
        new_block = Block(new_block_index,
                          date.datetime.now(),
                          new_transactions,
                          prev_hash)

        # append the new block to both blockchains
        new_ticket.event.blockchain.blocks.append(new_block)
        new_ticket.event.venue.events[event.id][1].blocks.append(new_block)

        # UNFINISHED mine one new block
        new_block_hash = None

        # UNFINISHED broadcast the nonce to the other blockchain

        # add record and hash to ticket's history
        new_ticket.history.append((new_block_index, new_block_hash))

        # remove upgraded ticket from user inventory and add new ticket
        self.inventory.remove(owned_ticket)
        self.inventory.append(new_ticket)

        # subtract appropriate funds from user's wallet
        self.wallet -= (new_ticket.list_value - owned_ticket.list_value)

        # add appropriate funds to seller's wallet (iteration 2)

        # mark old ticket as for sale, and new as sold
        owned_ticket.for_sale = True
        new_ticket.for_sale = False

        # signify completion
        return True

    def search(self, text):
        # iteration 2
        return False

    def explore(self):
        # iteration 2
        return False

    def generateTicketCode(self, venue, event, ticket):
        """
        Generate a QR code object if the User owns the Ticket

            venue: Venue object
            event: Event object
            ticket: Ticket object

        """
        ticket_code = None
        # confirm Event is valid
        if event.id in venue.events and event == venue.events[event.id][0]:
            # confirm Ticket is valid
            if ticket in event.tickets:
                current_owner = ticket.mostRecentTransaction().target
                # confirm Ticket ownership
                if self.id == current_owner:
                    ticket_data = ("venue_id = " + str(venue_id) +
                                   "\nevent_id = " + str(event_id) +
                                   "\nticket_num = " + str(ticket.ticket_num) +
                                   "\ncurrent_owner = " + str(current_owner))
                    # generate ticket code
                    ticket_code = qr.create(ticket_data)

        return ticket_code    # call ticket_code.png('filename.png') to generate


class Venue:
    """
    Class for uniquely identifying event venues as well as storing a list of
    its upcoming Events mapped to validation copies of each one's blockchain

    """
    def __init__(self, name, location):
        """
        Venue constructor

            name: string
            location: string

        """
        location_exists = False
        venue_already_exists = False
        # check if the name/location pair already exists
        if location in Trackers.registered_venues:
            location_exists = True
            if name in Trackers.registered_venues[location]:
                venue_already_exists = True
        if name and location and not venue_already_exists:
            self.id = Trackers.getNextUserVenueID()
            self.name = name
            # dictionary mapping event_ids to tuples that pair Events to Venue
            # copies of their blockchains
            # ex. {1023: (<Event obj>: <Chain obj>)}
            self.events = {}
            self.location = location
            # add this Venue to the catalog of registered Venues
            if not location_exists:
                Trackers.registered_venues[location] = {}
            Trackers.registered_venues[location][name] = self
        else:
            self.id = self.name = self.events = self.location = None

    def validateTicket(self, code, chain):
        return False

    def createEvent(self, name, datetime, desc):
        new_event = Event(name, datetime, desc)
        new_event.venue = self
        return new_event

    def manageEvent(self, event):
        return False

    def createTicket(self, event, face_value, seat):
        """
        Allows a Venue to create a new Ticket for one of its Events

            event: Event object
            face_value: int
            seat: Seat object

        """
        # make sure Venue is valid
        if self.id is not None:
            # make sure Event is valid
            if (event.id is not None and
                event.id in self.events and
                event == self.events[event.id][0]):
                # make sure Ticket for this Seat does not already exist
                assert seat is not None
                valid_ticket = True
                for ticket in event.tickets:
                    if ticket.seat == seat:
                        valid_ticket = False
                        break
                if valid_ticket:
                    # create the new Ticket
                    new_ticket = Ticket(event, face_value, seat)
                    # post to both blockchains and Ticket history
                    new_txn = Transaction(self.id, None, 0,
                                          new_ticket.ticket_num)
                    prev_hash = None
                    new_block_index = len(event.blockchain.blocks)
                    if new_block_index > 0:
                        prev_hash = event.blockchain.blocks[-1].hash
                    new_block = Block(new_block_index, date.datetime.now(),
                                      [new_txn], prev_hash)
                    event_chain = event.blockchain
                    venue_chain = self.events[event.id][1]
                    # add new block to both chains
                    event_chain.blocks.append(new_block)
                    venue_chain.blocks.append(new_block)
                    # mine the new block
                    if event_chain.mineNewBlock([venue_chain]):
                        new_block_hash = event_chain.blocks[-1].hash
                        new_ticket.history.append((new_block_index,
                                                   new_block_hash))
                        event.tickets.append(new_ticket)
                    else:
                        del event_chain.blocks[-1]
                        del venue_chain.blocks[-1]
                        print("Transaction aborted: could not mine block")


    def manageTicket(self, event, ticket_class):
        return False

    def scheduleRelease(self, event, ticket_class, number):
        return False


class Event:
    """ Class to define an event, each of which will belong to a Venue """
    def __init__(self, name, datetime, desc):
        """
        Event constructor

            name: string
            datetime: datetime object
            desc: string

        """
        self.tickets = []    # can add tickets later
        self.venue = None
        if not name or datetime < date.datetime.now():
            self.id = self.name = self.datetime = None
            self.desc = self.blockchain = None
        else:
            self.id = Trackers.getNextEventID()
            self.next_ticket_num = 0
            self.name = name
            self.datetime = datetime
            self.desc = desc
            self.blockchain = Chain()    # initialize an empty blockchain


class Seat:
    """ Class to uniquely identify a seat within a Venue """
    def __init__(self, section, row, seat_no):
        """
        Seat constructor

            section: string
            row: string
            seat_no: int

        """
        if not section or not row or seat_no < 0:
            self.section = self.row = self.seat_no = None
        else:
            self.section = section
            self.row = row
            self.seat_no = seat_no


# The Ticket class, pretty simple and self explanatory
class Ticket:
    def __init__(self, event, face_value, seat):
        #
        # event: Event object
        # face_value: int
        # seat: Seat object
        # history: list of (block_no (int), hash (int))
        #
        self.ticket_num = event.next_ticket_num
        event.next_ticket_num += 1
        self.event = event
        self.seat = seat
        self.face_value = face_value
        self.list_price = face_value # upon inception, list price = face_value
        self.for_sale = False
        self.history = []    # history is list of tuples of (block index, hash)

    def isForSale(self):
        return self.for_sale

    def mostRecentTransaction(self):
        # TO-DO: add three-way consensus check here in iteration 2
        return self.event.blockchain.findRecentTrans(self.ticket_num)

    def listTicket(self, list_price, seller_id):
        # confirm that whoever is trying to list the Ticket actually owns it
        valid_seller = (seller_id == self.mostRecentTransaction().target)
        # enforce that list_price is positive and non-zero
        if valid_seller and list_price > 0.00:
            self.for_sale = True
            self.list_price = list_price
