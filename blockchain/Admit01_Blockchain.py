from random import *
import datetime as date
import hashlib as hasher
import pyqrcode as qr
import re
import string
import operator
import copy


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
    def getVenue(venue_id):
        """
        Get Venue object from its id

            venue_id: int

        Returns a Venue object

        """
        if venue_id is None or venue_id < 0:
            return None

        venues = Trackers.registered_venues
        for city in venues:
            for venue_name in venues[city]:
                if venue_id == venues[city][venue_name].id:
                    return venues[city][venue_name]

        return None

    @staticmethod
    def getUser(user_id):
        """
        Get User object from its id

            user_id: int

        Returns a User object

        """
        if user_id is None or user_id < 0:
            return None

        users = Trackers.registered_users
        for email in users:
            if user_id == users[email].id:
                return users[email]

        return None

    @staticmethod
    def getNextUserVenueID():
        """
        Retrieves the next usable ID for User or Venue

        Returns an int

        """
        next_id = Trackers.next_user_venue_id
        Trackers.next_user_venue_id += 1
        return next_id

    @staticmethod
    def getNextEventID():
        """
        Retrieves the next usable ID for Event

        Returns an int

        """
        next_id = Trackers.next_event_id
        Trackers.next_event_id += 1
        return next_id


# The Block class, constituting an instance of a block in the chain
class Block:
    """
    Class for defining Blocks, which are the units within the chain which
    store the list of most recent Transactions along with their timestamps
    """
    def __init__(self, index, timestamp, transactions, prev_hash):
        """
        Block constructor

            index: int
            timestamp: datetime object
            transactions: list of Transactions
            prev_hash: string

        """
        valid_index = (index is not None) and (index >= 0)
        if(not valid_index or (timestamp is None) or (transactions is None)):
            self. index = self.timestamp = self.data = self.prev_hash = self.hash = None
        elif prev_hash is None or len(prev_hash) == 0:
            # genesis
            self.index = 0
            self.timestamp = timestamp
            self.data = transactions
            self.prev_hash = ""
            self.hash = ""
            self.nonce = ""
        else:
            self.index = index # numerical index, (matching the list index of the block?)
            self.timestamp = timestamp # a datetime timestamp object
            self.data = transactions # a list of transactions
            self.prev_hash = prev_hash # the hash of the previous block in the chain
            self.hash = ""  # the new hash for this block, generated in hashcash format
                            # where data content of hashcash is a string representation of the block
            self.nonce = ""

    def hashBlock(self, nonce):
        """
        Return a Block's hash given a nonce

            nonce: string

        Returns a string

        """
        return Block.genSHA1Hash(':'.join(["1", "12",
                                 self.timestamp.strftime("%y%m%d%H%M%S"),
                                 str(self), nonce]))

    @staticmethod
    def genSHA1Hash(text):
        """
        Generates a hash given text input

            text: string

        Returns a string

        """
        sha = hasher.sha1()
        sha.update(text.encode('utf-8'))
        return sha.hexdigest()

    def __str__(self):
        """ Default to_string method """
        return str(self.index) + str(self.data) + self.prev_hash


