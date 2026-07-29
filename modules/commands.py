#so hum jo bhi commands de rhe the jarvis ko wo ab yaha shift kar denge taaki difficulty na ho aur scalability badh jaye

# ---------------- COMMAND LISTS ---------------- #

TIME_COMMANDS = [
    "time",
    "what is the time",
    "tell me the time",
    "current time",
    "time please"
]

DATE_COMMANDS = [
    "date",
    "what is the date",
    "tell me the date",
    "today's date",
    "current date",
    "date please"
]




#------------------IMPORTING FROM ALL OVER THE FILES IN JARVIS--------------------


#new import for system commands from system_commands.py
from modules.command_handlers.system_commands import handle_system_command

#importing 
from modules.apps import open_notepad, open_chrome, open_app

from modules.browser import open_website, search_google, play_youtube, find_amazon

from modules.datetime_module import show_time, show_date

from youtubesearchpython import VideosSearch

#MISSION 22 IMPORTING SCREENSHOT FROM SCREENSHOT.PY
from modules.screenshot import take_screenshot

#mission 24 Importing notes from notes.py
from modules.notes import save_note 

from modules.debug import show_hud

#importing speech module taaaki jarvis bol sake
from modules.speech import say

#importing weather function
from modules.weather import get_weather

#gemini ai use ho sake jarvis me
from modules.ai import ask_gemini

import time

from modules.command_handlers.app_handler import handle_app_commands

from modules.command_handlers.screenshot_handler import handle_screenshot_commands

from modules.command_handlers.file_handler import handle_file_commands







#importing commands for play,pause, volume up and down
from modules.media import(
    pause_media,
    next_media,
    previous_media,
    volume_up,
    volume_down,
    mute_volume
)
#-------------------------------------------------------------------------------------------------------



#ek function banayenge taki ye "query  = " ".join(words[1:])" baar baar call ho sake aur har function me baar baar likhna naa pade
def get_query(words):

    return " ".join(words[1:])


# ==========================================================
# AI COMMAND DETECTION
#
# Note:
# This function is temporary.
# Future versions will automatically send all
# unhandled commands to Gemini AI.
# ==========================================================
def is_ai_command(command):
    ai_keywords = [
        "who",
        "what",
        "when",
        "where",
        "why",
        "how",
        "which",
        "whose",
        "explain",
        "define",
        "meaning",
        "difference",
        "compare",
        "tell",
        "describe",
        "summarize",
        "latest",
        "news",
        "price",
        "bitcoin",
        "crypto",
        "stock",
        "share",
        "ipl",
        "match",
        "score",
        "ai",
        "openai",
        "true",
        "false",
        "give",
        "question",
        "answer",
        "solve",
        "statement",
    ]

    return any(word in command for word in ai_keywords)

#what this function gonna do
#Ye kya karega?
#latest ai news        ✅ AI
#who is elon musk      ✅ AI
#bitcoin price         ✅ AI
#weather pune          ❌ Local
#play believer         ❌ Local
#open chrome           ❌ Local



#this is SINGLE RESPONSIBILITY PRINCIPLE (SRP)
def handle_system_commands(command):


    # ---------------- GREETING COMMANDS ---------------- #
    if command in ["hi jarvis", "hello jarvis", "hey jarvis"]:

        say("Hello Sir!")
        return True

    
    # ---------------- EXIT COMMAND ---------------- #
    elif command in ["turn off jarvis", "exit jarvis", "switch off jarvis", "shutdown jarvis"]:

        say("Jarvis Shutting Off, Goodbye Sir!")
        return False


    # ---------------- TIME COMMAND ---------------- #
    elif command in TIME_COMMANDS:

        current_time = show_time()

        show_hud(
            command="time",
            command_type="LOCAL",
            status="SUCCESS",
            extra=f"Current Time : {current_time}"
        )

        say(f"Sir, Current Time is {current_time}")

        return True



    # ---------------- DATE COMMAND ---------------- #
    elif command in DATE_COMMANDS:

        current_date = show_date()

        show_hud(
            command="date",
            command_type="LOCAL",
            status="SUCCESS",
            extra=f"Current Date : {current_date}"
        )

        say(f"Sir, Today's date is {current_date}")

        return True


    # ---------------- IDENTITY COMMAND ---------------- #
    elif command == "your name":

        print("I'm Jarvis")

        say("I'm Jarvis")

        return True

    
    # ---------------- STATUS COMMAND ---------------- #
    elif command == "how r u":

        print("I'm Fine Sir.")

        say("I'm doing well Sir. How can I help you?")

        return True


    # Command not handled here
    return None


