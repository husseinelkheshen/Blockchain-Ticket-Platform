from blockchain.Admit01_Blockchain import *
import datetime as date

    # def test_hashcash(self):
    #     badinit = HashcashHeader("pandas")
    #     # test constructor failure
    #     assert(badinit.data is None)
    #     event = Event("sample event", date.datetime.now(), "a test event")
    #     venue = Venue("sample venue", "Chicago")
    #     # transaction = Transaction.genesisTransaction(event)
    #     blockchain = Chain()
    #     initheader = HashcashHeader(blockchain)
    #     # test constructor success
    #     assert(initheader.data == str(blockchain[-1]))
    #     initheader.generateAcceptableHeader()
    #     margin = date.timedelta(hours=3)
    #     ### tests on chain of length 1 - adding to genesis block
    #     assert(initheader.hash[0:5] == "00000")
    #     assert(initheader.data.index == 0)
    #     assert(date.datetime.now() - margin <= initheader.timestamp <= date.datetime.now() + margin)
    #     blockchain.append(Block(1, date.timetime.now(), None, blockchain[-1].hash, initheader.hash))
    #     nextheader = HashcashHeader(blockchain)
    #     nextheader.generateAcceptableHeader()
    #     ### tests adding a new block to an existing chain - non genesis block
    #     assert(nextheader.hash[0:5] == "00000")
    #     assert(nextheader.data.index == 1)
    #     assert(date.datetime.now() - margin <= initheader.timestamp <= date.datetime.now() + margin)
# @staticmethod
def test_minenewblock():
    # event = Event("sample event", date.datetime.now(), "a test event")
    venue = Venue("sample venue", "Chicago")
    # seat = Seat("GA", "1", 1)
    # event = venue.createEvent("sample event", date.datetime.now())
    # venue.createTicket(event, 20, seat)
    # transaction = Transaction.genesisTransaction(event)
    blockchain = Chain()
    mirror = Chain()
    initblock = Block(0, date.datetime.now(), [Transaction("target", "source", 20, 1)], "")
    blockchain.blocks.append(initblock)
    mirror.blocks.append(initblock)
    assert(blockchain.mineNewBlock([mirror]) == True)
    secondblock = Block(1, date.datetime.now(), [Transaction("newtarget", "target", 30, 1)], blockchain.blocks[-1].hash)
    blockchain.blocks.append(secondblock)
    mirror.blocks.append(secondblock)
    # tests successful mining of second block
    assert(blockchain.mineNewBlock([mirror]) == True)
    thirdblock = Block(2, date.datetime.now(), [Transaction("anothertarget", "newtarget", 25, 1)], blockchain.blocks[-1].hash)
    blockchain.blocks.append(thirdblock)
    mirror.blocks.append(thirdblock)
    # tests successful mining of third block
    assert(blockchain.mineNewBlock([mirror]) == True)
    ######
    ### testing constant truths of mining new blocks
    # prev_hash equals hash of previous block tests
    assert(blockchain.blocks[0].hash == blockchain.blocks[1].prev_hash)
    assert(blockchain.blocks[1].hash == blockchain.blocks[2].prev_hash)
    assert(mirror.blocks[0].hash == mirror.blocks[1].prev_hash)
    assert(mirror.blocks[1].hash == mirror.blocks[2].prev_hash)
    # prev_hashes equal, current hashes equal
    assert(blockchain.blocks[1].prev_hash == mirror.blocks[1].prev_hash)
    assert(blockchain.blocks[2].prev_hash == mirror.blocks[2].prev_hash)
    assert(blockchain.blocks[1].hash == mirror.blocks[1].hash)
    assert(blockchain.blocks[2].hash == mirror.blocks[2].hash)
    # tests hashes aren't the same
    assert(blockchain.blocks[0].hash != blockchain.blocks[1].hash)
    assert(blockchain.blocks[1].hash != blockchain.blocks[2].hash)
    # testing 12 bits of 0, "000"
    assert(blockchain.blocks[1].hash[0:3] == blockchain.blocks[2].hash[0:3])
    assert(mirror.blocks[1].hash[0:3] == mirror.blocks[2].hash[0:3])
    assert(blockchain.blocks[1].hash[0:3] == "000")
    assert(mirror.blocks[1].hash[0:3] == "000")









