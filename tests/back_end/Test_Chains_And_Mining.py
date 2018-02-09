
from ../../back_end/Admit01_Blockchain.py import *
import datetime as date
import pytest

class Iter1Tests:
    def test_hashcash(self):
        badinit = HashcashHeader("pandas")
        # test constructor failure
        assert(badinit.data is None)
        event = Event("sample event", date.datetime.now(), "a test event")
        venue = Venue("sample venue", "Chicago")
        # transaction = Transaction.genesisTransaction(event)
        blockchain = Chain(event, Ticket(event, 20, None))
        initheader = HashcashHeader(blockchain)
        # test constructor success
        assert(initheader.data == blockchain[-1])
        initheader.generateAcceptableHeader()
        margin = date.timedelta(hours=3)
        ### tests on chain of length 1 - adding to genesis block
        assert(initheader.hash[0:5] == "00000")
        assert(initheader.data.index == 0)
        assert(date.datetime.now() - margin <= initheader.timestamp <= date.datetime.now() + margin)
        blockchain.append(Block(1, date.timetime.now(), None, blockchain[-1].hash, initheader.hash))
        nextheader = HashcashHeader(blockchain)
        nextheader.generateAcceptableHeader()
        ### tests adding a new block to an existing chain - non genesis block
        assert(nextheader.hash[0:5] == "00000")
        assert(nextheader.data.index == 1)
        assert(date.datetime.now() - margin <= initheader.timestamp <= date.datetime.now() + margin)

    def test_minenewblock(self):
        event = Event("sample event", date.datetime.now(), "a test event")
        venue = Venue("sample venue", "Chicago")
        # transaction = Transaction.genesisTransaction(event)
        blockchain = Chain(event, Ticket(event, 20, None))
        blockchain.mineNewBlock(None)
        # testing mining for second block
        assert(len(blockchain.blocks) == 2)
        # testing mining for third block
        blockchain.mineNewBlock(None)
        assert(len(blockchain.blocks) == 3)
        ######
        ### testing constant truths of mining new blocks
        # prev_hash equals hash of previous block tests
        assert(blockchain.blocks[0].hash == blockchain.blocks[1].prev_hash)
        assert(blockchain.blocks[1].hash == blockchain.blocks[2].prev_hash)
        # tests hashes aren't the same
        assert(blockchain.blocks[0].hash != blockchain.blocks[1].hash)
        assert(blockchain.blocks[1].hash != blockchain.blocks[2].hash)
        # hashes after genesis hash are the same and equal to "00000"
        assert(blockchain.blocks[1].hash[0:5] == blockchain.block[2].hash[0:5])
        assert(blockchain.blocks[1].hash[0:5] == "00000")









