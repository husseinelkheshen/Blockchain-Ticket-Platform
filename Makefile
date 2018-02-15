# Install prerequisites
install:
	pip3 install pyqrcode
	python3 -m pip install pytest

# Run back end unit tests
back_end_unit_tests:
	# python3 -m pytest tests/back_end/Test_Chains_And_Mining.py
	# python3 -m pytest tests/back_end/Test_CreateTicket.py
	# python3 -m pytest tests/back_end/Test_Event.py
	# python3 -m pytest tests/back_end/Test_Seat.py
	python3 -m pytest tests/back_end/Test_Trackers.py
	# python3 -m pytest tests/back_end/Test_User.py
	# python3 -m pytest tests/back_end/Test_Venue.py

# Delete all pytest cache files
clean:
	find . -name \*.pyc -delete
