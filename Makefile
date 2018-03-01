# Install prerequisites
install:
	pip3 install pyqrcode
	pip3 install pypng
	pip3 install nltk
	pip3 install numpy
	python3 -m pip install pytest
	python3 downloads/downloads.py

# Run a comprehensive acceptance test
acceptance_test:
	cd blockchain; python3 AcceptanceTest.py

# Run the full test suite
test_suite:
	make unit_tests

# Run the full test suite (w/ logging)
test_suite_log:
	make unit_tests_log

# Run all unit tests
unit_tests:
	make iter1_unittests
	make iter2_unittests

# Run all unit tests (w/ logging)
unit_tests_log:
	make iter1_unittests_log
	make iter2_unittests_log

iter1_unittests:
	# Iteration 1
	python3 -m pytest tests/back_end/Test_Chains_And_Mining.py
	python3 -m pytest tests/back_end/Test_CreateTicket.py
	python3 -m pytest tests/back_end/Test_Event.py
	python3 -m pytest tests/back_end/Test_Seat.py
	python3 -m pytest tests/back_end/Test_Trackers.py
	python3 -m pytest tests/back_end/Test_User.py
	python3 -m pytest tests/back_end/Test_Venue.py
	python3 -m pytest tests/back_end/Test_GetOwnedTickets.py
	python3 -m pytest tests/back_end/Test_Transaction.py
	python3 -m pytest tests/back_end/Test_BlockChain.py
	python3 -m pytest tests/back_end/Test_Ticket.py
	python3 -m pytest tests/back_end/Test_BuyTicket.py
	python3 -m pytest tests/back_end/Test_UpgradeTicket.py
	python3 -m pytest tests/back_end/Test_ListTicket.py
	make clean

iter1_unittests_log:
	# Iteration 1 (w/ logging)
	python3 -m pytest tests/back_end/Test_Chains_And_Mining.py > tests/back_end/pytest_logs/Test_Chains_And_Mining.log
	python3 -m pytest tests/back_end/Test_CreateTicket.py > tests/back_end/pytest_logs/Test_CreateTicket.log
	python3 -m pytest tests/back_end/Test_Event.py > tests/back_end/pytest_logs/Test_Event.log
	python3 -m pytest tests/back_end/Test_Seat.py > tests/back_end/pytest_logs/Test_Seat.log
	python3 -m pytest tests/back_end/Test_Trackers.py > tests/back_end/pytest_logs/Test_Trackers.log
	python3 -m pytest tests/back_end/Test_User.py > tests/back_end/pytest_logs/Test_User.log
	python3 -m pytest tests/back_end/Test_Venue.py > tests/back_end/pytest_logs/Test_Venue.log
	python3 -m pytest tests/back_end/Test_GetOwnedTickets.py > tests/back_end/pytest_logs/Test_GetOwnedTickets.log
	python3 -m pytest tests/back_end/Test_Transaction.py > tests/back_end/pytest_logs/Test_Transaction.log
	python3 -m pytest tests/back_end/Test_BlockChain.py > tests/back_end/pytest_logs/Test_BlockChain.log
	python3 -m pytest tests/back_end/Test_Ticket.py > tests/back_end/pytest_logs/Test_Ticket.log
	python3 -m pytest tests/back_end/Test_BuyTicket.py > tests/back_end/pytest_logs/Test_BuyTicket.log
	python3 -m pytest tests/back_end/Test_UpgradeTicket.py > tests/back_end/pytest_logs/Test_UpgradeTicket.log
	python3 -m pytest tests/back_end/Test_ListTicket.py > tests/back_end/pytest_logs/Test_ListTicket.log
	make clean

iter2_unittests:
	# Iteration 2
	python3 -m pytest tests/back_end/Test_Search.py
	python3 -m pytest tests/back_end/Test_CreateEvent.py
	python3 -m pytest tests/back_end/Test_ManageEvent.py
	python3 -m pytest tests/back_end/Test_UpdatePreferences.py
	python3 -m pytest tests/back_end/Test_Explore.py
	python3 -m pytest tests/back_end/Test_VenueTickets.py
	python3 -m pytest tests/back_end/Test_ManageTickets.py
	python3 -m pytest tests/back_end/Test_ValidateTicketCode.py
	make clean

iter2_unittests_log:
	# Iteration 2 (w/ logging)
	python3 -m pytest tests/back_end/Test_Search.py > tests/back_end/pytest_logs/Test_Search.log
	python3 -m pytest tests/back_end/Test_CreateEvent.py > tests/back_end/pytest_logs/Test_CreateEvent.log
	python3 -m pytest tests/back_end/Test_ManageEvent.py > tests/back_end/pytest_logs/Test_ManageEvent.log
	python3 -m pytest tests/back_end/Test_UpdatePreferences.py > tests/back_end/pytest_logs/Test_UpdatePreferences.log
	python3 -m pytest tests/back_end/Test_Explore.py > tests/back_end/pytest_logs/Test_Explore.log
	python3 -m pytest tests/back_end/Test_VenueTickets.py > tests/back_end/pytest_logs/Test_VenueTickets.log
	python3 -m pytest tests/back_end/Test_ManageTickets.py > tests/back_end/pytest_logs/Test_ManageTickets.log
	python3 -m pytest tests/back_end/Test_ValidateTicketCode.py > tests/back_end/pytest_logs/Test_ValidateTicketCode.log
	make clean

# Delete all pytest cache files
clean:
	find . -name \*.pyc -delete

# Delete all pytest log files
clean_log:
	find . -name \*.log -delete
