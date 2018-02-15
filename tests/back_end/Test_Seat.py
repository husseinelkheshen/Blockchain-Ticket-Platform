from blockchain.Admit01_Blockchain import *

valid_section = "Mezzanine"
valid_row = "B"
valid_seatno = 12

seat1 = Seat(valid_section, valid_row, valid_seatno) # success
seat2 = Seat("", valid_row, valid_seatno) # failure
seat3 = Seat(valid_section, "", valid_seatno) # failure
seat4 = Seat(valid_section, valid_row, -3) # failure

def test_allvalid():
    #
    # A Seat with valid section, row, and seat_no should construct successfully
    #
    assert (seat1.section == valid_section and
            seat1.row == valid_row and
            seat1.seat_no == valid_seatno)

def test_badsection():
    #
    # A Seat constructor with an invalid section should contruct a null Seat
    #
    assert (seat2.section == None and
            seat2.row == None and
            seat2.seat_no == None)

def test_badrow():
    #
    # A Seat constructor with an invalid row should contruct a null Seat
    #
    assert (seat3.section == None and
            seat3.row == None and
            seat3.seat_no == None)

def test_badseatno():
    #
    # A Seat constructor with an invalid seat_no should contruct a null Seat
    #
    assert (seat4.section == None and
            seat4.row == None and
            seat4.seat_no == None)
