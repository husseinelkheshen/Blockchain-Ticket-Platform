# Install prerequisites
install:
	pip3 install pyqrcode
	python3 -m pip install pytest

# Run a comprehensive acceptance test
acceptance_test:
	cd blockchain; python3 AcceptanceTest.py

# Run the full test suite
test_suite:
	make unit_tests

# Run all unit tests
unit_tests:
	make back_end_unit_tests

# Run back end unit tests
back_end_unit_tests:
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

	make clean

# Delete all pytest cache files
clean:
	find . -name \*.pyc -delete
