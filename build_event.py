from icalendar import Calendar, Event, Alarm
import pytz
from datetime import datetime, timedelta

def build_event_duration(summary, description, start, duration, location,
        freq_of_recurrence, until):

    '''
    Return an event that can be added to a calendar

    summary: summary of the event
    description: description of the event
    location: self explanatory
    start, end, stamp: These are datetime.datetime objects
    freq_of_recurrence: frequency of recurrence, string which can take the
    values daily, weekly, monthly, etc.
    until: A datetime.datetime object which signifies when the recurrence will
    end
    '''

    event = Event()
    event.add('summary', summary)
    event.add('description', description)
    event.add('dtstart', start)
    event.add('duration', timedelta(hours=duration))
    event.add('dtstamp', datetime.now())
    event.add('location', location)
    event.add('rrule', { 'FREQ': freq_of_recurrence, 'UNTIL': until})
    for i in range(3):
        alarm = Alarm()
        alarm.add("ACTION", "DISPLAY")
        if i == 0:
            alarm.add("TRIGGER", "-P0DT3H0M0S", encode=0)
        elif i == 1:
            alarm.add("TRIGGER", "-P0DT1H0M0S", encode=0)
        elif i == 2:
            alarm.add("TRIGGER", "-P0DT0H20M0S", encode=0)
        alarm.add("DESCRIPTION", "Your Class Reminder")
        event.add_component(alarm)

    return event

def generateIndiaTime(year, month, date, hour, minutes):

    return datetime(year, month, date, hour, minutes, tzinfo=pytz.timezone('Asia/Kolkata'))

if __name__ == '__main__':
    cal = Calendar()
    cal.add('prodid', '-//Your Timetable generated by GYFT//mxm.dk//')
    cal.add('version', '1.0')

    example_event = build_event(
        "example event", 
        "example event's description 2!",
        generateIndiaTime(2016, 8, 22, 19, 0), 
        generateIndiaTime(2016, 8, 22, 20, 0), 
        "imaginary location!",
        "weekly",
        generateIndiaTime(2016, 11, 20, 12, 0))

    cal.add_component(example_event)

    with open('timetable.ics', 'wb') as f:
            f.write(cal.to_ical())