# ==========================================================
#                 BROWSER COMMAND HANDLER
#
# Purpose:
# Handles all browser-related commands such as:
#   • Open Website
#   • Google Search
#   • Play YouTube Videos
#   • Search Products on Amazon
#
# Returns:
#   True  -> Command executed successfully
#   None  -> Command not handled
# ==========================================================
def handle_browser_commands(words, command):

    #empty command safety check
    if not words:
        return None

    # ------------------------------------------------------
    #                   OPEN COMMAND
    #       Example:
    #                   open google
    #                   open github
    # ------------------------------------------------------

    if open_website(command):

        say(f"Opening {command} Sir")

        return True

    if words[0] == "open":

        if len(words) > 1:

            query = get_query(words)

            if open_app(query):

                say(f"Opening {query} Sir")

            else:

                say(f"Opening {query} Sir")

                open_website(query)

            return True

        else:

            say("Please tell me what to open, Sir")

            return True


    # ------------------------------------------------------
    #                      SEARCH COMMAND
    # Example:
    #                   search python tutorials
    # ------------------------------------------------------


    elif words[0] == "search":

        if len(words) > 1:

            query = get_query(words)

            say(f"Searching {query} on Google, Sir")

            search_google(query)

        else:
            say("Please tell me what to search, Sir")

        return True

    # ------------------------------------------------------
    #                   PLAY COMMAND
    # Example:
    #                   play believer
    # ------------------------------------------------------

    elif words[0] == "play":

        if len(words) > 1:

            query = get_query(words)

            say(f"Playing {query} on Youtube, Sir")

            play_youtube(query)

        else:
            say("Please tell me which song to play, Sir")

        return True

    # ------------------------------------------------------
    #                  BUY COMMAND
    # Example:
    #                   buy keyboard
    # ------------------------------------------------------

    elif words[0] == "buy":

        if len(words) > 1:

            query = get_query(words)

            say(f"Searching Amazon for {query}, Sir")

            find_amazon(query)

        else:
            say("Please tell me what product to find, Sir")

        return True

    #command not handled
    return None


# ==========================================================
#                 WEATHER COMMAND HANDLER
#
# Purpose:
# Handles all weather-related commands.
#
# Returns:
#   True  -> Weather command executed
#   None  -> Command not handled
# ==========================================================

def handle_weather_commands(words, command):

    if not words:   
        return None

    # ------------------------------------------------------
    # WEATHER COMMAND
    # Example:
    # weather pune
    # weather mumbai
    # ------------------------------------------------------    

    if words[0] =="weather":

        if len(words) > 1:

            city = get_query(words)

            #measure API response time
            start_time = time.perf_counter()

            result = get_weather(city)

            end_time = time.perf_counter()

            response_time = end_time - start_time

            if result is None:

                say("Sorry Sir, I couldn't find that city, Sir")

            else:

                city_name, temp, humidity, weather = result

                show_hud(
                    command=command,
                    command_type="LOCAL",
                    status="SUCCESS",
                    response_time=response_time,
                    extra=(
                        f"City         : {city_name}\n"
                        f"Temperature  : {temp:.1f}°C\n"
                        f"Humidity     : {humidity}%\n"
                        f"Weather      : {weather}"
                    )
                )

                say(
                    f"Sir, in {city_name}, the temperature is "
                    f"{temp:.1f} degree Celsius with {weather}"

                )
        else:

            say("Please tell me the city name, Sir.")

        return True

    #COMMAND NOT HANDLED
    return None


