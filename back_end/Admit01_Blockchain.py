
import datetime as date
import hashlib as hasher

# The Block class, constituting an instance of a block in the chain
class Block:
    def __init__(self, index, timestamp, transaction, prev_hash, target):
        if len(prev_hash):
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
    def genesisBlock(self, target): # target is the venue
        return Block(0, date.datetime.now(), Transaction.genesisTransaction(target), self.genesisHash(512))

    # generates a sha256 hash given a string
    def generateHash(self, text):
        sha = hasher.sha256()
        sha.update(text.encode('utf-8'))
        return sha.hexdigest()

    # generates a hash of length random characters (ascii uppercase and digits)
    def genesisHash(self, length):
        return generateHash(''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(length)))


# The Chain class, really just for ease of debugging, no really necessary
class Chain:
    def __init__(self, event, ticket, host):
        self.event = event
        self.ticket = ticket
        self.blocks = list(Block.genesisBlock(host))

    def findRecentTrans(self, ticket_id):
        return Transaction()

    def mineNewBlock(self):
        return Block;



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


# The User class
class User:
    def __init__(self, id, inventory, wallet):
        self.id = id
        self.inventory = inventory
        self.wallet = wallet

    def buyTicket(self, event):
        return False

    def upgradeTicket(self, ticket):
        return False

    def listTicket(self, ticket):
        return False

    def search(self, text):
        return False

    def explore(self):
        return False

    def generateTicketCode(self, ticket):
        return False


#The host class will inherit the user class, and add new functionalities
class Host(User):
    def createEvent(self, name, date, time, desc):
        return Event(name, date, time, desc, None, None)

    def manageEvent(self, event):
        return False

    def createTicket(self, event, cost, ticket_class, number):
        i = 0
        tickets = []
        while i < number:
            tickets.append(Ticket(event, cost, ticket_class))
            i += 1

        return tickets

    def manageTicket(self, event, ticket_class):
        return False

    def scheduleRelease(self, event, ticket_class, number):
        return False


#The Venue class with inherit the host class, and add the ability to validate a ticket
class Venue(Host):
    def __init__(self, name, blockchains, events, location):
        self.name = name
        self.blockchains = blockchains # dictionary of blockchains
        self.location = location

    def validateTicket(self, code, chain):
        return False


#The Event class, pretty simple and self explanitory
class Event:
    def __init__(self, name, date, time, desc, tickets, classes):
        self.name = name
        self.date = date
        self.time = time
        self.desc = desc
        self.tickets = tickets # number of tickets available for the event?
        self.classes = classes # classes of tickets, like GA, upper level, etc. Represented in a list
        self.blockchain = initialBlockchain() # do this

    def initialBlockchain(self):
        return Chain() # do this


# The Ticket class, pretty simple and self explanitory
class Ticket:
    def __init__(self, event, cost, ticket_class, history):
        self.event = event
        self.cost = cost # the (base) cost of the ticket?
        self.ticket_class = ticket_class # the class of the ticket
        self.history = history # history is list of tuples of block index, hash


class HashcashHeader:
    def __init__(self, bits, data, counter):
        date.datetime.tzname("CDT")
        self.version = 1
        self.bits = bits
        self.date = date.datetime.now().strftime("%y%m%d%H%M%S")
        self.data = data
        self.randstring = ""
        self.counter = 0
        self.hash = ""

    def toString(self):
        return ':'.join(self.version, self.bits, self.date, self.data, self.randstring, self.counter)

    def generateAcceptableHeader(self):
        self.counter = randint()
        result = "11111"
        randstring = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_uppercase + '+' + '/') for _ in range(16))
        while result[0:5] != "00000":
            self.counter += 1
            result = genSHA1Hash(self)
        print("Got a matching hash\n")
        print(result)
        return self

    def genSHA1Hash(self):
        sha = hasher.sha1()
        sha.update(self.toString().encode('utf-8'))
        return sha.hexdigest()

