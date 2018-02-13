from back_end.Admit01_Blockchain import *

first_id = Trackers.getNextID()
next_id = Trackers.getNextID()

def test_firstid():
    assert first_id == 0

def test_increment():
    assert next_id == first_id + 1
