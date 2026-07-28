

# importing
from modules.apps import open_app
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

    if open_app(command):

        say(f"Opening {command} Sir")

        return True

    if command.startswith("open"):

        app_name = command.replace("open ", "").strip()

        if open_app(app_name):

            say(f"Opening {app_name} Sir")

            return True

        else:

            say(f"Sorry Sir, I couldn't find {app_name}")

            return True

    return None