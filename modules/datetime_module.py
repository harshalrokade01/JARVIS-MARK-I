#isme date and time module import karenge aur call kar sakenge
#MISSION 19: DATE AND TIME IMPORT KAR RHE H
import datetime


def show_time():
    current_time = datetime.datetime.now()
    return current_time.strftime("%H:%M:%S")



def show_date():
    current_time = datetime.datetime.now()
    return current_time.strftime(("%d:%m:%Y"))