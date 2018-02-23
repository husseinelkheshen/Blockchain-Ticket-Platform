from blockchain.Admit01_Blockchain import *
from datetime import timedelta

valid_datetime = date.datetime.now() + timedelta(days = 7) # one week from now
valid_date_new = date.datetime.now() + timedelta(days = 3) # 3 days from now
invalid_datetime = date.datetime.now() - timedelta(days = 7) # one week ago

venue1 = Venue("Wrigley Field", "Chicago, IL")
event1 = Event("Lady Gaga", valid_datetime, "Stadium world tour")
event1.venue = venue1

def test_valid_paramters():
    """ Tests a ManageEvent call where all parameters are valid to ensure success. """

    assert (venue1.manageEvent(event1, "Happy Time", valid_date_new, "Don't worry.") is True and
            event1.name == "Happy Time" and
            event1.datetime == valid_date_new and
            event1.desc == "Don't worry.")

def test_no_name():
    """ Tests a ManageEvent call where no name is given, to ensure failure. """
    assert (venue1.manageEvent(event1, None, valid_datetime, "Start worrying.") is False and
            event1.name == "Happy Time" and
            event1.datetime == valid_date_new and
            event1.desc == "Don't worry.")

def test_no_date():
    """ Tests a ManageEvent call where no date is given, to ensure failure. """
    assert (venue1.manageEvent(event1, "I'm not cramming!", None, "Start worrying.") is False and
            event1.name == "Happy Time" and
            event1.datetime == valid_date_new and
            event1.desc == "Don't worry.")

def test_old_date():
    """ Tests a ManageEvent call where a date in the past is given, to ensure failure. """
    assert (venue1.manageEvent(event1, "I'm not cramming!", invalid_datetime, "Start worrying.") is False and
            event1.name == "Happy Time" and
            event1.datetime == valid_date_new and
            event1.desc == "Don't worry.")

def test_no_description():
    """ Tests a ManageEvent call where the description is removed, to ensure success. """
    assert (venue1.manageEvent(event1, "I'm not cramming!", valid_datetime, None) and
            event1.name == "I'm not cramming!" and
            event1.datetime == valid_datetime and
            event1.desc is None)