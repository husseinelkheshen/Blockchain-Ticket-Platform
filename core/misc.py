from datetime import datetime

def venue_location_to_string(venue_city, venue_state):
    venue_loc_str = venue_city.strip() + ', ' + venue_state.strip()
    return venue_loc_str

def parse_event_time(event_time):
    if event_time is None:
        return None
    year=event_time.get('year')
    month=event_time.get('month')
    day=event_time.get('day')
    hour=event_time.get('hour')
    minute=event_time.get('minute')
    if year is None or month is None or day is None or hour is None or minute is None:
        return None
    dt = datetime(
        year=int(year),
        month=int(month),
        day=int(day),
        hour=int(hour),
        minute=int(minute))
    return dt

def parse_events(events):
    ret = []
    for e in events:
        dt = e.datetime
        e_dict = {'event_id': e.id, 'name': e.name, 'desc': e.desc,
            'num_scheduled_tickets': len(e.scheduled)}
        e_dict['time'] = {
            "minute": dt.minute,
            "hour": dt.hour,
            "day": dt.day,
            "month": dt.month,
            "year": dt.year
        }
        ret.append(e_dict)
    return ret