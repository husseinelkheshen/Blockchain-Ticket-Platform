from ../../back_end/Admit01_Blockchain.py import *

user1 = User("Ethan", "Reeder", "er@example.com") # success
user2 = User("Ross", "Piper", "er@example.com") # failure
user3 = User("", "Piper", "rp@example.com") # failure
user4 = User("Ross", "", "rp@example.com") # failure
user5 = User("Ross", "Piper", "") # failure
# "invalid.email@format" should also fail; regex validation handled on front end

def test_validuser:
    #
    # User with non-empty names and unique email_address should construct
    #
    assert user1.id != None and
           user1.fname == "Ethan" and
           user1.lname == "Reeder" and
           user1.email_address == "er@example.com"

def test_dupemail:
    #
    # User with non-unique email_address should fail construction
    #
    assert user2.id == None and
           user2.fname == None and
           user2.lname == None and
           user2.email_address == None

def test_badfname:
    #
    # User with empty fname should fail construction
    #
    assert user2.id == None and
           user3.fname == None and
           user3.lname == None and
           user3.email_address == None

def test_badlname:
    #
    # User with empty lname should fail construction
    #
    assert user2.id == None and
           user4.fname == None and
           user4.lname == None and
           user4.email_address == None

def test_noemail:
    #
    # User with empty email_address should fail construction
    #
    assert user2.id == None and
           user5.fname == None and
           user5.lname == None and
           user5.email_address == None
