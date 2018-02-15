from Admit01_Blockchain import *
from datetime import datetime
from datetime import timedelta
import copy

# create a new venue
print('Let\'s make a new venue!')
name = input('Venue name (ex. Apollo Theater): ')
loc = input('Venue location (ex. Chicago, IL): ')
venue1 = Venue(name, loc)

# check if valid venue
if venue1.id is None:
    print('Oh no! You entered invalid parameters for your new venue.')
    print('System exiting...')
    exit()
else:
    print('Great! You\'ve successfully created ' + name + ' in ' + loc + '.')
