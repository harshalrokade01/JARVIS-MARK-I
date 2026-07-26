#so hum jo bhi commands de rhe the jarvis ko wo ab yaha shift kar denge taaki difficulty na ho aur scalability badh jaye

#importing 
from modules.apps import open_notepad, open_chrome, open_app

from modules.browser import open_website, search_google, play_youtube, find_amazon

from modules.datetime_module import show_time, show_date

from youtubesearchpython import VideosSearch

#MISSION 22 IMPORTING SCREENSHOT FROM SCREENSHOT.PY
from modules.screenshot import take_screenshot

#mission 24 Importing notes from notes.py
from modules.notes import save_note 


#importing speech module taaaki jarvis bol sake
from modules.speech import say

#importing weather function
from modules.weather import get_weather

#gemini ai use ho sake jarvis me
from modules.ai import ask_gemini


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






#function create karenge user command call karne ke liye
def execute_command(command):

    words = command.split()

    print(f"\nCommand: {command}")

    if not words:
        say("Yes,Sir?")
        return True


    if command in ["hi jarvis", "what is jarvis", "hello jarvis", "hey jarvis"]:
        say("Hello Sir!")
        return True

    elif command == "exit jarvis":
        say("Jarvis Shutting off, GoodBye Sir!")
        return False


    elif command == "time":
        current_time = show_time()
        say(f"Sir, Current time is {current_time}")


    elif command == "date":
        current_date = show_date()
        say(f"Sir, Today's Date is {current_date}")


    elif command == "notepad":
        say("Opening Notepad Sir")
        open_notepad()


    elif command == "chrome":
        say("Opening Chrome Sir")
        open_chrome()


    elif command == "your name":
        print("I'm Jarvis")
        say("I'm Jarvis")


    elif command == "how r u":
        print("I'm Fine Sir.")
        say("I'm doing well, Sir. How can I help you?")


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

            result = get_weather(city)

            if result is None:
                say("Sorry Sir, I Couldn't find that city.")


            else:
                city_name, temp, humidity, weather = result

                print(f"City: {city_name}")
                print(f"Temperature: {temp}°C")
                print(f"Humidity: {humidity}")
                print(f"Weather: {weather}")

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

    elif command in ["pause", "pause music", "stop music", "stop song"]:
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

        answer = ask_gemini(command)

        if answer:
            print(answer)
            say(answer)

        else:
            say("Sorry Sir, Gemini is unavailable right now. Please try again later.")

    else:
        say("Sorry Sir, I don't know that command.")

    return True





