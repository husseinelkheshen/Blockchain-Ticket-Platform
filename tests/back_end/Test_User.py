from ../../back_end/Admit01_Blockchain.py import *

user1 = User("Ethan", "Reeder", "er@example.com") # success
user2 = User("Ross", "Piper", "er@example.com") # failure
user3 = User("", "Piper", "rp@example.com") # failure
user4 = User("Ross", "", "rp@example.com") # failure
user5 = User("Ross", "Piper", "") # failure
user6 = User("Ross", "Piper", "invalid.email@format") # failure


def test_validuser:
    assert user1.fname == "Ethan" and
           user1.lname == "Reeder" and
           user1.email_address == "er@example.com"

def test_dupemail:
    assert user2.fname == None and
           user2.lname == None and
           user2.email_address == None

def test_badfname:
    assert user3.fname == None and
           user3.lname == None and
           user3.email_address == None

def test_badlname:
    assert user4.fname == None and
           user4.lname == None and
           user4.email_address == None

def test_noemail:
    assert user5.fname == None and
           user5.lname == None and
           user5.email_address == None

def test_bademail:
    assert user6.fname == None and
           user6.lname == None and
           user6.email_address == None 