# ==========================================================
#                 MEDIA COMMAND HANDLER
#
# Purpose:
# Handles media playback and volume control commands.
#
# Handles:
#   • Pause
#   • Resume
#   • Next
#   • Previous
#   • Volume Up
#   • Volume Down
#   • Mute
#
# Returns:
#   True  -> Media command executed
#   None  -> Command not handled
# ==========================================================

def handle_media_commands(command):

    # ------------------------------------------------------
    #                      PAUSE COMMAND
    # Example:
    # pause
    # pause music
    # stop music
    # ------------------------------------------------------

    if command in [
        "pause",
        "pause music",
        "top music",
        "top song",
        "stop music",
        "stop song"
    ]:

        print("DEBUG: Pause command executed")

        pause_media()
        return True

    # ------------------------------------------------------
    # RESUME COMMAND
    # ------------------------------------------------------

    elif command in [
        "resume",
        "continue",
        "play music",
        "continue music"
    ]:

        pause_media()
        return True


    # ------------------------------------------------------
    # NEXT COMMAND
    # ------------------------------------------------------

    elif command in [
        "next",
        "next song",
        "skip"
    ]:

        next_media()
        return True


    # ------------------------------------------------------
    # PREVIOUS COMMAND
    # ------------------------------------------------------

    elif command in [
        "previous",
        "previous song",
        "back"
    ]:

        previous_media()
        return True


    # ------------------------------------------------------
    # VOLUME UP COMMAND
    # ------------------------------------------------------

    elif command in [
        "volume up",
        "volume",
        "volume of",
        "increase volume",
        "louder"
    ]:

        volume_up()
        return True


    # ------------------------------------------------------
    # VOLUME DOWN COMMAND
    # ------------------------------------------------------

    elif command in [
        "volume down",
        "decrease volume",
        "lower volume",
        "softer"
    ]:

        volume_down()
        return True


    # ------------------------------------------------------
    # MUTE COMMAND
    # ------------------------------------------------------

    elif command in [
        "mute",
        "mute volume",
        "silent"
    ]:

        mute_volume()
        return True

    #Command not handled by Media Handler
    return None


# ==========================================================
#                 NOTES COMMAND HANDLER
#
# Purpose:
# Handles note saving commands.
#
# Example:
#   note buy milk
#   note meeting at 5 pm
#
# Returns:
#   True  -> Note command executed
#   None  -> Command not handled
# ==========================================================

def handle_notes_commands(words):

    if not words:
        return None

    # ------------------------------------------------------
    #                  Note COMMAND
    # Example:
    # note buy milk
    # ------------------------------------------------------

    if words[0] == "note":

        if len(words) > 1:

            #extract everything after "note"
            note = get_query(words)

            #save note to file
            filepath = save_note(note)

            print(f"Note Saved in {filepath}")

            say("Your Note has been Saved Successfully, Sir.")

        else: 
            say("Please tell me what to save, Sir.")

        return True
    
    # Command not handled by Notes Handler
    return None


# ==========================================================
#                 SYSTEM COMMAND HANDLER
#
# Purpose:
# Handles all basic Jarvis system commands.
#
# Handles:
#   • Greetings
#   • Time
#   • Date
#   • Exit
#   • Identity
#   • Status
#
# Returns:
#   True  -> Command executed
#   False -> Exit Jarvis
#   None  -> Command not handled
# ==========================================================

def handle_system_commands(command):

    # ---------------- GREETING COMMANDS ---------------- #

    if command in [
        "hi jarvis",
        "hii jarvis",
        "hello jarvis",
        "hey jarvis"
    ]:

        say("Hello Sir!")

        return True
    # ------------------------------------------------------
# TIME COMMANDS
# ------------------------------------------------------

    elif command in TIME_COMMANDS:

        current_time = show_time()

        show_hud(
            command="time",
            command_type="LOCAL",
            status="SUCCESS",
            extra=f"Current Time : {current_time}"
        )

        say(f"Sir, Current time is {current_time}")

        return True


