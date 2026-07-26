#creating function for command through microphone

def takeCommand():
#MISSION 15: JARVIS WILL LISTEN OUR COMMANDS NOW
    import speech_recognition as sr
    recognizer = sr.Recognizer()

    recognizer.pause_threshold = 1
    recognizer.energy_threshold = 300
    recognizer.dynamic_energy_threshold = True

    with sr.Microphone() as source:
        print("Adjusting for ambient noise...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Listening...")
        audio = recognizer.listen(
            source,
            timeout=5,
            phrase_time_limit=8
        )
    try:
        #converting to text
        text = recognizer.recognize_google(audio, language="en-IN") 
        text = text.lower()
        text = text.replace("service", "jarvis")
        text = text.replace("jarviss", "jarvis")
        text = text.replace("jervis", "jarvis")
        text = text.replace("travis", "jarvis")
        #print the text
        print(text)
        return text.lower()

    except Exception:
        print("Sorry Sir, I Couldn't Understand...")
        return None