class Chain:
    """ Wrapper for a list of Block objects and some helper methods """
    def __init__(self):
        """ Chain constructor """
        self.blocks = []    # no need for a genesis block here
        self.prev_hashes = []

    def findRecentBlockTrans(self, ticket_id):
        """
        Finds the most recent block and transaction in which a given ticket
        was involved

            ticket_id: int

        Returns Block object, Transaction object

        """
        recentBlock = None
        recentTrans = None

        chainlength = len(self.blocks)
        foundTrans = False

        if chainlength != 0:
            block = -1
            while abs(block) <= chainlength:
                translength = len(self.blocks[block].data)
                trans = -1
                while abs(trans) <= translength:
                    this_block = self.blocks[block]
                    if this_block.data[trans].ticket_num == ticket_id:
                        recentBlock = this_block
                        recentTrans = this_block.data[trans]
                        foundTrans = True
                        break
                    trans -= 1

                if foundTrans:
                    break
                block -= 1

        return recentBlock, recentTrans

    def mineNewBlock(self, otherchains):
        """
        Allows a Chain to mine the hash for the most recently appended block

            otherchains: list of Chain objects

        Returns a boolean

        """
        if self.blocks[-1].hash:
            # If the most recent block already has a hash, then there is no hash to be mined.
            # Therefore we return false.
            return False
        else:
            # counter is a component of the nonce that we generate
            counter = randint(0, 65536)
            # result is the hash that results from our hashing of the block with our current nonce
            # it is initialized to a garbage value of "11111" to satisfy the while loop condition
            result = "111"
            # randstring is the other component of the nonce that we generate
            randstring = ''.join(choice(string.ascii_uppercase +
                                        string.digits + string.ascii_lowercase +
                                         '+' + '/') for _ in range(16))
            # while the first 12 bits are not 0, or the hash created matches a previous hash
            while result[0:3] != "000" or result in self.prev_hashes:
                # increment the counter, generate a hash, store it in result
                counter += 1
                result = Block.genSHA1Hash(
                    ':'.join(["1", "12", self.blocks[-1].timestamp.strftime(
                    "%y%m%d%H%M%S"), str(self.blocks[-1]),
                    randstring, str(counter)]))
            if len(self.blocks) > 1:
                # if there are multiple blocks, append the hash of the second block from the back
                # to the list of previous hashes of the chain
                # if this is the first block, there is no previous to worry about
                self.prev_hashes.append(self.blocks[-2].hash)
            nonce = randstring + ":" + str(counter)
            for chain in otherchains:
                # if the hash of any of the mirror chains with this nonce isn't the same
                # one of the chains is corrupt, return false
                if chain.blocks[-1].hashBlock(nonce) != result:
                    return False
            # put the hash on all of the chains' final blocks, including this one
            otherchains.append(self)
            for chain in otherchains:
                chain.blocks[-1].hash = result
                chain.blocks[-1].nonce = nonce
            return True