# ------------------------------------------------------
# DATE COMMANDS
# ------------------------------------------------------

    elif command in DATE_COMMANDS:

        current_date = show_date()

        show_hud(
            command="date",
            command_type="LOCAL",
            status="SUCCESS",
            extra=f"Current Date : {current_date}"
        )

        say(f"Sir, Today's date is {current_date}")

        return True


# ------------------------------------------------------
# IDENTITY COMMAND
# ------------------------------------------------------

    elif command == "your name":

        print("I'm Jarvis")

        say("I'm Jarvis")

        return True


# ------------------------------------------------------
# STATUS COMMAND
# ------------------------------------------------------

    elif command in [
        "how are you",
        "how r u",
        "how are u",
        "how you doing",
        "how do you do"
    ]:

        print("I'm Fine Sir.")

        say("I'm doing well, Sir. How can I help you?")

        return True


# ------------------------------------------------------
# EXIT COMMAND
# ------------------------------------------------------

    elif command in [
        "exit jarvis",
        "turn off jarvis",
        "shut down jarvis",
        "goodbye jarvis"
    ]:

        say("Jarvis Shutting off. Goodbye Sir!")

        return False


    # Command not handled
    return None



#---------------------------------------------------------------------------------------------------



#function create karenge user command call karne ke liye
def execute_command(command):

    print(f"DEBUG Command Received: '{command}'")

    words = command.split()

    print(f"\nCommand: {command}")

    if not words:
        say("Yes,Sir?")
        return True

    #actually this below line is used for debugging whether ai is detecting or not
    #print(f"AI Detection: {is_ai_command(command)}")


# ==========================================================
# Check Browser Commands
#
# If the command belongs to Browser Handler,
# execute it and stop further checking.
# ==========================================================

    result = handle_browser_commands(words, command)

    if result is not None:
        return result

# ==========================================================
# Check Weather Commands
#
# If the command belongs to Weather Handler,
# execute it and stop further checking.
# ==========================================================

    result = handle_weather_commands(words, command)

    if result is not None:
        return result


# ==========================================================
# Check Media Commands
#
# If the command belongs to Media Handler,
# execute it and stop further checking.
# ==========================================================

    result = handle_media_commands(command)

    if result is not None:
        return result


# ==========================================================
# Check Notes Commands
#
# If the command belongs to Notes Handler,
# execute it and stop further checking.
# ==========================================================

    result = handle_notes_commands(words)

    if result is not None:
        return result


# ==========================================================
# Check System Commands
#
# If the command belongs to System Handler,
# execute it and stop further checking.
# ==========================================================

    result = handle_system_command(command)

    if result is not None:
        return result


# ==========================================================
# Check App Commands
#
# If the command belongs to App Handler,
# execute it and stop further checking.
# ==========================================================

    result = handle_app_commands(command)

    if result is not None:
        return result


# ==========================================================
# Check Screenshot Commands
#
# If the command belongs to Screenshot Handler,
# execute it and stop further checking.
# ==========================================================

    result = handle_screenshot_commands(command)

    if result is not None:
        return result


# ==========================================================
# Check File Commands
#
# If the command belongs to File Handler,
# execute it and stop further checking.
# ==========================================================

    result = handle_file_commands(command)

    if result is not None:
        return result




#-------------------------------------------------------------------------------------------------
    

# ==========================================================
# AI FALLBACK
#
# If no local handler recognizes the command,
# forward it to Gemini AI.
# ==========================================================

    answer, response_time, api_calls = ask_gemini(command)

    if answer:

        show_hud(
            command=command,
            command_type="AI",
            status="SUCCESS",
            response_time=response_time,
            api_calls=api_calls
        )

        print(answer)
        say(answer)

    else:

        show_hud(
            command=command,
            command_type="AI",
            status="FAILED",
            api_calls=api_calls
        )

        say("Sorry Sir, Gemini is unavailable right now. Please try again later.")

    return True





