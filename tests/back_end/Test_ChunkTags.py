from blockchain.Admit01_Blockchain import *
from datetime import datetime
from datetime import timedelta
import copy

testUser1 = User("John", "Doe", "johndoe@uchicago.edu")

testText1 = "Ethan Reeder drove a bus to Chicago"

testText2 = "Gina Yu couldn't get to the bank until just before it closed, so of course the line was endless and she got stuck behind two women whose loud, stupid conversation put her in a murderous temper. Anders was never in the best of tempers anyway, Anders - a book critic known for the weary, elegant savagery with which he dispatched almost everything he reviewed."

def test_tagidentification():
    taglist = testUser1.chunkTags(testText1)
    assert "Ethan Reeder" in taglist
    assert "Chicago" in taglist
    assert "bus" not in taglist

def test_tagidentification2():
    taglist = testUser1.chunkTags(testText2)
    assert "Gina Yu" in taglist
    assert "Anders" in taglist
    assert "bank" not in taglist
