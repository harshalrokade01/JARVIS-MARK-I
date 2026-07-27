




#creating function for command through microphone


def takeCommand():
#MISSION 15: JARVIS WILL LISTEN OUR COMMANDS NOW
    import speech_recognition as sr

    recognizer = sr.Recognizer()

    recognizer.pause_threshold = 0.8
    recognizer.energy_threshold = 250
    recognizer.dynamic_energy_threshold = True

    try:
        with sr.Microphone() as source:

            print("Adjusting for ambient noise...")
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
    
            print("Listening...")

            audio = recognizer.listen(
            source,
            timeout=8,
            phrase_time_limit=10
            )

        #converting speech to text
        text = recognizer.recognize_google(audio, language="en-IN") 
        text = text.lower()

# ---------------- COMMAND NORMALIZATION ---------------- #
        # Fix common speech recognition mistakes
        text = text.replace("service", "jarvis")
        text = text.replace("jarviss", "jarvis")
        text = text.replace("jervis", "jarvis")
        text = text.replace("travis", "jarvis")

        text = text.replace("vedar", "weather")
        text = text.replace("whether", "weather")
        text = text.replace("wether", "weather")
        text = text.replace("vedhar", "weather")

# ---------------- MEDIA COMMAND NORMALIZATION ---------------- #

        text = text.replace("pose", "pause")
        text = text.replace("pausee", "pause")
        text = text.replace("boss", "pause")
        text = text.replace("paws", "pause")
        text = text.replace("pass", "pause")

# ---------------- SYSTEM COMMAND NORMALIZATION ---------------- #

        text = text.replace("state", "date")
        text = text.replace("data", "date")
        text = text.replace("today date", "today's date")



#-----------------------------------------------------------------
        #print the text
        print(text)

        return text

    except sr.WaitTimeoutError:
        print("No voice detected. Listening again...")
        return None

    except sr.UnknownValueError:
        print("Sorry Sir, I couldn't understand.")
        return None

    except sr.RequestError as e:
        print(f"Google Speech Error: {e}")
        return None

    except Exception as e:
        print(f"Unexpected Error: {e}")
        return None
