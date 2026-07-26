

from modules.datetime_module import show_time, show_date
from modules.speech import say


def handle_system_command(command):

    if command in [
        "time",
        "what is the time",
        "tell me the time",
        "current time",
        "time please"
    ]:
        show_time()
        return True

    elif command in [
        "date",
        "what is the date",
        "tell me the date",
        "today's date",
        "current date",
        "date please"
    ]:
        show_date()
        return True

    elif command in [
        "hi jarvis",
        "hello jarvis",
        "hey jarvis",
        "what is jarvis"
    ]:
        say("Hello Sir.")
        return True

    elif command == "your name":
        say("I am Jarvis Mark One, Sir.")
        return True

    elif command == "how are you":
        say("Functioning Perfectly, Sir.")
        return True

    elif command == "exit jarvis":
        say("Exiting, GoodBye Sir.")
        return False

    return None