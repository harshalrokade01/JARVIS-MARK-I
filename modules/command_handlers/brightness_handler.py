
from modules.speech import say

import screen_brightness_control as sbc

# ==========================================================
# BRIGHTNESS COMMAND HANDLER
#
# Purpose:
# Control screen brightness.
#
# Commands:
#   • increase brightness
#   • decrease brightness
#   • maximum brightness
#   • minimum brightness
#   • set brightness to 50
#
# Returns:
#   True  -> Command executed
#   None  -> Command not handled
# ==========================================================

def handle_brightness_commands(command):

    # ------------------------------------------------------
    # CURRENT BRIGHTNESS
    # ------------------------------------------------------

    if command == "brightness":

        current = sbc.get_brightness()

        print(current)

        say(f"Current brightness is {current} percent, Sir.")

        return True

    
    # ------------------------------------------------------
    # INCREASE BRIGHTNESS
    # ------------------------------------------------------    

    elif command == "increase brightness":

        current = sbc.get_brightness()[0]

        sbc.set_brightness(min(current + 10, 100))

        say("Brightness increased, Sir.")

        return True


    # ------------------------------------------------------
    # DECREASE BRIGHTNESS
    # ------------------------------------------------------  

    elif command == "decrease brightness":

        current = sbc.get_brightness()[0]

        sbc.set_brightness(max(current - 10, 0))

        say("Brightness decreased, Sir.")

        return True

    # ------------------------------------------------------
    # SET BRIGHTNESS
    # ------------------------------------------------------

    elif command.startswith("set brightness to"):

        try:

            level = int(command.replace ("set brightness to", "").strip())

            if 0 <= level <= 100:

                sbc.set_brightness(level)

                say(f"Brightness set to {level} percent, Sir.")

            else:

                say("Please choose a brightness between  0 and 100 percent, Sir.")

            return True


        except ValueError:

            say("Please provide a valid brightness value, Sir.")
    

    return None