class Transaction:
    """
    Class for defining Transactions, which store information about
    Ticket transfers between Users and Venues, as well as the
    creation and destruction of Ticket objects
    """
    def __init__(self, target, source, value, ticket_num):
        """
        Transaction constructor

            target: int
            source: int
            value: int
            ticket_num: int

        """
        has_target_or_source = (target != None) or (source is not None)
        has_ticket_num = (ticket_num is not None) and (ticket_num >= 0)
        valid_value = (value is not None) and (value >= 0)
        if not has_target_or_source or not has_ticket_num or not valid_value:
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
            self.tags_pref = {}
            self.location_pref = {}
            self.venue_pref = {}
            # add this User to the catalog of registered Users
            Trackers.registered_users[email_address] = self
        else:
            self.id = self.fname = self.lname = self.email_address = None
            self.inventory = self.wallet = None

    def getID(self):
        """
        Getter for User's ID number

        Returns an int

        """
        return self.id

    def buyTicket(self, ticket):
        """
        Allows a User to buy a listed ticket

            ticket: Ticket object

        Returns a boolean

        """

        if ticket is None:
            return False

        # check if involved objects are valid
        if (self.id == None
            or ticket.event == None
            or ticket.seat == None
            or ticket.face_value == None
            or ticket.list_price == None
            or ticket.for_sale == None
            or ticket.history == None):
            return False

        # check if the event has already transpired
        if ticket.event.datetime < date.datetime.now():
            return False

        # check if ticket is for sale
        if not ticket.for_sale:
            return False

        # check if user calling has enough money in wallet
        if ticket.list_price > self.wallet:
            return False

        # check if user already owns the ticket
        if ticket in self.inventory:
            return False

        # get correct source
        recent_trans = ticket.mostRecentTransaction()
        if recent_trans is None:
            return False
        owner = recent_trans.target

        # get owner object
        owner_obj = Trackers.getVenue(owner)
        if owner_obj is None:    # seller is not a Venue
            owner_obj = Trackers.getUser(owner)
        if owner_obj is None:    # seller is not a User / does not exist
            return False

        # generate new transactions
        new_transactions = []
        new_transactions.append(Transaction(self.id,
                                            owner,
                                            ticket.list_price,
                                            ticket.ticket_num))

        # post the transaction to a new block
        prev_hash = None
        new_block_index = len(ticket.event.blockchain.blocks)
        if new_block_index > 0:
            prev_hash = ticket.event.blockchain.blocks[-1].hash
        new_block = Block(new_block_index,
                          date.datetime.now(),
                          new_transactions,
                          prev_hash)

        # append the new block to both blockchains
        ticket.event.blockchain.blocks.append(new_block)
        ticket.event.venue.events[ticket.event.id][1].blocks.append(new_block)

        # mine one new block
        if ticket.event.blockchain.mineNewBlock([ticket.event.venue.events[ticket.event.id][1]]):
            new_block_hash = ticket.event.blockchain.blocks[-1].hash
            # add record and hash to ticket's history
            ticket.history.append((new_block_index, new_block_hash))
        else:
            del ticket.event.blockchain.blocks[-1]
            del ticket.event.venue.events[event.id][1].blocks[-1]
            return False

        # add record and hash to ticket's history
        ticket.history.append((new_block_index, new_block_hash))

        # add ticket to user's inventory
        self.inventory.append(ticket)

        # transfer funds from buyer to seller
        self.wallet -= ticket.list_price
        owner_obj.wallet += ticket.list_price

        # mark ticket as sold
        ticket.for_sale = False

        # signify completion
        return True

    def upgradeTicket(self, owned_ticket, new_ticket):
        """
        Allows a User to upgrade an owned ticket for another listed ticket

            owned_ticket: Ticket object
            new_ticket: Ticket object

        Returns a boolean

        """

        if new_ticket is None:
            return False

        # check if involved objects are valid
        if (self.id == None
            or new_ticket == None
            or owned_ticket == None
            or new_ticket.event == None
            or new_ticket.seat == None
            or new_ticket.face_value == None
            or new_ticket.list_price == None
            or new_ticket.for_sale == None
            or new_ticket.history == None):
            return False

        # check if the event has already transpired
        if new_ticket.event.datetime < date.datetime.now():
            return False

        # check if ticket is for sale
        if not new_ticket.for_sale:
            return False

        # check if new ticket is more valuable than old ticket
        if new_ticket.list_price <= owned_ticket.list_price:
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

        # get correct owner
        recent_trans = new_ticket.mostRecentTransaction()
        if recent_trans is None:
            return False
        owner = recent_trans.target

        # make sure that owner is a venue
        owner_venue = Trackers.getVenue(owner)
        if owner_venue is None:
            return False

        # generate new transactions
        new_transactions = []
        new_transactions.append(Transaction(self.id,
                                            owner,
                                            new_ticket.list_price,
                                            new_ticket.ticket_num))
        new_transactions.append(Transaction(owner,
                                            self.id,
                                            owned_ticket.list_price,
                                            owned_ticket.ticket_num))

        # post the transactions to a new block
        prev_hash = None
        new_block_index = len(new_ticket.event.blockchain.blocks)
        if new_block_index > 0:
            prev_hash = new_ticket.event.blockchain.blocks[-1].hash
        new_block = Block(new_block_index,
                          date.datetime.now(),
                          new_transactions,
                          prev_hash)

        # append the new block to both blockchains
        new_ticket.event.blockchain.blocks.append(new_block)
        new_ticket.event.venue.events[new_ticket.event.id][1].blocks.append(new_block)

        # mine one new block
        if new_ticket.event.blockchain.mineNewBlock([new_ticket.event.venue.events[new_ticket.event.id][1]]):
            new_block_hash = new_ticket.event.blockchain.blocks[-1].hash
            # add record and hash to ticket's history
            new_ticket.history.append((new_block_index, new_block_hash))
            owned_ticket.history.append((new_block_index, new_block_hash))
        else:
            del new_ticket.event.blockchain.blocks[-1]
            del new_ticket.event.venue.events[new_ticket.event.id][1].blocks[-1]
            return False

        # remove upgraded ticket from user inventory and add new ticket
        self.inventory.remove(owned_ticket)
        self.inventory.append(new_ticket)

        # transfer funds from user to venue
        upgrade_price = new_ticket.list_price - owned_ticket.list_price
        self.wallet -= upgrade_price
        owner_venue.wallet += upgrade_price

        # add appropriate funds to seller's wallet (iteration 2)

        # mark old ticket as for sale, and new as sold
        owned_ticket.for_sale = True
        new_ticket.for_sale = False

        # signify completion
        return True

    @staticmethod
    def search(text="", datetime=None, date_range=0):
        """
        A search function for retrieving a list of Events by given criteria

        A call with none of the optional parameters filled will result in a
        list of all the currently posted Events

            text: a string
            datetime: a Datetime object
            date_range: int

        Returns a list of Event objects

        """
        all_events = []
        for city in Trackers.registered_venues:
            for name in Trackers.registered_venues[city]:
                venue = Trackers.registered_venues[city][name]
                for event_id in venue.events:
                    all_events.append(venue.events[event_id][0])
        if not text and not datetime:
            return all_events    # return all events if no search criteria
        elif not datetime:
            filtered_events = all_events
        else:
            # set up date range
            lower_bound = datetime.replace(
                hour=0, minute=0, second=0, microsecond=0)
            upper_bound = lower_bound + date.timedelta(days=date_range+1)
            # apply the date filter
            filtered_events = []
            for event in all_events:
                if lower_bound <= event.datetime < upper_bound:
                    filtered_events.append(event)

        if not text:
            return filtered_events

        # apple the text filter
        search_results = []    # each entry a tuple of (event, score)
        search_words = text.split()
        search_re = re.compile(r'\b%s\b' % '\\b|\\b'.join(search_words),
                               flags=re.IGNORECASE)
        for event in filtered_events:
            event_str = (event.name + ' ' + event.desc + ' ' +
                         event.venue.name + ' ' + event.venue.location)
            score = len(search_re.findall(event_str))
            if score > 0:
                search_results.append((event, score))

        # return [] if no results match filters
        if len(search_results) == 0:
            return []

        # sort search results by score
        search_results.sort(key=operator.itemgetter(1), reverse=True)
        return [result[0] for result in search_results]

    def explore(self):
        # iteration 2
        pass

    def generateTicketCode(self, venue, event, ticket):
        """
        Generate a QR code object if the User owns the Ticket

            venue: Venue object
            event: Event object
            ticket: Ticket object

        Returns a pyqrcode object

        """
        ticket_code = None
        # confirm Event is valid
        if event.id in venue.events and event == venue.events[event.id][0]:
            # confirm Ticket is valid
            if ticket in event.tickets:
                current_owner = ticket.mostRecentTransaction().target
                # confirm Ticket ownership
                if self.id == current_owner:
                    ticket_data = ("event_id = " + str(event.id) +
                                   "\nticket_num = " + str(ticket.ticket_num) +
                                   "\ncurrent_owner = " + str(current_owner) +
                                   "\nhash = " + ticket.history[-1][1])
                    # generate ticket code
                    ticket_code = qr.create(ticket_data)

        return ticket_code    # call ticket_code.png('filename.png') to generate

    def getOwnedTickets(self):
        """
        Gets list of ticket_ids in a user's inventory

        Returns a list of ints

        """
        return [ticket.ticket_num for ticket in self.inventory]

