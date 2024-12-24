"""
Author: Michael Lizzio
Date: 9/9/2024
File: calendar_super.py
"""

# imports
from secret import MY_EMAIL
from secret import CLIENT_PATH as CREDENTIALS_PATH
from gcsa.google_calendar import GoogleCalendar


# Main function
def main():
    gc = GoogleCalendar(MY_EMAIL, credentials_path=CREDENTIALS_PATH)
    for event in gc:
        print(event)
    sub_calendars = {}
    for calendar in gc.get_calendar_list():
        print(calendar, calendar.id, calendar.description)
        name = (str(calendar.__str__()))
        name = name[name.index("-") + 3:-1]
        sub_calendars[name] = {"calendar_actions": calendar, "calendar_access": GoogleCalendar(default_calendar=calendar.id, credentials_path=CREDENTIALS_PATH)}
    for calendar, calendar_info in sub_calendars.items():
        print(f"{calendar}: {calendar_info['calendar_actions'].description}")
        for event in calendar_info["calendar_access"]:
            print(event)
        print()


# Call the main function
if __name__ == "__main__":
    main()
