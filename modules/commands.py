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


#importing commands for play,pause, volume up and down
from modules.media import(
    pause_media,
    next_media,
    previous_media,
    volume_up,
    volume_down,
    mute_volume
)




#ek function banayenge taki ye "query  = " ".join(words[1:])" baar baar call ho sake aur har function me baar baar likhna naa pade
def get_query(words):
    return " ".join(words[1:])

#COMMAND ANALYZER FOR GENAI
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
    elif command in ["turn off jarvis", "exit jarvis", "switch off jarvis"]:

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

        

    










#function create karenge user command call karne ke liye
def execute_command(command):

    words = command.split()

    print(f"\nCommand: {command}")

    if not words:
        say("Yes,Sir?")
        return True

    
# Check if the command belongs to System Commands.
# If handled, no need to execute the remaining command checks.


#    result = handle_system_command(command)
#    if result is not None:
#        return result
# ---------------- GREETING COMMANDS ---------------- #

    if command in ["hi jarvis", "hii jarvis", "hello jarvis", "hey jarvis"]:
        say("Hello Sir!")
        return True


# ---------------- EXIT COMMAND ---------------- #

    elif command in ["turn off jarvis", "exit jarvis", "shut down jarvis"]:
        say("Jarvis Shutting off, GoodBye Sir!")
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

        say(f"Sir, Current time is {current_time}")
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
        say("I'm doing well, Sir. How can I help you?")
        return True


    elif command == "notepad":
        say("Opening Notepad Sir")
        open_notepad()


    elif command == "chrome":
        say("Opening Chrome Sir")
        open_chrome()


#MAIN FUNCTIONS FOR TASK 
    elif words[0] == "open":

        if len(words)> 1:
            query  = get_query(words)
            say(f"Opening {query} Sir")
            if not open_app(query):
                open_website(query)

        else:
            say("Please Tell Me which website to open")


    elif words[0] == "search":

        if len(words)> 1:
            #query function banaya hai istead of commands hum .join(words) use kar rhe to get clean and neat code

            query  = get_query(words)
            say(f"Searching {query} on Google, Sir")
            search_google(query)

        else:
            say("Please Tell Me what to search, Sir")

#finally automatic song play kar sakte h with the help of jarvis, gemini ai and youtube
    elif words[0] == "play":

        if len(words) > 1:
            query  = get_query(words)
            say(f"Playing {query} on Youtube, Sir")
            play_youtube(query)

        else:
            say("Please Tell Me Which Song to play, Sir")


    elif words[0] == "buy":

        if len(words) > 1:
            query  = get_query(words)
            say(f"Searching Amazon for {query}, Sir")
            find_amazon(query)

        else:
            say("Please Tell Me What Product to Find, Sir")


#    elif words[0] == "jarvis":
#
#        if len(words) > 1:
#            query = get_query(words)
#
#            answer = ask_gemini(query)
#
#            print(answer)
#            say(answer)        
#
#        else:
#            say("I'm listening, Sir. What would you like to know?")


#FUNCTION FOR SCREENSHOT BY SAYING
    elif command in ["take screenshot","screenshot"]:

        filename = take_screenshot()

        print(f"Screenshot Saved as: {filename}")

        say("Screenshot Captured  and Saved Successfully, Sir.")


#function for getting weather information by saying
    elif words[0] == "weather":

        if len(words) > 1:
            city = get_query(words)

            start_time = time.perf_counter()

            result = get_weather(city)

            end_time = time.perf_counter()

            response_time= end_time - start_time

            if result is None:
                say("Sorry Sir, I Couldn't find that city.")


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

                #print(f"City: {city_name}")
                #print(f"Temperature: {temp}°C")
                #print(f"Humidity: {humidity}")
                #print(f"Weather: {weather}")

                say(f"Sir, in {city_name}, the temperature is {temp} degree celcius with {weather}.")

        else:
            say("Please tell me the city name, Sir.")


#function for saving notes automatically to jarvis by saying
    elif words[0] == "note":

        if len(words) > 1:
            note = get_query(words)

            filepath = save_note(note)

            print(f"Note Saved in {filepath}")

            say("Your Note has been Saved Successfully, Sir.")

        else: 
            say("Please tell me what to save, Sir.")

#commands for shortcut buttons

    elif command in ["pause", "pause music", "top music", "top song", "stop music", "stop song"]:
        pause_media()

    elif command in ["resume", "continue", "play music", "continue music"]:
        pause_media()

    elif command in ["next", "next song", "skip"]:
        next_media()

    elif command in ["previous", "previous song", "back"]:
        previous_media()

    elif command in ["volume up", "volume", "volume of", "increase volume", "louder"]:
        volume_up()

    elif command in ["volume down", "decrease volume", "lower volume", "softer"]:
        volume_down()

    elif command in ["mute", "mute volume", "silent"]:
        mute_volume()


    
    elif is_ai_command(command):

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

    else:
        say("Sorry Sir, I don't know that command.")

    return True