#     def updatePreferences(self, ticket, action):
#         """
#         Updates preferences in a user's preferences dictionary

#         ticket: the ticket being purchased or sold when fn is called
#         action: string indicating buy, sell or upgrade

#         """
#         venue = ticket.event.venue
#         loc = venue.location
#         #tags = tags_list (tag generator for ticket.event.name and ticket.event.desc)

#         tags_dict = self.tags_pref
#         loc_dict = self.location_pref
#         venue_dict = self.venue_pref

#         if action is "buy":
#             if venue in venue_dict
#                 venue_dict[venue] += 4
#             else
#                 venue_dict[venue] = 4

#             if location in loc_dict
#                 loc_dict[location] += 5
#             else
#                 loc_dict[location] = 5

#             for i, elem in enumerate(tags_list)
#                 if elem in tags_dict
#                      tags_dict[elem] += 2
#                 else
#                     tags_dict[elem] = 2

#         if action is "upgrade":
#             venue_dict[venue] += 2
#             loc_dict[location] += 3

#             for i, elem in enumerate(tags_list)
#                 if elem in tags_dict
#                      tags_dict[elem] += 1
#                 else
#                     tags_dict[elem] = 1

#         if action is "sell":
#             venue_dict[venue] -= 2
#             loc_dict[location] -= 2

