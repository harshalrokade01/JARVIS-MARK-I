

import psutil

from modules.speech import say

# ==========================================================
# BATTERY COMMAND HANDLER
#
# Purpose:
# Handle battery related commands.
#
# Commands:
#   • battery
#   • battery status
#   • battery percentage
#   • is my laptop charging
#
# Returns:
#   True  -> Command executed
#   None  -> Command not handled
# ==========================================================

def handle_battery_commands(command):

     # ------------------------------------------------------
    # BATTERY STATUS
    # ------------------------------------------------------

    if command in ["battery","battery status","battery percentage"]:

        battery = psutil.sensors_battery()

        percent = battery.percent

        charging = battery.power_plugged

        if charging:

            say(f"Battery is {percent} percent and currently charging, Sir. ")

        else:

            say(f"Battery is {percent} percent and running on battery power, Sir. ")
            

        return True

    return None