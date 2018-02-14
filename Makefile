install:
	pip3 install pyqrcode

# Run back end unit tests by calling 'make back_end_unit_tests'
back_end_unit_tests:
	python3 -m pytest tests/back_end/Test_Event.py
	python3 -m pytest tests/back_end/Test_Seat.py
	python3 -m pytest tests/back_end/Test_Trackers.py
	python3 -m pytest tests/back_end/Test_User.py
	python3 -m pytest tests/back_end/Test_Venue.py