#         return True
# """


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
            # start venue with zero balance
            self.wallet = 0
        else:
            self.id = self.name = self.events = self.location = self.wallet = None

    def validateTicketCode(self, event_id, ticket_num, user_id, hash):
        # iteration 2
        pass

    def createEvent(self, name, datetime, desc):
        """
        Allows a Venue to create an Event and save a clone of its blockchain

            name: string
            datetime: DateTime object
            desc: string

        Returns an Event object

        """
        event = Event(name, datetime, desc)
        if event.id is None:
            return None
        event.venue = self
        self.events[event.id] = (event, copy.deepcopy(event.blockchain))
        return event

    def manageEvent(self, event, name, new_date, desc):
        """
        Allows a Venue to edit Event date, time and description

            event: Event object
            name: string
            new_date: DateTime object
            desc: string

        Returns a boolean

        """
        current_date = date.datetime.now()
        invalid_date = False

        if new_date is None or new_date < current_date:
            invalid_date = True

        if event is None or name is None or invalid_date:
            return False

        else:
            event.name = name
            event.datetime = new_date
            event.desc = desc

        return True

    def createTicket(self, event, face_value, seat):
        """
        Allows a Venue to create a new Ticket for one of its Events

            event: Event object
            face_value: int
            seat: Seat object

        Returns a Ticket object

        """
        new_ticket = None
        # make sure Venue is valid
        if self.id is not None:
            # make sure Event is valid
            if (event is not None and
                event.id is not None and
                event.id in self.events and
                event == self.events[event.id][0]):
                # make sure Ticket for this Seat does not already exist
                # make sure Ticket has a positive face value
                valid_face_value = face_value is not None and face_value >= 0
                if seat is None or not valid_face_value:
                    return None
                valid_ticket = True
                for ticket in event.tickets:
                    if (ticket.seat.section == seat.section and
                        ticket.seat.row == seat.row and
                        ticket.seat.seat_no == seat.seat_no):
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

        return new_ticket

    def createTickets(self, event, face_value, section, row, seat_nos):
        """
        Allows a Venue to create a multiple Tickets for one of its Events

            event: Event object
            face_value: int
            section: string
            row: string
            seat_nos: list (int)

        Returns a list of Ticket objects

        """
        if not (section and row and seat_nos):
            return []

        # create seats
        seats = []
        for seat_no in seat_nos:
            new_seat = Seat(section, row, seat_no)
            if new_seat is not None and new_seat not in seats:
                seats.append(new_seat)

        # create tickets
        tickets = []
        for seat in seats:
            ticket = createTicket(event, face_value, seat)
            if ticket is not None:
                tickets.append(ticket)

        return tickets

    def venueTickets(self, event_id):
        """
        Allows a Venue to find a list of tickets it owns in each Event by ticket_num

            event_id: int

        Returns a list of ints
        """

        if event_id is None or event_id < 0 or event_id >= Trackers.next_event_id:
            return False

        event_blockchain = self.events[event_id][0].blockchain
        chainlength = len(event_blockchain.blocks)

        foundTickets = []
        venueTickets = []

        assert chainlength == 1

        if chainlength != 0:
            block = -1
            while abs(block) <= chainlength:
                translength = len(event_blockchain.blocks[block].data)

                assert translength == 1

                trans = -1
                while abs(trans) <= translength:
                    this_block = event_blockchain.blocks[block]
                    ticket_id = this_block.data[trans].ticket_num
                    if ticket_id not in foundTickets:
                        foundTickets.append(ticket_id)

                        assert len(foundTickets) == 1

                        if this_block.data[trans].target == self.id:
                            venueTickets.append(ticket_id)

                            assert len(venueTickets) == 1

                    trans -= 1
                block -= 1

        assert len(venueTickets) == 1

        if len(venueTickets) == 0:
            return None

        return venueTickets.sort()

    def manageTickets(self, event, new_price, section, row, seat_num):
        """
        Allows a Venue to edit Ticket price by section, row and seat number

            event: Event object
            new_price: int
            section: string
            row: string
            seat_num: int

        Returns a boolean

        """
        invalid_price = False
        if(new_price is None or new_price < 0):
            invalid_price = True

        if(event is None or invalid_price):
            return False

    def scheduleRelease(self, event, ticket_class, date, number):
        # iteration 2
        pass


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

    def rwValidation(self):
        """
        Validates the blockchains on the Event and Venue nodes to make sure
        chains are not broken and that the chains are in sync

        Returns a boolean

        """
        i = 1
        valid = self.blockchain.blocks[0].hash == self.venue.events[self.id][1].blocks[0].hash \
            and self.blockchain.blocks[0].prev_hash == self.venue.events[self.id][1].blocks[0].prev_hash
        if not valid:
            return False
        while i < len(self.blockchain.blocks) - 1:
            valid = self.blockchain.blocks[i].hashBlock(self.blockchain.blocks[i].nonce) == self.blockchain.blocks[i+1].prev_hash
            if valid:
                valid = self.venue.events[self.id][1].blocks[i].hashBlock(self.venue.events[self.id][1].blocks[i].nonce) == \
                    self.venue.events[self.id][1].blocks[i+1].prev_hash
                if valid:
                    i += 1
                else:
                    return False
            else:
                return False
        if self.blockchain.blocks[-1].hash == self.venue.events[self.id][1].blocks[-1].hash:
            return True
        else:
            return False


