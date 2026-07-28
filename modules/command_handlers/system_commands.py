

from modules.datetime_module import show_time, show_date, get_greeting
from modules.speech import say

from modules.constants import (
    TIME_COMMANDS,
    DATE_COMMANDS,
    GREETING_COMMANDS,
    EXIT_COMMANDS,
    STATUS_COMMANDS,
)



def handle_system_command(command):

    if command in TIME_COMMANDS:
        show_time()
        return True

    elif command in DATE_COMMANDS:
        show_date()
        return True

    elif command in GREETING_COMMANDS:

        greeting = get_greeting()

        say(f"{greeting}, Sir. How may I assist you?")

        return True

    elif command == "your name":
        say("I am Jarvis Mark One, Sir.")
        return True

    elif command in STATUS_COMMANDS:
        say("Functioning perfectly, Sir.")
        return True

    elif command in EXIT_COMMANDS:
        say("Exiting. Goodbye Sir.")
        return False

    return None