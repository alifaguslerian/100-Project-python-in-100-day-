#Event Countdown Timer
from datetime import datetime, timedelta
import time

# Function to get the date and time of the event
def get_event_datetime():
    try:
        date_input = input("Enter the date and time of the event (YYYY-MM-DD HH:MM): ")
        return datetime.strptime(date_input, "%Y-%m-%d %H:%M")
    except ValueError:
        print("Invalid date or time format. Please try again.")
        return None
    
#Calculating time remaining
def calculate_time_remaining(event_date):
    current_datetime = datetime.now()
    time_difference = event_date - current_datetime
    return time_difference

# Display the countdown timer
def display_countdown(time_left):
    days = time_left.days
    hours, remainder = divmod(time_left.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    print(f"\nTime remaining: {days} days, {hours} hours, {minutes} minutes, {seconds} seconds", end="")

# Main Countdown Timer
def start_countdown(event_date):
    while True:
        time_left = calculate_time_remaining(event_date)
        if time_left.total_seconds() <= 0:
            print("\nEvent has started!")
            break
        display_countdown(time_left)
        time.sleep(1)

# Main program
event_datetime = get_event_datetime()

if event_datetime:
    print(f"\nEvent date and time: {event_datetime}")
    start_countdown(event_datetime)


