

# ==========================================================
# CALCULATOR COMMAND HANDLER
#
# Purpose:
# Perform mathematical calculations locally without Gemini.
#
# Examples:
#   • calculate 25 + 30
#   • calculate 15 * 6
#   • calculate 100 / 5
#
# Returns:
#   True  -> Command executed
#   None  -> Command not handled
# ==========================================================

from modules.speech import say

CALCULATOR_COMMANDS = [
    "calculate",
    "calculator",
    "bullet"      # Speech recognition kabhi calculate ko bullet sunta hai
]

# ==========================================================
# CALCULATOR COMMAND HANDLER
# ==========================================================

def handle_calculator_commands(command):

    # ------------------------------------------------------
    # CALCULATE COMMAND
    # ------------------------------------------------------
    for keyword in CALCULATOR_COMMANDS:

        if command.startswith("calculate "):

            expression = command.replace("calculate", "", 1).strip()

            try: 

                result = eval(expression)

                print(f"result: {result}")

                say(f"The answer is {result}")

            except Exception:

                say("Sorry Sir, I couldn't calculate this.")
                
            return True