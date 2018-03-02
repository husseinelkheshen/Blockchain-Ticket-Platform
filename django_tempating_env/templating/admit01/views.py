from django.http import HttpResponse
from django.template import loader

def index(request):
	logged_in = False
	template  = loader.get_template('admit01/index.html')
	context = {
		'logged_in': logged_in,
	}
	return HttpResponse(template.render(context, request))

def event(request):
	logged_in_event = False
	template  = loader.get_template('admit01/event_home.html')
	context = {
		'logged_in': logged_in_event,
	}
	return HttpResponse(template.render(context, request))

def login_register(request):
	logged_in = False
	template  = loader.get_template('admit01/login_register.html')
	context = {
		'logged_in': logged_in,
	}
	return HttpResponse(template.render(context, request))

def event_login_register(request):
	logged_in_event = False
	template  = loader.get_template('admit01/event_login_register.html')
	context = {
		'logged_in': logged_in_event,
	}
	return HttpResponse(template.render(context, request))

def detail_event(request):
	logged_in = False
	ticket1 = {
		'price' : 199,
		'section' :'Upper Deck',
		'row' : 'AAAAA',
		'seat' : 25,
		'can_upgrade' : True
	}
	ticket2 = {
		'price' : 1,
		'section' : 'General Admission',
		'row' : 'GA',
		'seat' : 1000,
		'can_upgrade' : False,
	}
	detail_event = {
		'event_name' : 'Idk what the kids like',
		'event_released': True, 
		'venue' : 'Soldier Field',
		'when' : '5/22/2018 at 9:30pm',
		'tickets' : [ticket1, ticket2],
	}

	template  = loader.get_template('admit01/detail_event.html')
	context = {
		'logged_in': logged_in,
		'detail_event' : detail_event,
	}
	return HttpResponse(template.render(context, request))

def purchase(request):
	logged_in= False
	template  = loader.get_template('admit01/purchase.html')
	ticket1 = {
		'price' : 199,
		'section' :'Upper Deck',
		'row' : 'AAAAA',
		'seat' : 25,
		'can_upgrade' : True
	}
	ticket2 = {
		'price' : 1,
		'section' : 'General Admission',
		'row' : 'GA',
		'seat' : 1000,
		'can_upgrade' : False,
	}
	wallet_info = {
		'money_in_wallet': 100.15
	}
	ticket_wanted = {
		'price' : 25,
		'section' : 'General Admission',
		'row' : 'GA',
		'seat' : 1000,
		'can_upgrade' : False,
	}
	detail_event = {
		'event_name' : 'Idk what the kids like',
		'event_released': True, 
		'venue' : 'Soldier Field',
		'when' : '5/22/2018 at 9:30pm',
		'tickets' : [ticket1, ticket2],
	}
	context = {
		'logged_in': logged_in,
		'already_purchased' : [ticket1, ticket2], 
		'ticket_wanted': ticket_wanted,
		"detail_event": detail_event,
		"wallet_info": wallet_info
	}
	return HttpResponse(template.render(context, request))


### NOTE SEARCH AND EXPLORE HAVE THE SAME INTERFACE, SHOULD BE MERGED INTO ONE VIEW WITH MODIFIED
### REQUEST PARAMETER
def search(request):
	detail_event1 = {
		'event_name' : 'Idk what the kids like',
		'event_released': True, 
		'venue' : 'Soldier Field',
		'when' : '5/22/2018 at 9:30pm',
		'tickets' : [],
	}
	detail_event2 = {
		'event_name' : 'Elmo',
		'event_released': True, 
		'venue' : 'Soldier Field',
		'when' : '5/22/2018 at 9:30pm',
		'tickets' : [],
	}
	detail_event3 = {
		'event_name' : 'Rachel Ray LIve',
		'event_released': True, 
		'venue' : 'Soldier Field',
		'when' : '5/22/2018 at 9:30pm',
		'tickets' : [],
	}

	logged_in = False

	context = {
		'logged_in' : logged_in,
		'isexplore' : False,
		'search_results' : [detail_event1, detail_event2, detail_event3]
	}
	template  = loader.get_template('admit01/list_event.html');
	return HttpResponse(template.render(context, request))


def explore(request):
	detail_event1 = {
		'event_name' : 'Idk what the kids like',
		'event_released': True, 
		'venue' : 'Soldier Field',
		'when' : '5/22/2018 at 9:30pm',
		'tickets' : [],
	}
	detail_event2 = {
		'event_name' : 'Elmo',
		'event_released': True, 
		'venue' : 'Soldier Field',
		'when' : '5/22/2018 at 9:30pm',
		'tickets' : [],
	}
	detail_event3 = {
		'event_name' : 'Rachel Ray LIve',
		'event_released': True, 
		'venue' : 'Soldier Field',
		'when' : '5/22/2018 at 9:30pm',
		'tickets' : [],
	}

	logged_in = False

	context = {
		'logged_in' : logged_in,
		'isexplore' : True,
		'search_results' : [detail_event1, detail_event2, detail_event3]
	}
	template  = loader.get_template('admit01/list_event.html');
	return HttpResponse(template.render(context, request))

def base(request):
	logged_in = False
	template  = loader.get_template('admit01/base.html')
	context = {
		'logged_in': logged_in,
	}
	return HttpResponse(template.render(context, request))

def event_base(request):
	logged_in_event = False
	template  = loader.get_template('admit01/event_base.html')
	context = {
		'logged_in': logged_in_event,
	}
	return HttpResponse(template.render(context, request))