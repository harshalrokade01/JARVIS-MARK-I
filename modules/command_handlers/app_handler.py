# importing
from modules.apps import open_notepad, open_chrome
from modules.speech import say


# ==========================================================
#                 APP COMMAND HANDLER
#
# Purpose:
# Handles local Windows applications.
#
# Handles:
#   • Notepad
#   • Chrome
#
# Returns:
#   True  -> Command executed
#   None  -> Command not handled
# ==========================================================

def handle_app_commands(command):

    # ------------------------------------------------------
    # NOTEPAD COMMAND
    # ------------------------------------------------------

    if command == "notepad":

        say("Opening Notepad Sir")

        open_notepad()

        return True


    # ------------------------------------------------------
    # CHROME COMMAND
    # ------------------------------------------------------

    elif command == "chrome":

        say("Opening Chrome Sir")

        open_chrome()

        return True


    # Command not handled by App Handler
    return None