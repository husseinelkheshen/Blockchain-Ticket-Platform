
from ../../back_end/Admit01_Blockchain.py import *
import datetime as date
import pytest

class Iter1Tests:
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

    def test_minenewblock(self):
        # event = Event("sample event", date.datetime.now(), "a test event")
        venue = Venue("sample venue", "Chicago")
        # seat = Seat("GA", "1", 1)
        # event = venue.createEvent("sample event", date.datetime.now())
        # venue.createTicket(event, 20, seat)
        # transaction = Transaction.genesisTransaction(event)
        blockchain = Chain()
        mirror = Chain()
        initblock = Block(0, date.datetime.now(), list(Transaction("target", "source", 20, 1)), "fakehash")
        blockchain.append(initblock)
        mirror.append(initblock)
        secondblock = Block(1, date.datetime.now(), list(Transaction("newtarget", "target", 30, 1)), "")
        blockchain.append(secondblock)
        mirror.append(secondblock)
        assert(blockchain.mineNewBlock(list(mirror)) == True)
        thirdblock = Block(2, date.datetime.now(), list(Transaction("anothertarget", "newtarget", 25, 1)), "")
        blockchain.append(thirdblock)
        mirror.append(thirdblock)
        assert(blockchain.mineNewBlock(list(mirror)) == True)
        ######
        ### testing constant truths of mining new blocks
        # prev_hash equals hash of previous block tests
        assert(blockchain.blocks[0].hash == blockchain.blocks[1].prev_hash)
        assert(blockchain.blocks[1].hash == blockchain.blocks[2].prev_hash)
        assert(mirror.blocks[0].hash == mirror.blocks[1].prev_hash)
        assert(mirror.blocks[1].hash == mirror.blocks[2].prev_hash)
        assert(blockchain.blocks[1].prev_hash == mirror.blocks[1].prev_hash)
        assert(blockchain.blocks[2].prev_hash == mirror.blocks[2].prev_hash)
        assert(blockchain.blocks[1].hash == mirror.blocks[1].hash)
        assert(blockchain.blocks[2].hash == mirror.blocks[2].hash)
        # tests hashes aren't the same
        assert(blockchain.blocks[0].hash != blockchain.blocks[1].hash)
        assert(blockchain.blocks[1].hash != blockchain.blocks[2].hash)
        # hashes after genesis hash are the same and equal to "00000"
        assert(blockchain.blocks[1].hash[0:5] == blockchain.blocks[2].hash[0:5])
        assert(mirror.blocks[1].hash[0:5] == mirror.blocks[2].hash[0:5])
        assert(blockchain.blocks[1].hash[0:5] == "00000")
        assert(mirror.blocks[1].hash[0:5] == "00000")









