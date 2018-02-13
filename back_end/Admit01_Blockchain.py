import datetime as date
import hashlib as hasher

# keep track of the next usable id number to avoid duplicates amongst or
# between Users and Venues
next_unused_id = 0

# keep track of all Venues on the platform
venues = []

# The Block class, constituting an instance of a block in the chain
class Block:
    def __init__(self, index, timestamp, transaction, prev_hash, target):
        if prev_hash == None or len(prev_hash) == 0:
            # genesis
            self.index = 0
            self.timestamp = timestamp
            self.data = Transaction.genesisTransaction(target)
            self.prev_hash = self.genesisHash(512)
            self.hash = self.hashBlock()
        else:
            self.index = index # numerical index, (matching the list index of the block?)
            self.timestamp = timestamp # a datetime timestamp object
            self.data = transaction # an instance of the transaction class defined below representing the transaction for this block
                                    # in the future, if more than a single transaction is put on a block, this can be a list of transactions
            self.prev_hash = prev_hash # the hash of the previous block in the chain
            self.hash = self.hashBlock() # the new hash for this block, including all of the above fields

    # generates a hash for a block
    def hashBlock(self):
        return self.generateHash(str(self.index) + str(self.timestamp) + str(self.data) + str(self.prev_hash))

    # generates a genesis block, with a genesis transaction given a target.
    # the hash for this genesis block is a sha256 hash of 512 random characters (ascii uppercase and digits)
    @staticmethod
    def genesisBlock(target): # target is the venue
        return Block(0, date.datetime.now(), Transaction.genesisTransaction(target), genesisHash(512))

    # generates a sha256 hash given a string
    @staticmethod
    def generateHash(text):
        sha = hasher.sha256()
        sha.update(text.encode('utf-8'))
        return sha.hexdigest()

    # generates a hash of length random characters (ascii uppercase and digits)
    @staticmethod
    def genesisHash(length):
        return generateHash(''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(length)))


class Chain:
    """ Wrapper for a list of Block objects and some helper methods """
    def __init__(self):
        self.blocks = list(a1.Block(0, date.datetime.now(), None, "", event))

    def findRecentTrans(self, ticket_id):
        return Transaction()

    def mineNewBlock(self, transactions):
        self.blocks.append(Block(len(self.blocks), date.datetime.now(), transactions,
                                 a1.HashcashHeader(self).generateAcceptableHeader()))




# The Transaction class, pretty simple, to, from, value of transaction.
class Transaction:
    def __init__(self, target, source, value, content):
        self.target = target
        self.source = source
        self.value = value
        self.content = content

    # function to create a genesis transaction with a recipient (host/venue)
    def genesisTransaction(self, target):
        return Transaction(target, None, 0)


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
        self.id = next_unused_id
        next_unused_id += 1
        self.fname = fname
        self.lname = lname
        self.email_address = email_address
        self.inventory = []
        self.wallet = 0

    def getID(self):
        return self.id

    def buyTicket(self, ticket):
        #
        # ticket: Ticket object
        #
        return False

    def upgradeTicket(self, ticket):
        return False

    def search(self, text):
        return False

    def explore(self):
        return False

    def generateTicketCode(self, ticket):
        return False


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
        self.id = next_unused_id
        next_unused_id += 1
        self.name = name
        self.events = {}  # dictionary mapping events to their blockchains
        self.location = location

    def validateTicket(self, code, chain):
        return False

    def createEvent(self, name, datetime, desc):
        return Event(name, datetime, desc)

    def manageEvent(self, event):
        return False

    def createTicket(self, event, cost, ticket_class, number):
        return []

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
        self.tickets = None    # can add tickets later
        if !name or datetime < date.datetime.now():
            self.name = self.datetime = self.desc = self.blockchain = None
        else:
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
        if !section or !row or seat_no < 0:
            self.section = self.row = self.seat_no = None
        else:
            self.section = section
            self.row = row
            self.seat_no = seat_no


# The Ticket class, pretty simple and self explanitory
class Ticket:
    def __init__(self, event, face_value, seat):
        #
        # event: Event object
        # face_value: int
        # seat: Seat object
        # history: list of (block_no (int), hash (int))
        #
        self.event = event
        self.face_value = face_value
        self.list_price = face_value # upon inception, list price = face_value
        self.for_sale = False
        self.history = None # history is list of tuples of block index, hash

    def isForSale(self):
        return self.for_sale

    def listTicket(self, list_price, seller_id):
        self.for_sale = True
        # TO-DO: finish the rest
        return False


class HashcashHeader:
    def __init__(self, chain):
        date.datetime.tzname("CDT")
        if type(chain) != a1.Chain:
            self.version = 1
            self.bits = 20
            self.date = date.datetime.now().strftime("%y%m%d%H%M%S")
            self.data = None
            self.randstring = ''.join(
                random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(16))
            self.counter = 0
            self.hash = ""
            self.prev_hashes = list()
        else:
            self.version = 1
            self.bits = 20
            self.date = date.datetime.now().strftime("%y%m%d%H%M%S")
            self.data = chain.blocks[-1]
            self.randstring = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(16))
            self.counter = 0
            self.hash = ""
            self.prev_hashes = list()

    def __str__(self):
        return ':'.join(self.version, self.bits, self.date, self.data, self.randstring, self.counter)

    def generateAcceptableHeader(self):
        self.counter = randint()
        result = "11111"
        # randstring = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase + '+' + '/') for _ in range(16))
        while result[0:5] != "00000" or result[5:] in self.prev_hashes:
            self.counter += 1
            result = genSHA1Hash(self)
        print("Got a matching hash\n")
        print(result)
        self.prev_hashes.append(self.hash[5:])
        self.hash = result
        return True

    def genSHA1Hash(self):
        sha = hasher.sha1()
        sha.update(self.toString().encode('utf-8'))
        return sha.hexdigest()
