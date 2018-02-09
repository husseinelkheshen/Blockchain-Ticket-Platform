from ../../back_end/Admit01_Blockchain.py import *

valid_section = "Mezzanine"
valid_row = "B"
valid_seatno = 12

seat1 = Seat(valid_section, valid_row, valid_seatno) # success
seat2 = Seat("", valid_row, valid_seatno) # failure
seat3 = Seat(valid_section, "", valid_seatno) # failure
seat4 = Seat(valid_section, valid_row, -3) # failure

def test_allvalid:
    assert seat1.section == valid_section and
           seat1.row == valid_row and
           seat1.seat_no == valid_seatno

def test_badsection:
    assert seat2.section == None and
           seat2.row == None and
           seat2.seat_no == None

def test_badrow:
    assert seat3.section == None and
           seat3.row == None and
           seat3.seat_no == None

def test_badseatno:
    assert seat4.section == None and
           seat4.row == None and
           seat4.seat_no == None 
