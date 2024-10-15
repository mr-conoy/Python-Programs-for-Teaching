from tkinter import Tk, Canvas
from datetime import date, datetime

def get_events():
    list_events = []
    with open('countdown_calendar/events.txt') as file:
        for line in file:
            line = line.rstrip('\n')
            current_event = line.split(',')
            event_date = datetime.strptime(current_event[1], '%d/%m/%y').date()
            current_event[1] = event_date
            list_events.append(current_event)
    return list_events

def days_between_dates(date1, date2):
    time_between = date1 - date2
    return time_between.days  # Access the days directly

root = Tk()
c = Canvas(root, width=800, height=800, bg='black')
c.pack()  # Pack the canvas to make it visible
c.create_text(100, 50, anchor='w', fill='orange', font='Arial 28 bold', text='My Countdown Calendar')

events = get_events()
today = date.today()

vertical_space = 100

for event in events:
    event_name = event[0]
    days_until = days_between_dates(event[1], today)
    display = 'Days until ' + event_name + ': ' + str(days_until)
    c.create_text(100, vertical_space, anchor='w', fill='lightblue', font='Arial 28 bold', text=display)
    vertical_space += 30

root.mainloop()  # Start the Tkinter event loop
