

#importing 
from modules.screenshot import take_screenshot
from modules.speech import say



# ==========================================================
#             SCREENSHOT COMMAND HANDLER
#
# Purpose:
# Handles screenshot related commands.
#
# Handles:
#   • take screenshot
#   • screenshot
#
# Returns:
#   True  -> Command executed
#   None  -> Command not handled
# ==========================================================

def handle_screenshot_commands(command):

    # ------------------------------------------------------
    # SCREENSHOT COMMAND
    # ------------------------------------------------------

    if command in [
        "take screenshot",
        "screenshot"
    ]:

        filename = take_screenshot()

        print(f"Screenshot Saved as: {filename}")

        say("Screenshot captured and Saved Successfully, Sir.")

        return True

    #command not handled by screenshot handler
    return None