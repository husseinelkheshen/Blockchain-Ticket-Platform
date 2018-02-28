# Install prerequisites
install:
	pip3 install pyqrcode
	pip3 install pypng
	python3 -m pip install pytest

# Run a comprehensive acceptance test
acceptance_test:
	cd blockchain; python3 AcceptanceTest.py

# Run the full test suite
test_suite:
	make unit_tests

# Run all unit tests
unit_tests:
	make iter1_unittests
	make iter2_unittests

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

iter2_unittests:
	# Iteration 2
	python3 -m pytest tests/back_end/Test_Search.py
	python3 -m pytest tests/back_end/Test_CreateEvent.py
	python3 -m pytest tests/back_end/Test_ManageEvent.py

# Delete all pytest cache files
clean:
	find . -name \*.pyc -delete