class Seat:
    """ Class to uniquely identify a seat within a Venue """
    def __init__(self, section, row, seat_no):
        """
        Seat constructor

            section: string
            row: string
            seat_no: int

        """
        if not section or not row or type(seat_no) is not int or seat_no < 0:
            self.section = self.row = self.seat_no = None
        else:
            self.section = section
            self.row = row
            self.seat_no = seat_no


class Ticket:
    """
    Class to uniquely identify a Ticket with relevant attributes
    including Seat, value and History
    """
    def __init__(self, event, face_value, seat):
        """
        Ticket constructor

            event: Event object
            face_value: int
            seat: Seat object

        """

        valid_face_value = (face_value is not None) and (face_value >= 0)

        if (not valid_face_value or event is None or seat is None):
            self.ticket_num = self.event = self.seat = None
            self.face_value = self.list_price = self.for_sale = self.history = None
        else:
            self.ticket_num = event.next_ticket_num
            event.next_ticket_num += 1
            self.event = event
            self.seat = seat
            self.face_value = face_value
            self.list_price = face_value # upon inception, list price = face_value
            self.for_sale = False
            self.history = []    # history is list of tuples of (block index, hash)
            self.isScheduled = False

    def isForSale(self):
        """
        Getter for for_sale attribute

        Returns a boolean

        """
        return self.for_sale

    def mostRecentTransaction(self):
        """
        Find and return the most recent transaction that this Ticket
        was involved in after performing validation and consensus checks

        Returns a Transaction object

        """
        assert self.event is not None
        valid_chains = self.event.rwValidation()
        if not valid_chains:    # chain broken or nodes out of sync
            print('ERROR: Blockchain for event #' +
                  str(self.event.id) + 'is broken')
            return None
        # blockchains at both nodes are identical and unbroken
        blockchain = self.event.blockchain    # "single version of the truth"
        # ensure ticket history matches blockchain records
        block, txn = blockchain.findRecentBlockTrans(self.ticket_num)
        consensus = (self.history[-1] == (block.index, block.hash))
        if consensus:
            return txn

        return None


    def listTicket(self, list_price, seller_id):
        """
        List this Ticket for sale at a specified price

            list_price: float
            seller_id: int

        Returns a boolean

        """
        # confirm that whoever is trying to list the Ticket actually owns it
        mostRecentTrans = self.mostRecentTransaction()
        if mostRecentTrans is not None:
            valid_seller = (seller_id == mostRecentTrans.target)
            # enforce that list_price is positive and non-zero
            if valid_seller and list_price >= 0.00:
                self.for_sale = True
                self.list_price = list_price
                return True

        return False
