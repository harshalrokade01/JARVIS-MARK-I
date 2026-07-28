#isme date and time module import karenge aur call kar sakenge
#MISSION 19: DATE AND TIME IMPORT KAR RHE H
from datetime import datetime

def show_time():
    current_time = datetime.now()
    return current_time.strftime("%H:%M:%S")


def show_date():
    current_time = datetime.now()
    return current_time.strftime("%d:%m:%Y")


def get_greeting():

    current_hour = datetime.now().hour

    if 5 <= current_hour < 12:
        return "Good Morning"

    elif 12 <= current_hour < 17:
        return "Good Afternoon"

    elif 17 <= current_hour < 23:
        return "Good Evening"

    else:
        return "Hello"